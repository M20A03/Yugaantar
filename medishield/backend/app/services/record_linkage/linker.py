"""Fellegi-Sunter & multi-field privacy-aware cross-hospital record linkage."""

import hashlib
import hmac
import math
import os
import re
import secrets
from collections import defaultdict
from typing import Dict, List, Set, Tuple

from rapidfuzz import fuzz
from rapidfuzz.distance import JaroWinkler

from app.models.schemas import HospitalRecordInput, LinkageCluster, LinkagePair
from app.services.pii_detection.detector import normalize_text, transliterate_devanagari


HONORIFICS_RE = re.compile(r"\b(?:mr|mrs|ms|shri|smt|dr|ji|sahab|saheb|didi|bhai)\b", re.IGNORECASE)


def _norm_name(name: str | None) -> str:
    if not name:
        return ""
    s = transliterate_devanagari(normalize_text(name)).lower()
    s = HONORIFICS_RE.sub("", s)
    s = re.sub(r"[^a-z\s]", " ", s)
    s = s.replace("aa", "a").replace("ee", "i").replace("oo", "u").replace("ph", "f")
    s = re.sub(r"\b(?:mohammad|mohammed|muhammad|mohmmd|mohd|md)\b", "mohd", s)
    return " ".join(s.split())


def _norm_phone(phone: str | None) -> str:
    if not phone:
        return ""
    digits = re.sub(r"\D", "", phone)
    return digits[-10:] if len(digits) >= 10 else digits


def _char_ngram_jaccard(a: str, b: str, n: int = 3) -> float:
    if not a or not b:
        return 0.0
    ga = {a[i : i + n] for i in range(max(1, len(a) - n + 1))}
    gb = {b[i : i + n] for i in range(max(1, len(b) - n + 1))}
    return len(ga & gb) / max(1, len(ga | gb))


def _soundex_token(token: str) -> str:
    if not token:
        return ""
    token = token.upper()
    first = token[0]
    mapping = {
        "B": "1", "F": "1", "P": "1", "V": "1",
        "C": "2", "G": "2", "J": "2", "K": "2", "Q": "2", "S": "2", "X": "2", "Z": "2",
        "D": "3", "T": "3", "L": "4", "M": "5", "N": "5", "R": "6",
    }
    encoded = [first]
    prev = mapping.get(first, "")
    for ch in token[1:]:
        code = mapping.get(ch, "")
        if code and code != prev:
            encoded.append(code)
        prev = code
    return ("".join(encoded) + "000")[:4]


class RecordLinkageEngine:
    """Three-tier probabilistic linkage: high_confidence_match, uncertain_review, non_match."""

    def __init__(self, secret_key: str | None = None, release_scope: str = "linkage-default") -> None:
        self._master = (secret_key or os.environ.get("RAKSHA_SECRET") or secrets.token_hex(32)).encode("utf-8")
        self._scope = release_scope

    def _pseudonym(self, seed: str) -> str:
        msg = f"medishield:v1:{self._scope}:cluster:{seed}".encode("utf-8")
        h = hmac.new(self._master, msg, hashlib.sha256).hexdigest()[:6].upper()
        return f"PSN-{h}"

    @staticmethod
    def _llr(sim: float, m_prob: float, u_prob: float) -> float:
        if sim >= 0.88:
            return math.log2(m_prob / u_prob)
        if sim >= 0.70:
            return math.log2((m_prob * 0.6) / max(u_prob, 0.05))
        return math.log2((1.0 - m_prob) / (1.0 - u_prob))

    def analyze(
        self, records: List[HospitalRecordInput], threshold: float = 0.72
    ) -> Tuple[int, List[LinkagePair], List[LinkageCluster]]:
        blocks: Dict[str, List[int]] = defaultdict(list)
        normed: List[Dict[str, str]] = []

        for idx, rec in enumerate(records):
            n_name = _norm_name(rec.name)
            n_phone = _norm_phone(rec.phone)
            normed.append({"name": n_name, "phone": n_phone})
            for tok in n_name.split():
                if len(tok) >= 2:
                    blocks[f"sx:{_soundex_token(tok)}"].append(idx)
            if len(n_phone) >= 4:
                blocks[f"ph:{n_phone[-4:]}"].append(idx)

        seen_pairs: Set[Tuple[int, int]] = set()
        for idxs in blocks.values():
            if len(idxs) < 2 or len(idxs) > 80:
                continue
            for i in range(len(idxs)):
                for j in range(i + 1, len(idxs)):
                    a, b = idxs[i], idxs[j]
                    if a > b:
                        a, b = b, a
                    seen_pairs.add((a, b))

        flagged: List[LinkagePair] = []
        adj: Dict[int, List[Tuple[int, float]]] = defaultdict(list)

        for a, b in sorted(seen_pairs):
            ra, rb = records[a], records[b]
            na, nb = normed[a]["name"], normed[b]["name"]
            pa, pb = normed[a]["phone"], normed[b]["phone"]

            field_scores: Dict[str, float] = {}
            reasons: List[str] = []
            weight_sum = 0.0
            score_sum = 0.0
            llr_total = 0.0

            if na and nb:
                jw = JaroWinkler.normalized_similarity(na, nb)
                tok = fuzz.token_set_ratio(na, nb) / 100.0
                ngram = _char_ngram_jaccard(na, nb, 3)
                name_sim = 0.45 * jw + 0.35 * tok + 0.20 * ngram
                field_scores["name"] = round(name_sim, 3)
                weight_sum += 0.45
                score_sum += 0.45 * name_sim
                llr_total += self._llr(name_sim, 0.92, 0.04)
                if name_sim >= 0.78:
                    reasons.append(f"Name similarity {name_sim:.2f}")

            if pa and pb:
                ph_sim = 1.0 if pa == pb else fuzz.ratio(pa, pb) / 100.0
                field_scores["phone"] = round(ph_sim, 3)
                weight_sum += 0.35
                score_sum += 0.35 * ph_sim
                llr_total += self._llr(ph_sim, 0.96, 0.005)
                if ph_sim >= 0.85:
                    reasons.append(f"Phone match {ph_sim:.2f}")
                elif ph_sim < 0.60:
                    # Different phone numbers is strong contradictory evidence
                    llr_total -= 4.0

            if ra.age is not None and rb.age is not None:
                diff = abs(ra.age - rb.age)
                age_sim = 1.0 if diff == 0 else (0.7 if diff <= 2 else 0.0)
                field_scores["age"] = age_sim
                weight_sum += 0.10
                score_sum += 0.10 * age_sim
                if age_sim > 0:
                    llr_total += 1.5
                    reasons.append(f"Age proximity (diff={diff})")
                elif diff > 5:
                    continue

            if ra.gender and rb.gender:
                g_sim = 1.0 if ra.gender.strip().lower()[:1] == rb.gender.strip().lower()[:1] else 0.0
                field_scores["gender"] = g_sim
                weight_sum += 0.10
                score_sum += 0.10 * g_sim
                if g_sim == 0.0:
                    continue

            if weight_sum == 0.0:
                continue

            final_score = round(score_sum / weight_sum, 3)
            has_strong_id = field_scores.get("phone", 0.0) >= 0.90
            agreeing = sum(1 for v in field_scores.values() if v >= 0.75)

            if final_score >= 0.85 and (has_strong_id or agreeing >= 3) and llr_total >= 4.0:
                decision = "high_confidence_match"
            elif final_score >= threshold and agreeing >= 2:
                decision = "uncertain_review"
            else:
                continue

            flagged.append(
                LinkagePair(
                    record_a=ra.record_id,
                    record_b=rb.record_id,
                    hospital_a=ra.hospital,
                    hospital_b=rb.hospital,
                    score=final_score,
                    fellegi_sunter_llr=round(llr_total, 2),
                    decision=decision,
                    field_scores=field_scores,
                    reasons=reasons or ["Composite weighted match"],
                )
            )
            # Only auto-cluster high-confidence matches (conservative clustering)
            if decision == "high_confidence_match":
                adj[a].append((b, final_score))
                adj[b].append((a, final_score))

        visited: Set[int] = set()
        clusters: List[LinkageCluster] = []
        for idx in range(len(records)):
            if idx in visited or idx not in adj:
                continue
            comp: List[int] = []
            edge_scores: List[float] = []
            stack = [idx]
            visited.add(idx)
            while stack:
                cur = stack.pop()
                comp.append(cur)
                for nxt, sc in adj[cur]:
                    edge_scores.append(sc)
                    if nxt not in visited:
                        visited.add(nxt)
                        stack.append(nxt)
            if len(comp) >= 2:
                rec_ids = sorted(records[i].record_id for i in comp)
                hospitals = sorted({records[i].hospital for i in comp})
                clusters.append(
                    LinkageCluster(
                        cluster_id=f"CLU-{len(clusters)+1:03d}",
                        pseudonym=self._pseudonym("|".join(rec_ids)),
                        record_ids=rec_ids,
                        hospitals=hospitals,
                        avg_confidence=round(sum(edge_scores) / max(1, len(edge_scores)), 3),
                    )
                )

        return len(seen_pairs), flagged, clusters

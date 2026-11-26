"""Privacy-aware cross-hospital record linkage using blocking and RapidFuzz."""

import hashlib
import hmac
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
    # Normalize common Indian transliteration variants & phonetic equivalents
    s = s.replace("aa", "a").replace("ee", "i").replace("oo", "u").replace("ph", "f")
    s = re.sub(r"\b(?:mohammad|mohammed|muhammad|mohmmd|mohd|md)\b", "mohd", s)
    return " ".join(s.split())


def _norm_phone(phone: str | None) -> str:
    if not phone:
        return ""
    digits = re.sub(r"\D", "", phone)
    return digits[-10:] if len(digits) >= 10 else digits


def _soundex_token(token: str) -> str:
    if not token:
        return ""
    token = token.upper()
    first = token[0]
    mapping = {
        "B": "1", "F": "1", "P": "1", "V": "1",
        "C": "2", "G": "2", "J": "2", "K": "2", "Q": "2", "S": "2", "X": "2", "Z": "2",
        "D": "3", "T": "3",
        "L": "4",
        "M": "5", "N": "5",
        "R": "6",
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
    """Finds potential cross-hospital linkage risks without exposing raw identities."""

    def __init__(self, secret_key: str | None = None) -> None:
        self._secret = (
            secret_key or os.environ.get("RAKSHA_SECRET") or secrets.token_hex(32)
        ).encode("utf-8")

    def _pseudonym(self, seed: str) -> str:
        h = hmac.new(self._secret, seed.encode("utf-8"), hashlib.sha256).hexdigest()[:6].upper()
        return f"PSN-{h}"

    def analyze(
        self, records: List[HospitalRecordInput], threshold: float = 0.72
    ) -> Tuple[int, List[LinkagePair], List[LinkageCluster]]:
        blocks: Dict[str, List[int]] = defaultdict(list)
        normed: List[Dict[str, str]] = []

        for idx, rec in enumerate(records):
            n_name = _norm_name(rec.name)
            n_phone = _norm_phone(rec.phone)
            normed.append({"name": n_name, "phone": n_phone})
            tokens = n_name.split()
            for tok in tokens:
                if len(tok) >= 2:
                    blocks[f"sx:{_soundex_token(tok)}"].append(idx)
            if len(n_phone) >= 4:
                blocks[f"ph:{n_phone[-4:]}"].append(idx)
            if rec.gender:
                blocks[f"g:{rec.gender.strip().lower()[:1]}"].append(idx)

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

            if na and nb:
                jw = JaroWinkler.normalized_similarity(na, nb)
                tok = fuzz.token_set_ratio(na, nb) / 100.0
                name_sim = 0.55 * jw + 0.45 * tok
                field_scores["name"] = round(name_sim, 3)
                weight_sum += 0.50
                score_sum += 0.50 * name_sim
                if name_sim >= 0.78:
                    reasons.append(f"Name similarity {name_sim:.2f} (normalized/transliterated)")

            if pa and pb:
                ph_sim = 1.0 if pa == pb else fuzz.ratio(pa, pb) / 100.0
                field_scores["phone"] = round(ph_sim, 3)
                weight_sum += 0.30
                score_sum += 0.30 * ph_sim
                if ph_sim >= 0.85:
                    reasons.append(f"Phone match {ph_sim:.2f}")

            if ra.age is not None and rb.age is not None:
                diff = abs(ra.age - rb.age)
                age_sim = 1.0 if diff == 0 else (0.7 if diff <= 2 else 0.0)
                field_scores["age"] = age_sim
                weight_sum += 0.10
                score_sum += 0.10 * age_sim
                if age_sim > 0:
                    reasons.append(f"Age proximity (diff={diff})")

            if ra.gender and rb.gender:
                g_sim = 1.0 if ra.gender.strip().lower()[:1] == rb.gender.strip().lower()[:1] else 0.0
                field_scores["gender"] = g_sim
                weight_sum += 0.10
                score_sum += 0.10 * g_sim
                if g_sim == 0.0:
                    # Strong negative evidence against linking
                    score_sum *= 0.5

            if weight_sum == 0.0:
                continue

            final_score = round(score_sum / weight_sum, 3)
            if final_score >= threshold:
                flagged.append(
                    LinkagePair(
                        record_a=ra.record_id,
                        record_b=rb.record_id,
                        hospital_a=ra.hospital,
                        hospital_b=rb.hospital,
                        score=final_score,
                        field_scores=field_scores,
                        reasons=reasons or ["Composite weighted match"],
                    )
                )
                adj[a].append((b, final_score))
                adj[b].append((a, final_score))

        # Connected components with average-edge guard to prevent transitive over-merging
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

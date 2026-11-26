"""Shared training & inference feature extraction for MediShield Record Linkage V3.

Ensures zero train/serve skew and cleanly separates missing fields from
contradictory evidence.
"""

import re
from typing import Any, Dict, List

from rapidfuzz import fuzz
from rapidfuzz.distance import JaroWinkler, Levenshtein

from app.services.pii_detection.detector import normalize_text, transliterate_devanagari


HONORIFICS_RE = re.compile(r"\b(?:mr|mrs|ms|shri|smt|dr|ji|sahab|saheb|didi|bhai)\b", re.IGNORECASE)

FEATURE_NAMES: List[str] = [
    "name_jw",
    "name_lev",
    "name_ngram",
    "name_token_set",
    "name_phonetic",
    "last_name_sim",
    "phone_exact",
    "phone_near",
    "phone_available",
    "age_diff",
    "age_missing",
    "dob_agree",
    "address_sim",
    "gender_agree",
    "missing_fraction",
    "contradictory_evidence",
]


def norm_name(name: str | None) -> str:
    if not name:
        return ""
    s = transliterate_devanagari(normalize_text(name)).lower()
    s = HONORIFICS_RE.sub("", s)
    s = re.sub(r"[^a-z\s]", " ", s)
    s = s.replace("aa", "a").replace("ee", "i").replace("oo", "u").replace("ph", "f")
    s = re.sub(r"\b(?:mohammad|mohammed|muhammad|mohmmd|mohd|md)\b", "mohd", s)
    return " ".join(s.split())


def norm_phone(phone: str | None) -> str:
    if not phone:
        return ""
    digits = re.sub(r"\D", "", phone)
    return digits[-10:] if len(digits) >= 10 else digits


def char_ngram_jaccard(a: str, b: str, n: int = 3) -> float:
    if not a or not b:
        return 0.0
    ga = {a[i : i + n] for i in range(max(1, len(a) - n + 1))}
    gb = {b[i : i + n] for i in range(max(1, len(b) - n + 1))}
    return len(ga & gb) / max(1, len(ga | gb))


def soundex_token(token: str) -> str:
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


def extract_pair_features(ra: Dict[str, Any], rb: Dict[str, Any]) -> List[float]:
    na, nb = norm_name(ra.get("name")), norm_name(rb.get("name"))
    pa, pb = norm_phone(ra.get("phone")), norm_phone(rb.get("phone"))
    aa, ab = norm_name(ra.get("address")), norm_name(rb.get("address"))

    name_jw = JaroWinkler.normalized_similarity(na, nb) if (na and nb) else 0.0
    name_lev = Levenshtein.normalized_similarity(na, nb) if (na and nb) else 0.0
    name_ngram = char_ngram_jaccard(na, nb, 3)
    name_token_set = (fuzz.token_set_ratio(na, nb) / 100.0) if (na and nb) else 0.0

    toks_a, toks_b = na.split(), nb.split()
    sa = {soundex_token(t) for t in toks_a if t}
    sb = {soundex_token(t) for t in toks_b if t}
    name_phonetic = (len(sa & sb) / max(1, len(sa | sb))) if (sa and sb) else 0.0
    last_name_sim = JaroWinkler.normalized_similarity(toks_a[-1], toks_b[-1]) if (toks_a and toks_b) else 0.0

    phone_available = 1.0 if (pa and pb) else 0.0
    phone_exact = 1.0 if (pa and pb and pa == pb) else 0.0
    phone_dist = Levenshtein.distance(pa, pb) if (pa and pb) else 99
    phone_near = 1.0 if (pa and pb and phone_dist <= 1) else 0.0

    age_a, age_b = ra.get("age"), rb.get("age")
    age_missing = 1.0 if (age_a is None or age_b is None) else 0.0
    age_diff = (abs(age_a - age_b) / 100.0) if (age_a is not None and age_b is not None) else 0.0

    dob_a, dob_b = (ra.get("dob") or "").strip(), (rb.get("dob") or "").strip()
    dob_agree = 1.0 if (dob_a and dob_b and dob_a == dob_b) else 0.0

    address_sim = (fuzz.token_set_ratio(aa, ab) / 100.0) if (aa and ab) else 0.0

    ga = (ra.get("gender") or "").strip().lower()[:1]
    gb = (rb.get("gender") or "").strip().lower()[:1]
    gender_agree = 1.0 if (ga and gb and ga == gb) else 0.0

    missing_cnt = sum([
        1 if (not pa or not pb) else 0,
        1 if (age_a is None or age_b is None) else 0,
        1 if (not aa or not ab) else 0,
        1 if (not ga or not gb) else 0,
    ])
    missing_fraction = missing_cnt / 4.0

    contra_age = (age_a is not None and age_b is not None and abs(age_a - age_b) > 5)
    contra_gender = (bool(ga) and bool(gb) and ga != gb)
    contra_dob = (bool(dob_a) and bool(dob_b) and dob_a != dob_b)
    # Two 10-digit phones differing by >= 3 digits are contradictory (not a 1-2 digit typo)
    contra_phone = (bool(pa) and bool(pb) and phone_dist >= 3)
    contradictory = 1.0 if (contra_age or contra_gender or contra_dob or contra_phone) else 0.0

    return [
        float(name_jw),
        float(name_lev),
        float(name_ngram),
        float(name_token_set),
        float(name_phonetic),
        float(last_name_sim),
        float(phone_exact),
        float(phone_near),
        float(phone_available),
        float(age_diff),
        float(age_missing),
        float(dob_agree),
        float(address_sim),
        float(gender_agree),
        float(missing_fraction),
        float(contradictory),
    ]

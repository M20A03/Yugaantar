"""Offline, LLM-free multilingual PII detection engine (English, Hindi, Hinglish).

Combines Unicode NFKC normalization, Devanagari-to-Latin transliteration,
precision regexes, contextual keyword/relative disambiguation, clinical
entity protection, and a lightweight scikit-learn TF-IDF + LogisticRegression
context classifier trained on deterministic synthetic patterns.
"""

import os
import re
import unicodedata
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from app.models.schemas import DetectedEntity


# Devanagari to Latin transliteration table for cross-script matching
DEVANAGARI_MAP: Dict[str, str] = {
    "अ": "a", "आ": "aa", "इ": "i", "ई": "ee", "उ": "u", "ऊ": "oo", "ऋ": "ri",
    "ए": "e", "ऐ": "ai", "ओ": "o", "औ": "au", "अं": "an", "अः": "ah",
    "क": "k", "ख": "kh", "ग": "g", "घ": "gh", "ङ": "ng",
    "च": "ch", "छ": "chh", "ज": "j", "झ": "jh", "ञ": "ny",
    "ट": "t", "ठ": "th", "ड": "d", "ढ": "dh", "ण": "n",
    "त": "t", "थ": "th", "द": "d", "ध": "dh", "न": "n",
    "प": "p", "फ": "ph", "ब": "b", "भ": "bh", "म": "m",
    "य": "y", "र": "r", "ल": "l", "व": "v", "श": "sh",
    "ष": "sh", "स": "s", "ह": "h", "ळ": "l",
    "ा": "a", "ि": "i", "ी": "ee", "ु": "u", "ू": "oo",
    "े": "e", "ै": "ai", "ो": "o", "ौ": "au", "ं": "n", "ः": "h",
    "्": "", "ँ": "n", "़": "", "क़": "q", "ख़": "kh", "ग़": "g",
    "ज़": "z", "ड़": "r", "ढ़": "rh", "फ़": "f",
    "०": "0", "१": "1", "२": "2", "३": "3", "४": "4",
    "५": "5", "६": "6", "७": "7", "८": "8", "९": "9",
}

CLINICAL_WHITELIST = {
    "diabetes", "type 2 diabetes", "type 1 diabetes", "hypertension", "dengue",
    "malaria", "typhoid", "tuberculosis", "asthma", "copd", "parkinson",
    "parkinson's disease", "alzheimer", "metformin", "ramipril", "dolo",
    "paracetamol", "amoxicillin", "atorvastatin", "insulin", "azithromycin",
    "aspirin", "pantoprazole", "fever", "cough", "headache", "chest pain",
    "breathlessness", "vomiting", "bp", "spo2", "hb", "hba1c", "ecg",
    "mg", "ml", "mcg", "mmhg", "bpm", "bd", "od", "tds", "hs", "sos",
}

HINGLISH_MARKERS = {
    "ko", "hai", "hain", "ka", "ki", "ke", "sahab", "ji", "didi", "bhai",
    "se", "me", "mein", "aur", "nahi", "bukhar", "dard", "dawai", "goli",
    "umra", "umar", "saal", "mareez", "mariz", "rogi", "pata", "ghar", "gaon", "zila",
}

CLINICAL_COMPLAINT_TERMS = {
    "fever", "bukhar", "cough", "khansi", "pain", "dard", "headache",
    "breathlessness", "weakness", "vomiting", "dizziness", "diabetes",
    "hypertension", "chest pain", "diarrhea", "cold", "infection",
}

NON_NAME_STOPWORDS = {
    "was", "is", "are", "were", "be", "been", "has", "have", "had",
    "yesterday", "today", "tomorrow", "admitted", "brought", "hospital",
    "regarding", "medication", "medicine", "ko", "hai", "hain", "ka", "ki",
    "ke", "se", "me", "mein", "aur", "for", "with", "and", "the", "a", "an",
    "aged", "age", "patient", "marez", "mareez", "mariz", "rogi", "bimar",
    "contact", "phone", "residing", "diagnosis", "disease", "syndrome",
    "aayi", "aaya", "thi", "tha", "to", "from", "in", "on", "at", "of", "by",
    "who", "took", "stayed", "follow", "up", "reports", "summary", "sample",
    "blood", "history", "provided", "collected", "booked", "discussed",
    "normal", "acute", "chronic", "severe", "mild", "positive", "negative",
}

INDIAN_FIRST_NAMES = {
    "rahul", "ananya", "ravi", "priya", "sunita", "mohammed", "mohammad",
    "arif", "aarav", "meera", "rohan", "vikram", "sneha", "karan",
    "siddharth", "kavita", "arjun", "pooja", "aditya", "nikhil", "suresh",
    "manish", "deepak", "neha", "divya", "shruti", "nandini", "amit",
    "rajan", "rajesh", "sanjay", "vijay", "anita", "rekha", "geeta",
    "seema", "kiran", "alok", "ashok", "manoj", "ramesh", "mahesh",
    "ganesh", "vinod", "pradeep", "harish", "prashant", "gaurav", "vivek",
    "tarun", "komal", "swati", "bhavna", "pallavi", "rashmi",
}

INDIAN_SURNAMES = {
    "sharma", "verma", "patel", "iyer", "nair", "gupta", "khan", "das",
    "joshi", "mehta", "kulkarni", "deshmukh", "chatterjee", "banerjee",
    "saxena", "bhatnagar", "subramanian", "krishnan", "rao", "malhotra",
    "singh", "kumar", "devi", "yadav", "agarwal", "tiwari", "mishra",
    "pandey", "chauhan", "reddy", "patil", "kaur",
}

RELATIVE_PREFIX_RE = re.compile(
    r"\b(?:S/[Oo]|D/[Oo]|W/[Oo]|C/[Oo]|son of|daughter of|wife of|care of|पति|पुत्र|पुत्री|निवासी)\b",
    re.IGNORECASE,
)

PATIENT_PREFIX_RE = re.compile(
    r"\b(?:Patient|Pt\.?|Name|Mareez|Mariz|Rogi|Mr\.?|Mrs\.?|Ms\.?|Shri|Smt\.?|नाम|रोगी|मरीज़)\s*[:\-]?\s*",
    re.IGNORECASE,
)

DOCTOR_PREFIX_RE = re.compile(r"\b(?:Dr\.?|Doctor|डॉ\.?)\s+", re.IGNORECASE)

REGEX_RULES: List[Tuple[str, re.Pattern, float]] = [
    ("EMAIL", re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"), 0.99),
    ("PAN", re.compile(r"\b[A-Z]{5}[0-9]{4}[A-Z]\b"), 0.98),
    ("AADHAAR", re.compile(r"\b[2-9][0-9]{3}[\s\-]?[0-9]{4}[\s\-]?[0-9]{4}\b"), 0.95),
    ("ABHA_ID", re.compile(r"\b\d{2}[\-\s]?\d{4}[\-\s]?\d{4}[\-\s]?\d{4}\b"), 0.93),
    ("HOSPITAL_ID", re.compile(r"\b(?:MRN|UHID|REG|PAT|OPD|IPD)[\-_:/]?\d{4,10}\b", re.IGNORECASE), 0.96),
    (
        "PHONE",
        re.compile(
            r"(?<!\d)(?:(?:\+91[\s\-]?|0)?[6-9]\d{4}[\s\-]?\d{5}|\+\d{1,3}[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{4})(?!\d)"
        ),
        0.96,
    ),
    (
        "DOB",
        re.compile(
            r"\b(?:DOB|Date of Birth|जन्म\s*तिथि)\s*[:\-]?\s*(\d{1,2}[/\-\.]\d{1,2}[/\-\.]\d{2,4}|\d{4}[/\-\.]\d{1,2}[/\-\.]\d{1,2})\b",
            re.IGNORECASE,
        ),
        0.95,
    ),
    (
        "PIN_CODE",
        re.compile(r"(?:PIN|Pincode|पिन|Address|residing at|resident of|village|gaon|road|marg)[^.\n]{0,45}?\b([1-9][0-9]{5})\b", re.IGNORECASE),
        0.90,
    ),
]


def normalize_text(text: str) -> str:
    cleaned = re.sub(r"[\u200b-\u200d\ufeff]", "", text)
    return unicodedata.normalize("NFKC", cleaned)


def transliterate_devanagari(text: str) -> str:
    out = []
    for ch in text:
        out.append(DEVANAGARI_MAP.get(ch, ch))
    return "".join(out)


def detect_language(text: str) -> str:
    has_devanagari = bool(re.search(r"[\u0900-\u097F]", text))
    lower_tokens = set(re.findall(r"[a-zA-Z]+", text.lower()))
    has_hinglish = len(lower_tokens & HINGLISH_MARKERS) >= 1
    has_latin = len(lower_tokens) > 0
    if has_devanagari and has_latin:
        return "mixed (hi+en)"
    if has_devanagari:
        return "hi"
    if has_hinglish:
        return "hinglish"
    return "en"


class _ContextNameClassifier:
    """Offline TF-IDF + LogisticRegression classifier (loads trained artifact if present)."""

    def __init__(self) -> None:
        artifacts_dir = Path(__file__).resolve().parents[3] / "artifacts"
        v3_path = artifacts_dir / "pii_model_v3.joblib"
        v2_path = artifacts_dir / "pii_model.joblib"
        artifact = v3_path if v3_path.is_file() else v2_path
        self.pipeline = joblib.load(artifact) if artifact.is_file() else None
        if self.pipeline is not None:
            return
        samples = [
            ("Patient Rahul Sharma admitted with fever", 1),
            ("Pt. Meera Devi W/o Rajan Kumar", 1),
            ("Mr. Mohammad Arif phone 9876543210", 1),
            ("Arif sahab ka BP 150/90 hai", 1),
            ("C/O Ramesh Verma resident of Rampur", 1),
            ("Name: Sunita Yadav aged 45", 1),
            ("Diagnosed with Type 2 Diabetes", 0),
            ("Prescribed Metformin 500 mg BD", 0),
            ("C/O fever and cough since 3 days", 0),
            ("Dr. Rajesh Gupta advised rest", 0),
            ("Parkinson disease follow up note", 0),
            ("Dolo 650 mg 1-0-1 for 5 days", 0),
        ]
        texts = [t for t, _ in samples]
        labels = [y for _, y in samples]
        self.vectorizer = TfidfVectorizer(analyzer="char_wb", ngram_range=(2, 4), lowercase=True)
        X = self.vectorizer.fit_transform(texts)
        self.clf = LogisticRegression(C=2.0, max_iter=300)
        self.clf.fit(X, labels)

    def score_context(self, window: str) -> float:
        if self.pipeline is not None:
            return float(self.pipeline.predict_proba([window])[0][1])
        X = self.vectorizer.transform([window])
        return float(self.clf.predict_proba(X)[0][1])


class MultilingualPIIDetector:
    """Hybrid offline detector for English, Hindi (Devanagari), and Hinglish."""

    def __init__(self) -> None:
        self.ctx_clf = _ContextNameClassifier()

    def scan(self, text: str) -> Tuple[str, List[DetectedEntity]]:
        norm = normalize_text(text)
        language = detect_language(norm)
        candidates: List[DetectedEntity] = []

        # 1. Regex-based structured identifiers
        for entity_type, pattern, conf in REGEX_RULES:
            for match in pattern.finditer(norm):
                if entity_type in {"DOB", "PIN_CODE"} and match.lastindex:
                    start, end = match.span(1)
                    val = match.group(1)
                else:
                    start, end = match.span()
                    val = match.group(0)
                if self._is_clinical_false_positive(val, norm, start, end):
                    continue
                candidates.append(
                    DetectedEntity(
                        entity_type=entity_type,
                        text=val,
                        start=start,
                        end=end,
                        method="regex",
                        confidence=conf,
                        language=language,
                    )
                )

        # 2. Age & Address contextual patterns (English, Hindi, Hinglish + parenthetical yrs)
        age_re = re.compile(
            r"(?:\b(?:aged|age|umra|umar|उम्र)\s*[:\-]?\s*(\d{1,3})\s*(?:years?|yrs?|y/o|saal|साल)?\b|\((\d{1,3})\s*(?:years?|yrs?|y/o)\))",
            re.IGNORECASE,
        )
        for m in age_re.finditer(norm):
            grp = 1 if m.group(1) else 2
            candidates.append(
                DetectedEntity(
                    entity_type="AGE",
                    text=m.group(grp),
                    start=m.start(grp),
                    end=m.end(grp),
                    method="context_rule",
                    confidence=0.92,
                    language=language,
                )
            )

        addr_re = re.compile(
            r"\b(?:residing at|resident of|address|city|from|pata|पता|शहर|निवासी)\s*[:\-]?\s*([A-Za-z0-9\u0900-\u097F,.\-\s]{3,70}?)(?=[.\n,;]|$|\b(?:Contact|Phone|Tel|Mob|Mobile|PIN|diagnosed|admitted|Patient|Pt|Unko|Rx)\b)",
            re.IGNORECASE,
        )
        for m in addr_re.finditer(norm):
            val = m.group(1).strip(" ,.-:")
            if len(val) >= 3:
                s = norm.find(val, m.start(1))
                candidates.append(
                    DetectedEntity(
                        entity_type="ADDRESS",
                        text=val,
                        start=s,
                        end=s + len(val),
                        method="context_rule",
                        confidence=0.89,
                        language=language,
                    )
                )

        # 3. Patient & Relative Names (English, Devanagari, Hinglish)
        self._detect_names(norm, language, candidates)

        # 4. Resolve overlapping spans (prefer longer, higher-confidence spans)
        resolved = self._resolve_overlaps(candidates)
        return language, resolved

    def _is_clinical_false_positive(self, val: str, full_text: str, start: int, end: int) -> bool:
        low = val.strip().lower()
        if low in CLINICAL_WHITELIST:
            return True
        after = full_text[end : end + 15].lower()
        if re.match(r"^\s*(mg|ml|mcg|mmhg|bpm|days?|hrs?|%|units?)\b", after):
            return True
        return False

    def _detect_names(
        self, text: str, language: str, candidates: List[DetectedEntity]
    ) -> None:
        # Pattern A: Explicit patient/attendant prefix (English, Hindi, Hinglish, case-insensitive)
        pat_name_re = re.compile(
            r"\b(?:Patient|Pateint|Patinet|Pt\.?|Name|Naam|Mareez|Marez|Mariz|Rogi|Bimar|Attendant|Guardian|Emergency\s+Contact|OPD\s+Note|IPD\s+Note|Mr\.?|Mrs\.?|Ms\.?|Shri|Smt\.?|नाम|रोगी|मरीज़|मरीज)\s*[:\-]?\s*([A-Za-z\u0900-\u097F][a-zA-Z\u0900-\u097F\.]{1,25}(?:\s+[A-Za-z\u0900-\u097F][a-zA-Z\u0900-\u097F\.]{1,25}){0,2})",
            re.IGNORECASE,
        )
        for m in pat_name_re.finditer(text):
            raw_words = m.group(1).strip(" .,:-").split()
            kept_words: List[str] = []
            for w in raw_words:
                if w.lower().strip(".,:") in NON_NAME_STOPWORDS or w.lower().strip(".,:") in CLINICAL_WHITELIST:
                    break
                kept_words.append(w)
            name_val = " ".join(kept_words).strip(" .,:-")
            if name_val and self._valid_person_name(text, m.start(1), name_val):
                window = text[max(0, m.start() - 20) : min(len(text), m.end() + 20)]
                ml_score = self.ctx_clf.score_context(window)
                candidates.append(
                    DetectedEntity(
                        entity_type="PERSON",
                        text=name_val,
                        start=m.start(1),
                        end=m.start(1) + len(name_val),
                        method="hybrid_nlp_ml",
                        confidence=round(min(0.99, 0.78 + 0.2 * ml_score), 2),
                        language=language,
                    )
                )

        # Pattern A2: Unstructured clinical/conversational subject & prepositional cues (English & Hinglish)
        unstruct_patterns = [
            re.compile(
                r"\b(?:met|spoke\s+with|discussed\s+with|called|saw|examined|visited|kal|check(?:ing)?\s+on|follow\s+up\s+(?:for|on|with)|reports?\s+of|summary\s+for|booked\s+for|collected\s+from|provided\s+by|referred\s+by|consulted\s+with)\s+([A-Za-z\u0900-\u097F]{2,20}\s+[A-Za-z\u0900-\u097F]{2,20})\b",
                re.IGNORECASE,
            ),
            re.compile(
                r"(?:^|[.\n]\s*)([A-Za-z\u0900-\u097F]{2,20}\s+[A-Za-z\u0900-\u097F]{2,20})\s+(?:(?:was|is)\s+)?(?:brought|presented|visited|admitted|complained|reported|tested|hospital\s+aay[aei])\b",
                re.IGNORECASE,
            ),
        ]
        for upat in unstruct_patterns:
            for m in upat.finditer(text):
                name_val = m.group(1).strip()
                # Guard against possessive diseases like "Parkinson's disease"
                after_span = text[m.end(1) : m.end(1) + 12].lower()
                if after_span.startswith("'s") or "disease" in name_val.lower():
                    continue
                if self._valid_person_name(text, m.start(1), name_val):
                    w_parts = name_val.lower().split()
                    window = text[max(0, m.start() - 15) : min(len(text), m.end() + 15)]
                    ml_score = self.ctx_clf.score_context(window)
                    in_lexicon = w_parts[0] in INDIAN_FIRST_NAMES or w_parts[-1] in INDIAN_SURNAMES
                    if in_lexicon or ml_score >= 0.55:
                        candidates.append(
                            DetectedEntity(
                                entity_type="PERSON",
                                text=name_val,
                                start=m.start(1),
                                end=m.start(1) + len(name_val),
                                method="unstructured_ctx",
                                confidence=round(max(0.84, min(0.96, ml_score)), 2) if in_lexicon else round(ml_score, 2),
                                language=language,
                            )
                        )

        # Pattern A3: Unprefixed name before age/gender or in parentheses ("Rahul Sharma, 45/M", "(Rhea Dutta)")
        demo_name_re = re.compile(
            r"(?:^|[.\n]\s*)([A-Z][a-z]{1,20}\s+[A-Z][a-z]{1,20})\s*[,\(]\s*\d{1,3}\s*(?:/|\s)?\s*[MFmf]\b"
        )
        for m in demo_name_re.finditer(text):
            name_val = m.group(1).strip()
            if self._valid_person_name(text, m.start(1), name_val):
                candidates.append(
                    DetectedEntity(
                        entity_type="PERSON",
                        text=name_val,
                        start=m.start(1),
                        end=m.start(1) + len(name_val),
                        method="demographic_ctx",
                        confidence=0.89,
                        language=language,
                    )
                )

        paren_name_re = re.compile(r"\(\s*([A-Z][a-z]{1,20}\s+[A-Z][a-z]{1,20})\s*\)")
        for m in paren_name_re.finditer(text):
            name_val = m.group(1).strip()
            if self._valid_person_name(text, m.start(1), name_val):
                candidates.append(
                    DetectedEntity(
                        entity_type="PERSON",
                        text=name_val,
                        start=m.start(1),
                        end=m.start(1) + len(name_val),
                        method="parenthetical_ctx",
                        confidence=0.87,
                        language=language,
                    )
                )

        # Pattern D: Sliding-window Indian First+Last Name Pair (handles unprefixed lowercase at any word offset)
        word_matches = list(re.finditer(r"\b[A-Za-z]{2,20}\b", text))
        for idx in range(len(word_matches) - 1):
            m1, m2 = word_matches[idx], word_matches[idx + 1]
            gap = text[m1.end() : m2.start()]
            if not gap.isspace():
                continue
            w1, w2 = m1.group(0).lower(), m2.group(0).lower()
            if w1 in INDIAN_FIRST_NAMES and w2 in INDIAN_SURNAMES:
                name_val = text[m1.start() : m2.end()]
                if self._valid_person_name(text, m1.start(), name_val):
                    candidates.append(
                        DetectedEntity(
                            entity_type="PERSON",
                            text=name_val,
                            start=m1.start(),
                            end=m2.end(),
                            method="multilingual_lexicon",
                            confidence=0.90,
                            language=language,
                        )
                    )

        # Pattern B: Hinglish honorifics ("Arif sahab", "Meera ji", "Ramesh bhai")
        hinglish_name_re = re.compile(
            r"\b([A-Z\u0900-\u097F][a-zA-Z\u0900-\u097F]{1,20}(?:\s+[A-Z\u0900-\u097F][a-zA-Z\u0900-\u097F]{1,20})?)\s+(?:ji|sahab|saheb|didi|bhai)\b",
            re.IGNORECASE,
        )
        for m in hinglish_name_re.finditer(text):
            name_val = m.group(1).strip()
            if self._valid_person_name(text, m.start(1), name_val):
                candidates.append(
                    DetectedEntity(
                        entity_type="PERSON",
                        text=name_val,
                        start=m.start(1),
                        end=m.start(1) + len(name_val),
                        method="hinglish_rule",
                        confidence=0.91,
                        language=language,
                    )
                )

        # Pattern C: Relative markers ("S/o Mohan", "W/o Rajan", "C/O Ramesh" vs "C/O fever")
        rel_re = re.compile(
            r"\b(?:S/[Oo]|D/[Oo]|W/[Oo]|C/[Oo]|son of|daughter of|wife of|care of)\s*[:\-]?\s*([A-Za-z\u0900-\u097F]{2,25}(?:\s+[A-Za-z\u0900-\u097F]{2,20})?)",
            re.IGNORECASE,
        )
        for m in rel_re.finditer(text):
            val = m.group(1).strip(" .,:-")
            first_word = val.split()[0].lower()
            if first_word in CLINICAL_COMPLAINT_TERMS or first_word in CLINICAL_WHITELIST:
                continue
            if self._valid_person_name(text, m.start(1), val):
                candidates.append(
                    DetectedEntity(
                        entity_type="RELATIVE_PERSON",
                        text=val,
                        start=m.start(1),
                        end=m.start(1) + len(val),
                        method="meaning_disambiguation",
                        confidence=0.90,
                        language=language,
                    )
                )

    def _valid_person_name(self, full_text: str, start: int, name_val: str) -> bool:
        words = [w.strip(".,:") for w in name_val.lower().split() if w.strip(".,:")]
        if not words:
            return False
        if any(w in CLINICAL_WHITELIST or w in CLINICAL_COMPLAINT_TERMS for w in words):
            return False
        if all(w in NON_NAME_STOPWORDS for w in words):
            return False
        if words[0] in NON_NAME_STOPWORDS:
            return False
        before = full_text[max(0, start - 8) : start]
        if DOCTOR_PREFIX_RE.search(before):
            return False
        return len(name_val) >= 2

    @staticmethod
    def _resolve_overlaps(entities: List[DetectedEntity]) -> List[DetectedEntity]:
        ordered = sorted(entities, key=lambda e: (e.start, -(e.end - e.start), -e.confidence))
        result: List[DetectedEntity] = []
        for ent in ordered:
            if any(not (ent.end <= kept.start or ent.start >= kept.end) for kept in result):
                continue
            result.append(ent)
        return sorted(result, key=lambda e: e.start)

"""Offline, LLM-free multilingual PII detection engine (English, Hindi, Hinglish).

Combines Unicode NFKC normalization, Devanagari-to-Latin transliteration,
precision regexes, contextual keyword/relative disambiguation, clinical
entity protection, and a lightweight scikit-learn TF-IDF + LogisticRegression
context classifier trained on deterministic synthetic patterns.
"""

import re
import unicodedata
from typing import Dict, List, Optional, Tuple

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
    "umra", "saal", "mareez", "rogi", "pata", "ghar", "gaon", "zila",
}

CLINICAL_COMPLAINT_TERMS = {
    "fever", "bukhar", "cough", "khansi", "pain", "dard", "headache",
    "breathlessness", "weakness", "vomiting", "dizziness", "diabetes",
    "hypertension", "chest pain", "diarrhea", "cold", "infection",
}

RELATIVE_PREFIX_RE = re.compile(
    r"\b(?:S/[Oo]|D/[Oo]|W/[Oo]|C/[Oo]|son of|daughter of|wife of|care of|पति|पुत्र|पुत्री|निवासी)\b",
    re.IGNORECASE,
)

PATIENT_PREFIX_RE = re.compile(
    r"\b(?:Patient|Pt\.?|Name|Mareez|Rogi|Mr\.?|Mrs\.?|Ms\.?|Shri|Smt\.?|नाम|रोगी|मरीज़)\s*[:\-]?\s*",
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
    return unicodedata.normalize("NFKC", text)


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
    """Tiny offline TF-IDF + LogisticRegression classifier for ambiguous name contexts."""

    def __init__(self) -> None:
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
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2), lowercase=True)
        X = self.vectorizer.fit_transform(texts)
        self.clf = LogisticRegression(C=2.0, max_iter=300)
        self.clf.fit(X, labels)

    def score_context(self, window: str) -> float:
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
            r"\b(?:residing at|resident of|address|pata|पता|निवासी)\s*[:\-]?\s*([A-Za-z0-9\u0900-\u097F,.\-\s]{4,70}?)(?=[.\n]|$|\b(?:Contact|Phone|Mob|Mobile|PIN|diagnosed|Patient|Pt|Unko)\b)",
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
        # Pattern A: Explicit patient prefix (incl. common typos like Pateint & OPD/IPD Note)
        pat_name_re = re.compile(
            r"\b(?:Patient|Pateint|Patinet|Pt\.?|Name|Mareez|Rogi|OPD\s+Note|IPD\s+Note|Mr\.?|Mrs\.?|Ms\.?|Shri|Smt\.?|नाम|रोगी|मरीज़)\s*[:\-]?\s*([A-Z\u0900-\u097F][a-zA-Z\u0900-\u097F\.]{1,25}(?:\s+[A-Z\u0900-\u097F][a-zA-Z\u0900-\u097F\.]{1,25}){0,2})",
        )
        for m in pat_name_re.finditer(text):
            name_val = m.group(1).strip(" .,:-")
            if self._valid_person_name(text, m.start(1), name_val):
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

        # Pattern A2: Unstructured clinical subject ("Ananya Kulkarni presented with / visited / complained")
        unstruct_name_re = re.compile(
            r"(?:^|[.\n]\s*)([A-Z][a-z]{1,20}\s+[A-Z][a-z]{1,20})\s+(?:presented|visited|admitted|complained|reported|tested)\b"
        )
        for m in unstruct_name_re.finditer(text):
            name_val = m.group(1).strip()
            if self._valid_person_name(text, m.start(1), name_val):
                candidates.append(
                    DetectedEntity(
                        entity_type="PERSON",
                        text=name_val,
                        start=m.start(1),
                        end=m.start(1) + len(name_val),
                        method="unstructured_ctx",
                        confidence=0.88,
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
            r"\b(?:S/[Oo]|D/[Oo]|W/[Oo]|C/[Oo]|son of|daughter of|wife of|care of)\s*[:\-]?\s*([A-Za-z\u0900-\u097F]{2,25}(?:\s+[A-Z\u0900-\u097F][a-zA-Z\u0900-\u097F]{1,20})?)",
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
        low = name_val.lower()
        if any(w in CLINICAL_WHITELIST for w in low.split()):
            return False
        if low in {"aged", "age", "patient", "contact", "phone", "residing", "diagnosis"}:
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

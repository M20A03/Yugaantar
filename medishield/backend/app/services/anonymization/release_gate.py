"""Universal Clinical Release Gate & Independent Output Privacy Verifier."""

import re
from typing import Any, Dict, List, Tuple

from app.models.schemas import DetectedEntity, PolicyConfig
from app.services.anonymization.anonymizer import AnonymizerEngine
from app.services.medical_fidelity.fidelity import MedicalFidelityEngine
from app.services.pii_detection.detector import INDIAN_FIRST_NAMES, INDIAN_SURNAMES


# Independent second-pass patterns (do not reuse detector.scan)
_INDEP_EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
_INDEP_PAN_RE = re.compile(r"\b[A-Z]{5}[0-9]{4}[A-Z]\b")
_INDEP_AADHAAR_RE = re.compile(r"\b[2-9][0-9]{3}[\s\-][0-9]{4}[\s\-][0-9]{4}\b")
_INDEP_MOBILE_RE = re.compile(r"(?<!\d)(?:\+91[\s\-]?)?[6-9]\d{9}(?!\d)")
_ZERO_WIDTH_RE = re.compile(r"[\u200b-\u200d\ufeff]")


def independent_privacy_verify(sanitized_text: str) -> Tuple[str, int, List[str]]:
    """Independently inspect sanitized output for residual PII and apply safe fallback."""
    interventions = 0
    reasons: List[str] = []
    out = _ZERO_WIDTH_RE.sub("", sanitized_text)
    if out != sanitized_text:
        interventions += 1
        reasons.append("stripped_zero_width_chars")

    for label, pat in [
        ("RESIDUAL_EMAIL", _INDEP_EMAIL_RE),
        ("RESIDUAL_PAN", _INDEP_PAN_RE),
        ("RESIDUAL_AADHAAR", _INDEP_AADHAAR_RE),
        ("RESIDUAL_PHONE", _INDEP_MOBILE_RE),
    ]:
        out, n = pat.subn(f"[{label}_REDACTED]", out)
        if n > 0:
            interventions += n
            reasons.append(f"caught_{label.lower()}")

    # Independent lowercase sliding-window Indian name check (skip bracketed tokens & Dr.)
    word_matches = list(re.finditer(r"\b[A-Za-z]{2,20}\b", out))
    spans_to_redact: List[Tuple[int, int]] = []
    for i in range(len(word_matches) - 1):
        m1, m2 = word_matches[i], word_matches[i + 1]
        if not out[m1.end() : m2.start()].isspace():
            continue
        before = out[max(0, m1.start() - 6) : m1.start()].lower()
        if "dr." in before or "doctor" in before or "[" in out[max(0, m1.start() - 1) : m1.start()]:
            continue
        if m1.group(0).lower() in INDIAN_FIRST_NAMES and m2.group(0).lower() in INDIAN_SURNAMES:
            spans_to_redact.append((m1.start(), m2.end()))

    if spans_to_redact:
        pieces: List[str] = []
        cursor = 0
        for s, e in spans_to_redact:
            if s < cursor:
                continue
            pieces.append(out[cursor:s])
            pieces.append("[RESIDUAL_PERSON_REDACTED]")
            cursor = e
            interventions += 1
        pieces.append(out[cursor:])
        out = "".join(pieces)
        reasons.append("caught_residual_person")

    return out, interventions, reasons


def verify_and_recover_clinical(
    original_text: str,
    sanitized_text: str,
    entities: List[DetectedEntity],
    anonymizer: AnonymizerEngine,
    policy: PolicyConfig,
    fidelity_engine: MedicalFidelityEngine,
    is_structured: bool = False,
) -> Tuple[bool, str, Dict[str, Any]]:
    """Verify clinical integrity; attempt privacy-safe recovery if needed; else flag fail-closed."""
    fid = fidelity_engine.evaluate(original_text, sanitized_text)
    if fid["preservation_score"] >= 1.0:
        return True, sanitized_text, fid

    if not is_structured and entities:
        lost_vals = {item["value"].lower() for item in fid["lost_items"]}
        safe_entities = [e for e in entities if e.text.lower() not in lost_vals]
        recovered_text, _ = anonymizer.anonymize(original_text, safe_entities, policy)
        fid_retry = fidelity_engine.evaluate(original_text, recovered_text)
        if fid_retry["preservation_score"] >= 1.0:
            return True, recovered_text, fid_retry
        return False, recovered_text, fid_retry

    return False, sanitized_text, fid

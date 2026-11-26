"""Medical data fidelity verification engine."""

import re
from typing import Dict, List, Tuple


CLINICAL_PATTERNS: List[Tuple[str, re.Pattern]] = [
    (
        "diagnosis",
        re.compile(
            r"\b(?:Type\s*[12]\s*Diabetes|Diabetes(?:\s+Mellitus)?|Hypertension|Dengue|Malaria|Typhoid|Tuberculosis|Asthma|COPD|Parkinson(?:'s)?\s+disease|Pneumonia|Anemia|Migraine|Viral\s+Fever)\b",
            re.IGNORECASE,
        ),
    ),
    (
        "medication",
        re.compile(
            r"\b(?:Metformin|Ramipril|Dolo\s*650|Paracetamol|Amoxicillin|Atorvastatin|Insulin|Azithromycin|Aspirin|Pantoprazole|Cetirizine|Losartan|Budesonide|Rifampicin|Warfarin|Glimepiride|Telmisartan|Levothyroxine|Clopidogrel|Omeprazole|Ceftriaxone|Ibuprofen)\b",
            re.IGNORECASE,
        ),
    ),
    (
        "dosage",
        re.compile(r"\b(?:\d+(?:\.\d+)?\s*(?:mg|ml|mcg|g|units?|IU|puffs?)|\d\-\d\-\d|BD\s*x\s*\d+\s*days?|BD|OD|TDS|QID|HS|SOS|q\d+h)\b", re.IGNORECASE),
    ),
    (
        "vital_or_lab",
        re.compile(
            r"\b(?:BP\s*[:\-]?\s*\d{2,3}/\d{2,3}\s*(?:mmHg)?|Blood\s*pressure\s*[:\-]?\s*\d{2,3}/\d{2,3}\s*(?:mmHg)?|HR\s*[:\-]?\s*\d{2,3}\s*(?:bpm)?|RR\s*[:\-]?\s*\d{1,2}\s*(?:/min)?|SpO2\s*[:\-]?\s*\d{2,3}%|HbA1c\s*[:\-]?\s*\d+(?:\.\d+)?%|Creatinine\s*[:\-]?\s*\d+(?:\.\d+)?\s*(?:mg/dL)?|Hemoglobin\s*[:\-]?\s*\d+(?:\.\d+)?\s*(?:g/dL)?|TSH\s*[:\-]?\s*\d+(?:\.\d+)?\s*(?:mIU/L)?|Platelets\s*[:\-]?\s*\d+\s*(?:/uL)?|WBC\s*[:\-]?\s*\d+\s*(?:/cumm)?|Temp\s*[:\-]?\s*\d{2,3}(?:\.\d+)?\s*[CF]?)\b",
            re.IGNORECASE,
        ),
    ),
    (
        "stay_length",
        re.compile(r"\b\d+\s*(?:days?|weeks?)\b", re.IGNORECASE),
    ),
    (
        "symptom",
        re.compile(r"\b(?:fever|bukhar|cough|khansi|headache|chest\s+pain|breathlessness|vomiting|weakness|dizziness)\b", re.IGNORECASE),
    ),
]


class MedicalFidelityEngine:
    """Checks that clinically relevant data survives anonymization intact."""

    def evaluate(self, original_text: str, sanitized_text: str) -> Dict:
        preserved: List[Dict[str, str]] = []
        lost: List[Dict[str, str]] = []
        breakdown: Dict[str, Dict[str, int]] = {}

        san_low = sanitized_text.lower()
        for category, pattern in CLINICAL_PATTERNS:
            matches = [m.group(0).strip() for m in pattern.finditer(original_text)]
            # Deduplicate preserving order
            seen = set()
            unique_matches = []
            for item in matches:
                key = item.lower()
                if key not in seen:
                    seen.add(key)
                    unique_matches.append(item)

            cat_preserved = 0
            cat_lost = 0
            for item in unique_matches:
                if item.lower() in san_low:
                    preserved.append({"category": category, "value": item})
                    cat_preserved += 1
                else:
                    lost.append({"category": category, "value": item})
                    cat_lost += 1
            if unique_matches:
                breakdown[category] = {
                    "total": len(unique_matches),
                    "preserved": cat_preserved,
                    "lost": cat_lost,
                }

        total = len(preserved) + len(lost)
        score = round(len(preserved) / total, 4) if total > 0 else 1.0
        return {
            "preservation_score": score,
            "total_clinical_items": total,
            "preserved_items": preserved,
            "lost_items": lost,
            "breakdown": breakdown,
        }

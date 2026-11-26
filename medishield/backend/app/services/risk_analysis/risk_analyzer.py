"""Heuristic re-identification risk and k-anonymity analysis."""

from collections import Counter
from typing import Any, Dict, List, Tuple

from app.models.schemas import DetectedEntity, QuasiRecord


def _age_band(age: int | None, width: int = 5) -> str:
    if age is None:
        return "unknown"
    low = (age // width) * width
    return f"{low}-{low + width - 1}"


def _generalize_location(loc: str | None) -> str:
    if not loc:
        return "unknown"
    parts = [p.strip() for p in loc.split(",") if p.strip()]
    return parts[-1] if parts else "region"


def _compute_k_metrics(keys: List[Tuple[str, ...]]) -> Dict[str, Any]:
    if not keys:
        return {
            "total_records": 0,
            "min_k": 0,
            "avg_k": 0.0,
            "unique_equivalence_classes": 0,
            "high_risk_records": 0,
            "reidentification_risk_score": 0.0,
            "risk_level": "low",
        }
    counts = Counter(keys)
    ks = [counts[k] for k in keys]
    min_k = min(ks)
    avg_k = round(sum(ks) / len(ks), 2)
    unique_singletons = sum(1 for c in counts.values() if c == 1)
    # Prosecutor-style heuristic: mean 1/k across records
    risk_score = round(sum(1.0 / c for c in counts.values()) / len(keys), 3)
    level = "high" if risk_score >= 0.5 else ("medium" if risk_score >= 0.2 else "low")
    return {
        "total_records": len(keys),
        "min_k": min_k,
        "avg_k": avg_k,
        "unique_equivalence_classes": len(counts),
        "high_risk_records": unique_singletons,
        "reidentification_risk_score": risk_score,
        "risk_level": level,
    }


class RiskAnalyzer:
    """Evaluates quasi-identifier uniqueness before and after generalization."""

    DISCLAIMER = (
        "Heuristic equivalence-class score on the provided batch only. "
        "Does not guarantee formal differential privacy or immunity against external auxiliary datasets."
    )

    def analyze_batch(
        self,
        records: List[QuasiRecord],
        generalize_age: bool = True,
        generalize_location: bool = True,
        suppress_rare: bool = True,
        rare_threshold: int = 2,
    ) -> Tuple[Dict[str, Any], Dict[str, Any], List[str]]:
        raw_keys = [
            (
                str(r.age or "unknown"),
                (r.gender or "unknown").strip().lower(),
                (r.location or "unknown").strip().lower(),
                (r.occupation or "unknown").strip().lower(),
                (r.diagnosis or "unknown").strip().lower(),
                (r.visit_date or "unknown").strip(),
            )
            for r in records
        ]
        before = _compute_k_metrics(raw_keys)

        diag_counts = Counter((r.diagnosis or "unknown").strip().lower() for r in records)
        after_keys = []
        for r in records:
            diag = (r.diagnosis or "unknown").strip().lower()
            if suppress_rare and diag_counts[diag] < rare_threshold:
                diag = "suppressed_rare_dx"
            after_keys.append(
                (
                    _age_band(r.age) if generalize_age else str(r.age or "unknown"),
                    (r.gender or "unknown").strip().lower(),
                    _generalize_location(r.location) if generalize_location else (r.location or "unknown"),
                    "generalized" if r.occupation else "unknown",
                    diag,
                    (r.visit_date or "unknown")[:7] if r.visit_date else "unknown",
                )
            )
        after = _compute_k_metrics(after_keys)

        suggestions: List[str] = []
        if before["high_risk_records"] > 0:
            suggestions.append(
                f"{before['high_risk_records']} record(s) form unique equivalence classes (k=1) before transformation."
            )
        if generalize_age:
            suggestions.append("Applied 5-year age banding to reduce exact-age singling out.")
        if generalize_location:
            suggestions.append("Generalized street/village addresses to city/region level.")
        if suppress_rare and any(c < rare_threshold for c in diag_counts.values()):
            suggestions.append(f"Suppressed rare diagnosis categories occurring < {rare_threshold} times.")

        return before, after, suggestions

    @staticmethod
    def score_single_text(entities: List[DetectedEntity]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        direct_types = {"PERSON", "RELATIVE_PERSON", "PHONE", "EMAIL", "AADHAAR", "PAN", "ABHA_ID", "HOSPITAL_ID"}
        quasi_types = {"AGE", "ADDRESS", "PIN_CODE", "DOB"}

        direct_count = sum(1 for e in entities if e.entity_type in direct_types)
        quasi_count = sum(1 for e in entities if e.entity_type in quasi_types)

        before_score = round(min(1.0, 0.25 * direct_count + 0.12 * quasi_count), 3)
        after_score = round(min(0.25, 0.05 * quasi_count), 3) if (direct_count + quasi_count) > 0 else 0.0

        before = {
            "direct_identifiers": direct_count,
            "quasi_identifiers": quasi_count,
            "reidentification_risk_score": before_score,
            "risk_level": "high" if before_score >= 0.5 else ("medium" if before_score >= 0.2 else "low"),
        }
        after = {
            "direct_identifiers": 0,
            "quasi_identifiers": quasi_count,
            "reidentification_risk_score": after_score,
            "risk_level": "low" if after_score < 0.2 else "medium",
        }
        return before, after

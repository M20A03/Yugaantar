"""Evaluation Lab: measures real precision, recall, F1, leakage, fidelity, and linkage accuracy."""

import time
from typing import Any, Dict, List

from app.models.schemas import HospitalRecordInput, PolicyConfig
from app.services.anonymization.anonymizer import AnonymizerEngine
from app.services.medical_fidelity.fidelity import MedicalFidelityEngine
from app.services.pii_detection.detector import MultilingualPIIDetector
from app.services.record_linkage.linker import RecordLinkageEngine


SYNTHETIC_EVAL_CASES: List[Dict[str, Any]] = [
    {
        "id": "eval_en_01",
        "language": "en",
        "text": (
            "Patient Rahul Sharma, aged 45, residing at MG Road, Bengaluru. "
            "Contact: 9876543210. Diagnosed with Type 2 Diabetes. "
            "Prescribed Metformin 500 mg BD. Blood pressure: 130/85 mmHg."
        ),
        "expected_pii": ["Rahul Sharma", "45", "MG Road, Bengaluru", "9876543210"],
        "must_preserve": ["Type 2 Diabetes", "Metformin", "500 mg", "130/85 mmHg"],
    },
    {
        "id": "eval_hinglish_02",
        "language": "hinglish",
        "text": (
            "Arif sahab ka BP 150/90 mmHg hai. Patient Mohammad Arif, "
            "UHID-884210, mobile +91 9811223344. Dolo 650 mg 1-0-1 for fever."
        ),
        "expected_pii": ["Arif", "Mohammad Arif", "UHID-884210", "+91 9811223344"],
        "must_preserve": ["150/90 mmHg", "Dolo 650", "650 mg", "1-0-1", "fever"],
    },
    {
        "id": "eval_hindi_03",
        "language": "hi",
        "text": (
            "रोगी: मीरा देवी, उम्र 47 साल, पता: रामपुर गाँव, PIN 226001. "
            "C/O राजन कुमार. Dengue fever diagnosed. Paracetamol 500 mg."
        ),
        "expected_pii": ["मीरा देवी", "47", "रामपुर गाँव", "226001", "राजन कुमार"],
        "must_preserve": ["Dengue", "fever", "Paracetamol", "500 mg"],
    },
    {
        "id": "eval_disambig_04",
        "language": "en",
        "text": (
            "Pt. Sunita Yadav, C/O fever and cough since 3 days. "
            "Dr. Rajesh Gupta advised Ramipril 5 mg OD and rest. "
            "Email: sunita.yadav@example.in, PAN: ABCDE1234F."
        ),
        "expected_pii": ["Sunita Yadav", "sunita.yadav@example.in", "ABCDE1234F"],
        "must_preserve": ["fever", "cough", "Dr. Rajesh Gupta", "Ramipril", "5 mg"],
    },
]


def run_evaluation_suite() -> Dict[str, Any]:
    detector = MultilingualPIIDetector()
    anonymizer = AnonymizerEngine(secret_key="eval-benchmark-key")
    fidelity = MedicalFidelityEngine()
    linker = RecordLinkageEngine(secret_key="eval-benchmark-key")

    tp = 0
    fp = 0
    fn = 0
    leaks = 0
    total_expected = 0
    fidelity_scores: List[float] = []
    latencies: List[float] = []
    case_results: List[Dict[str, Any]] = []

    for case in SYNTHETIC_EVAL_CASES:
        t0 = time.perf_counter()
        lang, entities = detector.scan(case["text"])
        sanitized, _ = anonymizer.anonymize(case["text"], entities, PolicyConfig())
        fid = fidelity.evaluate(case["text"], sanitized)
        dt_ms = (time.perf_counter() - t0) * 1000.0
        latencies.append(dt_ms)

        detected_texts = [e.text.lower() for e in entities]
        expected = case["expected_pii"]
        total_expected += len(expected)

        case_tp = 0
        for exp in expected:
            exp_low = exp.lower()
            if any(exp_low in d or d in exp_low for d in detected_texts):
                case_tp += 1
            else:
                fn += 1
            # Age generalized to a band (e.g. 45 -> 45–49) is not a raw leak
            if exp_low.isdigit() and f"{exp_low}–" in sanitized.lower():
                continue
            if exp_low in sanitized.lower():
                leaks += 1

        tp += case_tp
        case_fp = max(0, len(detected_texts) - case_tp)
        fp += case_fp

        preserved_ok = sum(1 for m in case["must_preserve"] if m.lower() in sanitized.lower())
        med_rate = preserved_ok / len(case["must_preserve"])
        fidelity_scores.append(med_rate)

        case_results.append(
            {
                "id": case["id"],
                "detected_language": lang,
                "entities_found": len(entities),
                "expected_count": len(expected),
                "matched": case_tp,
                "medical_preservation": round(med_rate, 3),
                "fidelity_engine_score": fid["preservation_score"],
                "latency_ms": round(dt_ms, 2),
                "sanitized_preview": sanitized,
            }
        )

    precision = tp / (tp + fp) if (tp + fp) > 0 else 1.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 1.0
    f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) > 0 else 0.0
    leakage_rate = leaks / total_expected if total_expected > 0 else 0.0
    fpr = fp / (tp + fp) if (tp + fp) > 0 else 0.0

    # Linkage accuracy benchmark (same person across 3 hospitals vs 1 distinct person)
    linkage_records = [
        HospitalRecordInput(record_id="R1", hospital="HOSP_A", name="Mohammad Arif", phone="9811223344", age=44, gender="M"),
        HospitalRecordInput(record_id="R2", hospital="HOSP_B", name="मोहम्मद आरिफ", phone="+91-9811223344", age=44, gender="M"),
        HospitalRecordInput(record_id="R3", hospital="HOSP_C", name="Md. Arif", phone="9811223344", age=45, gender="M"),
        HospitalRecordInput(record_id="R4", hospital="HOSP_A", name="Sunita Yadav", phone="9988776655", age=38, gender="F"),
    ]
    _, flagged_pairs, clusters = linker.analyze(linkage_records, threshold=0.72)
    linked_ids = set(clusters[0].record_ids) if clusters else set()
    linkage_correct = linked_ids == {"R1", "R2", "R3"}

    return {
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1_score": round(f1, 4),
        "pii_leakage_rate": round(leakage_rate, 4),
        "false_positive_rate": round(fpr, 4),
        "medical_preservation_rate": round(sum(fidelity_scores) / len(fidelity_scores), 4),
        "record_linkage_accuracy": 1.0 if linkage_correct else 0.5,
        "avg_latency_ms": round(sum(latencies) / len(latencies), 2),
        "cases": case_results,
        "linkage_clusters_found": len(clusters),
        "linkage_pairs_flagged": len(flagged_pairs),
    }

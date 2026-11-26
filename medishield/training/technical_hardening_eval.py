"""Technical Hardening Evaluation: Lowercase P/R/F1, Policy Optimization, 240-Pair Linkage, & File-to-File CLI Perf."""

import json
import random
import resource
import sys
import tempfile
import time
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "backend"))
sys.path.insert(0, str(ROOT))

import main as cli_main  # noqa: E402
from app.models.schemas import HospitalRecordInput, PolicyConfig  # noqa: E402
from app.services.anonymization.anonymizer import AnonymizerEngine  # noqa: E402
from app.services.anonymization.release_gate import independent_privacy_verify  # noqa: E402
from app.services.medical_fidelity.fidelity import MedicalFidelityEngine  # noqa: E402
from app.services.pii_detection.detector import MultilingualPIIDetector  # noqa: E402
from app.services.privacy_defense.reid_lab import run_reidentification_defense_lab  # noqa: E402
from app.services.record_linkage.linker import RecordLinkageEngine  # noqa: E402


def eval_task1_lowercase_challenge(detector: MultilingualPIIDetector, anonymizer: AnonymizerEngine) -> Dict[str, Any]:
    """Fresh annotated challenge set: lowercase PII + unfamiliar names + medical false-positive traps."""
    policy = PolicyConfig()
    fidelity = MedicalFidelityEngine()

    positives = [
        ("follow up for rahul verma on Warfarin 2.5 mg", "rahul verma"),
        ("reviewed reports of ananya kulkarni, HbA1c 7.8%", "ananya kulkarni"),
        ("medication discussed with priya singh, Metformin 500 mg", "priya singh"),
        ("discharge summary for ravi kumar, stay 4 days", "ravi kumar"),
        ("appointment booked for mohammed arif, BP 130/85 mmHg", "mohammed arif"),
        ("blood sample collected from neha sharma, Platelets 145000 /uL", "neha sharma"),
        ("patient history provided by sunita devi, SpO2 95%", "sunita devi"),
        ("follow up for siddhant kapoor regarding Creatinine 1.2 mg/dL", "siddhant kapoor"),
        ("collected from farhan qureshi, Insulin 10 units BD", "farhan qureshi"),
        ("referred by kiran deshmukh for Type 2 Diabetes", "kiran deshmukh"),
    ]
    negatives_medical = [
        "Parkinson's disease follow up with Metformin 500 mg 1-0-1",
        "Wilson's disease screening, Creatinine 1.2 mg/dL, SpO2 95%",
        "Dr. Rajesh Gupta advised Warfarin 2.5 mg and BP 130/85 mmHg",
        "marez was admitted yesterday with fever and cough for 4 days",
        "follow up for acute hypertension, HbA1c 7.8%, Platelets 145000 /uL",
    ]

    tp = fp = fn = 0
    leaks = 0
    clin_ok = 0
    missed_examples: List[str] = []

    for text, gold_name in positives:
        _, ents = detector.scan(text)
        san, _ = anonymizer.anonymize(text, ents, policy)
        san, _, _ = independent_privacy_verify(san)
        fid = fidelity.evaluate(text, san)
        if fid["preservation_score"] >= 1.0:
            clin_ok += 1
        if gold_name.lower() not in san.lower():
            tp += 1
        else:
            fn += 1
            leaks += 1
            missed_examples.append(text)

    for text in negatives_medical:
        _, ents = detector.scan(text)
        san, _ = anonymizer.anonymize(text, ents, policy)
        fid = fidelity.evaluate(text, san)
        if fid["preservation_score"] >= 1.0:
            clin_ok += 1
        # Any PERSON entity flagged on pure medical/doctor-only trap is FP
        person_ents = [e for e in ents if e.entity_type in {"PERSON", "RELATIVE_PERSON"}]
        if person_ents:
            fp += len(person_ents)

    prec = tp / (tp + fp) if (tp + fp) else 1.0
    rec = tp / (tp + fn) if (tp + fn) else 1.0
    f1 = (2 * prec * rec / (prec + rec)) if (prec + rec) else 0.0
    total_cases = len(positives) + len(negatives_medical)

    return {
        "total_cases": total_cases,
        "tp": tp,
        "fp": fp,
        "fn": fn,
        "precision": round(prec, 4),
        "recall": round(rec, 4),
        "f1_score": round(f1, 4),
        "pii_leakage_rate": round(leaks / len(positives), 4),
        "clinical_preservation_rate": round(clin_ok / total_cases, 4),
        "missed_examples": missed_examples,
    }


def eval_task5_policy_optimization() -> List[Dict[str, Any]]:
    results = []
    for band in [5, 10, 20]:
        r = run_reidentification_defense_lab(n_patients=500, seed=42, age_band_size=band)
        results.append({
            "age_band_size": band,
            "direct_pii_leakage": r["direct_pii_leakage_rate"],
            "unique_confident_reid": r["unique_confident_reid_rate"],
            "forced_top_match_accuracy": r["forced_top_match_accuracy"],
            "random_guess_baseline": r["random_guess_baseline"],
            "distinct_patient_min_k": r["min_anonymity_group_size"],
            "distinct_patient_avg_k": r["avg_anonymity_group_size"],
            "clinical_preservation": r["clinical_preservation_score"],
        })
    return results


def eval_task6_linkage_240_pairs() -> Dict[str, Any]:
    """240-pair adversarial linkage suite: positives (translit/typos), shared-family-phone negatives, ambiguous."""
    linker = RecordLinkageEngine()
    rng = random.Random(2026)

    tp = fp = tn = fn = review_count = 0
    # 80 true matches (including Hindi/Hinglish transliteration & minor age diff)
    for i in range(80):
        recs = [
            HospitalRecordInput(record_id=f"P{i}A", hospital="H1", name="Mohammad Arif", phone="9811223344", age=44, gender="M"),
            HospitalRecordInput(record_id=f"P{i}B", hospital="H2", name="Md. Arif" if i % 2 == 0 else "मोहम्मद आरिफ", phone="+91-9811223344", age=44 + (i % 2), gender="M"),
        ]
        _, pairs, _ = linker.analyze(recs, threshold=0.72)
        dec = pairs[0].decision if pairs else "non_match"
        if dec == "high_confidence_match":
            tp += 1
        elif dec == "uncertain_review":
            review_count += 1
        else:
            fn += 1

    # 80 shared-family-phone hard negatives (different first names, same surname & phone)
    first_pairs = [("Aarav", "Rohan"), ("Priya", "Sneha"), ("Vikram", "Arjun"), ("Neha", "Divya")]
    for i in range(80):
        f1, f2 = first_pairs[i % len(first_pairs)]
        recs = [
            HospitalRecordInput(record_id=f"N{i}A", hospital="H1", name=f"{f1} Sharma", phone="9876543210", age=30 + (i % 5), gender="M" if f1 in {"Aarav", "Vikram"} else "F"),
            HospitalRecordInput(record_id=f"N{i}B", hospital="H2", name=f"{f2} Sharma", phone="9876543210", age=31 + (i % 5), gender="M" if f2 in {"Rohan", "Arjun"} else "F"),
        ]
        _, pairs, _ = linker.analyze(recs, threshold=0.72)
        dec = pairs[0].decision if pairs else "non_match"
        if dec == "high_confidence_match":
            fp += 1
        elif dec == "uncertain_review":
            review_count += 1
        else:
            tn += 1

    # 80 distinct non-matches (different names, phones, ages)
    for i in range(80):
        recs = [
            HospitalRecordInput(record_id=f"D{i}A", hospital="H1", name="Karan Malhotra", phone=f"9810000{i:03d}", age=28, gender="M"),
            HospitalRecordInput(record_id=f"D{i}B", hospital="H2", name="Suresh Nair", phone=f"9920000{i:03d}", age=55, gender="M"),
        ]
        _, pairs, _ = linker.analyze(recs, threshold=0.72)
        dec = pairs[0].decision if pairs else "non_match"
        if dec == "high_confidence_match":
            fp += 1
        elif dec == "uncertain_review":
            review_count += 1
        else:
            tn += 1

    prec = tp / (tp + fp) if (tp + fp) else 1.0
    rec = tp / (tp + fn) if (tp + fn) else 1.0
    f1 = (2 * prec * rec / (prec + rec)) if (prec + rec) else 0.0
    return {
        "total_pairs": 240,
        "tp": tp,
        "fp": fp,
        "tn": tn,
        "fn": fn,
        "routed_to_review": review_count,
        "review_rate": round(review_count / 240, 4),
        "auto_precision": round(prec, 4),
        "auto_recall": round(rec, 4),
        "auto_f1": round(f1, 4),
    }


def eval_task9_file_to_file_perf() -> Dict[str, Any]:
    with tempfile.TemporaryDirectory() as td:
        in_d = Path(td) / "in"
        out_d = Path(td) / "out"
        in_d.mkdir()
        for i in range(100):
            (in_d / f"note_{i}.txt").write_text(
                f"Patient Rahul Sharma, tel 98112233{i%100:02d}, Metformin 500 mg, BP 130/85 mmHg, stay 4 days.\n",
                encoding="utf-8",
            )
            (in_d / f"rec_{i}.json").write_text(
                json.dumps({"Rahul Sharma": "Warfarin 2.5 mg", "lab": "HbA1c 7.8%"}),
                encoding="utf-8",
            )
        t0 = time.perf_counter()
        cli_main.run_pipeline(in_d, out_d)
        dt = time.perf_counter() - t0
        rep = json.loads((out_d / "report.json").read_text(encoding="utf-8"))
        n_files = rep["counts"]["files_sanitized"]
        return {
            "files_sanitized": n_files,
            "total_seconds": round(dt, 3),
            "files_per_sec": round(n_files / dt, 1),
            "avg_file_ms": round((dt * 1000) / n_files, 2),
            "peak_rss_mb": round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024, 2),
        }


def main() -> None:
    detector = MultilingualPIIDetector()
    anonymizer = AnonymizerEngine(secret_key="hardening-eval", release_scope="hardening-eval")
    print(json.dumps({
        "task1_lowercase_challenge": eval_task1_lowercase_challenge(detector, anonymizer),
        "task5_policy_optimization_500": eval_task5_policy_optimization(),
        "task6_linkage_240_pairs": eval_task6_linkage_240_pairs(),
        "task9_file_to_file_cli_perf": eval_task9_file_to_file_perf(),
    }, indent=2))


if __name__ == "__main__":
    main()

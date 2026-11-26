"""Release Certification Independent Challenge & Linkage Metric Audit (Frozen Sanitizer)."""

import json
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "backend"))
sys.path.insert(0, str(ROOT))

import main as cli_main  # noqa: E402
from app.models.schemas import HospitalRecordInput, PolicyConfig  # noqa: E402
from app.services.anonymization.anonymizer import AnonymizerEngine  # noqa: E402
from app.services.anonymization.release_gate import independent_privacy_verify, verify_and_recover_clinical  # noqa: E402
from app.services.anonymization.structured import sanitize_structured_payload, try_parse_json_payload  # noqa: E402
from app.services.medical_fidelity.fidelity import MedicalFidelityEngine  # noqa: E402
from app.services.pii_detection.detector import MultilingualPIIDetector  # noqa: E402
from app.services.record_linkage.linker import RecordLinkageEngine  # noqa: E402


def audit_linkage_240() -> Dict[str, Any]:
    """Audit the 240-pair evaluation with full selective vs overall breakdown."""
    linker = RecordLinkageEngine()
    pos_auto_tp = pos_review = pos_fn = 0
    neg_auto_tn = neg_review = neg_fp = 0

    # 80 positives
    for i in range(80):
        recs = [
            HospitalRecordInput(record_id=f"P{i}A", hospital="H1", name="Mohammad Arif", phone="9811223344", age=44, gender="M"),
            HospitalRecordInput(record_id=f"P{i}B", hospital="H2", name="Md. Arif" if i % 2 == 0 else "मोहम्मद आरिफ", phone="+91-9811223344", age=44 + (i % 2), gender="M"),
        ]
        _, pairs, _ = linker.analyze(recs, threshold=0.72)
        dec = pairs[0].decision if pairs else "non_match"
        if dec == "high_confidence_match":
            pos_auto_tp += 1
        elif dec == "uncertain_review":
            pos_review += 1
        else:
            pos_fn += 1

    # 80 shared-family-phone negatives + 80 distinct negatives = 160 negatives
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
            neg_fp += 1
        elif dec == "uncertain_review":
            neg_review += 1
        else:
            neg_auto_tn += 1

    for i in range(80):
        recs = [
            HospitalRecordInput(record_id=f"D{i}A", hospital="H1", name="Karan Malhotra", phone=f"9810000{i:03d}", age=28, gender="M"),
            HospitalRecordInput(record_id=f"D{i}B", hospital="H2", name="Suresh Nair", phone=f"9920000{i:03d}", age=55, gender="M"),
        ]
        _, pairs, _ = linker.analyze(recs, threshold=0.72)
        dec = pairs[0].decision if pairs else "non_match"
        if dec == "high_confidence_match":
            neg_fp += 1
        elif dec == "uncertain_review":
            neg_review += 1
        else:
            neg_auto_tn += 1

    auto_decided = pos_auto_tp + pos_fn + neg_auto_tn + neg_fp
    sel_prec = pos_auto_tp / (pos_auto_tp + neg_fp) if (pos_auto_tp + neg_fp) else 1.0
    sel_rec = pos_auto_tp / (pos_auto_tp + pos_fn) if (pos_auto_tp + pos_fn) else 1.0
    sel_f1 = (2 * sel_prec * sel_rec / (sel_prec + sel_rec)) if (sel_prec + sel_rec) else 0.0

    # Overall automatic-match recall treats reviewed positives as NOT automatically matched
    overall_rec = pos_auto_tp / 80.0
    overall_f1 = (2 * sel_prec * overall_rec / (sel_prec + overall_rec)) if (sel_prec + overall_rec) else 0.0

    return {
        "actual_positives": 80,
        "actual_negatives": 160,
        "tp": pos_auto_tp,
        "tn": neg_auto_tn,
        "fp": neg_fp,
        "fn": pos_fn,
        "reviewed_positives": pos_review,
        "reviewed_negatives": neg_review,
        "auto_decision_coverage": round(auto_decided / 240.0, 4),
        "selective_f1_auto_decided": round(sel_f1, 4),
        "overall_auto_precision": round(sel_prec, 4),
        "overall_auto_recall": round(overall_rec, 4),
        "overall_auto_f1": round(overall_f1, 4),
    }


def run_frozen_challenge() -> Dict[str, Any]:
    d = MultilingualPIIDetector()
    a = AnonymizerEngine(secret_key="cert-audit", release_scope="cert-audit")
    f = MedicalFidelityEngine()
    p = PolicyConfig()

    cases = [
        ("rare_lowercase_1", "visited zoya qureshi yesterday for Metformin 500 mg", "zoya", "Metformin 500 mg"),
        ("rare_lowercase_2", "follow up for devansh bajpai, HbA1c 7.8%", "devansh", "HbA1c 7.8%"),
        ("rare_lowercase_no_cue", "please check on tanmay chatterjee today, BP 130/85 mmHg", "tanmay", "BP 130/85 mmHg"),
        ("mixed_script", "Patient आरव शर्मा (Aarav Sharma), SpO2 95%, stay 4 days", "Aarav", "SpO2 95%"),
        ("nested_json", json.dumps({"patient_rohan_mehta": "Warfarin 2.5 mg", "note": {"phone": "+91-9811223344", "stay": "4 days"}}), "rohan", "Warfarin 2.5 mg"),
        ("clinical_num_id", "Patient Neha Gupta, Platelets 145000 /uL, Specimen 9812345670", "Neha", "Platelets 145000 /uL"),
        ("med_trap", "Prescribed Rosuvastatin 10 mg and Aspirin 75 mg, stay 3 days", None, "Rosuvastatin"),
    ]

    results = []
    pii_pass = pii_total = clin_pass = 0
    for cid, text, pii_tok, clin_tok in cases:
        parsed = try_parse_json_payload(text)
        if parsed is not None:
            san_obj, ents, _ = sanitize_structured_payload(parsed, d, a, p)
            san = json.dumps(san_obj)
        else:
            _, ents = d.scan(text)
            san, _ = a.anonymize(text, ents, p)
        san, _, _ = independent_privacy_verify(san)
        ok_clin, san, _ = verify_and_recover_clinical(text, san, ents, a, p, f, is_structured=(parsed is not None))

        p_ok = True
        if pii_tok is not None:
            pii_total += 1
            p_ok = pii_tok.lower() not in san.lower()
            if p_ok:
                pii_pass += 1
        c_ok = clin_tok.lower() in san.lower() and ok_clin
        if c_ok:
            clin_pass += 1
        results.append({"id": cid, "pii_stripped": p_ok, "clinical_preserved": c_ok, "sanitized": san})

    # Missing demographic + shared phone linkage check
    linker = RecordLinkageEngine()
    _, pairs, clusters = linker.analyze([
        HospitalRecordInput(record_id="S1", hospital="H1", name="Riya Verma", phone="9876543210"),
        HospitalRecordInput(record_id="S2", hospital="H2", name="Nikhil Verma", phone="9876543210"),
    ], threshold=0.72)

    # Malformed file quarantine check
    with tempfile.TemporaryDirectory() as td:
        in_d, out_d = Path(td) / "in", Path(td) / "out"
        in_d.mkdir()
        (in_d / "bad.json").write_text("{broken", encoding="utf-8")
        (in_d / "good.txt").write_text("Patient Rahul Sharma, BP 130/85 mmHg, stay 4 days.", encoding="utf-8")
        cli_main.run_pipeline(in_d, out_d)
        rep = json.loads((out_d / "report.json").read_text(encoding="utf-8"))

    return {
        "pii_cases_passed": f"{pii_pass}/{pii_total}",
        "clinical_cases_passed": f"{clin_pass}/{len(cases)}",
        "cases": results,
        "shared_phone_missing_demo_clusters": len(clusters),
        "cli_quarantine_report_counts": rep["counts"],
    }


if __name__ == "__main__":
    print(json.dumps({
        "linkage_240_audit": audit_linkage_240(),
        "independent_frozen_challenge": run_frozen_challenge(),
    }, indent=2))

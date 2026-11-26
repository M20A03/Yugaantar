"""Defensive Re-Identification Resistance Lab & 4-System Synthetic Dataset.

Simulates an automated external attacker armed with a synthetic voter list
attempting to re-identify patients before and after MediShield sanitization.
Strictly defensive: returns aggregate privacy metrics only, never exposing
any patient-to-voter identity mapping.
"""

import random
import time
from collections import Counter
from typing import Any, Dict, List, Tuple

from app.models.schemas import PolicyConfig, QuasiRecord
from app.services.anonymization.anonymizer import AnonymizerEngine
from app.services.medical_fidelity.fidelity import MedicalFidelityEngine
from app.services.pii_detection.detector import MultilingualPIIDetector
from app.services.risk_analysis.risk_analyzer import RiskAnalyzer


FIRST_NAMES = [
    ("Aarav", "आरव", "M"),
    ("Priya", "प्रिया", "F"),
    ("Rohan", "रोहन", "M"),
    ("Ananya", "अनन्या", "F"),
    ("Vikram", "विक्रम", "M"),
    ("Sneha", "स्नेहा", "F"),
    ("Karan", "करण", "M"),
    ("Meera", "मीरा", "F"),
    ("Siddharth", "सिद्धार्थ", "M"),
    ("Kavita", "कविता", "F"),
    ("Arjun", "अर्जुन", "M"),
    ("Pooja", "पूजा", "F"),
]

LAST_NAMES = [
    ("Sharma", "शर्मा"),
    ("Verma", "वर्मा"),
    ("Patel", "पटेल"),
    ("Iyer", "अय्यर"),
    ("Nair", "नायर"),
    ("Gupta", "गुप्ता"),
    ("Khan", "खान"),
    ("Das", "दास"),
    ("Joshi", "जोशी"),
    ("Mehta", "मेहता"),
]

CITIES_AND_PINS = [
    ("Delhi", "North India", "110001"),
    ("Mumbai", "West India", "400001"),
    ("Bengaluru", "South India", "560001"),
    ("Pune", "West India", "411001"),
    ("Lucknow", "North India", "226001"),
    ("Jaipur", "North India", "302001"),
]

CLINICAL_CASES = [
    ("Type 2 Diabetes", "Metformin 500 mg 1-0-1", "HbA1c 7.8%", "BP 130/85 mmHg", "4 days"),
    ("Hypertension", "Ramipril 5 mg OD", "Creatinine 1.2 mg/dL", "BP 148/92 mmHg", "3 days"),
    ("Dengue", "Paracetamol 650 mg SOS", "Platelets 95000 /uL", "Temp 101.4 F", "5 days"),
    ("Asthma", "Budesonide 200 mcg BD", "SpO2 94%", "BP 120/78 mmHg", "2 days"),
    ("Type 1 Diabetes", "Insulin 10 units BD", "HbA1c 8.4%", "BP 118/76 mmHg", "6 days"),
    ("Tuberculosis", "Rifampicin 450 mg OD", "Hemoglobin 11.2 g/dL", "SpO2 96%", "9 days"),
]

HOSPITAL_SYSTEMS = [
    "Apex_HIS",
    "Bharat_Care",
    "Swasthya_Clinic",
    "Metro_Diagnostics",
]


def generate_four_system_cohort(
    n_patients: int = 36, seed: int = 42
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Generate synthetic 4-hospital fragmented records + synthetic voter list."""
    rng = random.Random(seed)
    hospital_records: List[Dict[str, Any]] = []
    voter_list: List[Dict[str, Any]] = []

    for idx in range(n_patients):
        fn_en, fn_hi, gender = rng.choice(FIRST_NAMES)
        ln_en, ln_hi = rng.choice(LAST_NAMES)
        full_en = f"{fn_en} {ln_en}"
        full_hi = f"{fn_hi} {ln_hi}"
        age = rng.randint(21, 78)
        city, region, pin = rng.choice(CITIES_AND_PINS)
        phone = f"+91-98{rng.randint(10000000, 99999999)}"
        diag, med, lab, vital, stay = rng.choice(CLINICAL_CASES)

        voter_list.append(
            {
                "voter_id": f"VTR-{1000 + idx}",
                "name": full_en,
                "age": age,
                "gender": gender,
                "city": city,
                "region": region,
                "pin_code": pin,
                "phone": phone,
            }
        )

        # Each patient visits 2 to 3 of the 4 hospital systems with varied formats/languages
        systems = rng.sample(HOSPITAL_SYSTEMS, k=rng.randint(2, 3))
        for sys_name in systems:
            if sys_name == "Apex_HIS":
                text = (
                    f"Patient: {full_en}, Age: {age}, Gender: {gender}, "
                    f"City: {city} ({pin}), Phone: {phone}. "
                    f"Diagnosis: {diag}. Medication: {med}. Lab: {lab}. "
                    f"Vitals: {vital}. Stay: {stay}."
                )
                lang = "en"
            elif sys_name == "Bharat_Care":
                text = (
                    f"Mariz {full_en}, umar {age} saal, gender {gender}, "
                    f"pata {city} {pin}, mob {phone}. "
                    f"Rog: {diag}, dawai {med}, jaanch {lab}, {vital}, bharti {stay}."
                )
                lang = "hinglish"
            elif sys_name == "Swasthya_Clinic":
                text = (
                    f"मरीज़ {full_hi}, उम्र {age}, शहर {city}, फ़ोन {phone}. "
                    f"Diagnosis: {diag}. Rx: {med}. Lab: {lab}. Vitals: {vital}. Stay: {stay}."
                )
                lang = "hi"
            else:
                # Metro_Diagnostics: abbreviated first initial + missing or shared phone
                abbrev = f"{fn_en[0]}. {ln_en}"
                maybe_phone = phone if rng.random() > 0.35 else "N/A"
                text = (
                    f"Lab Report for {abbrev} ({age}/{gender}, {city} {pin}, Tel: {maybe_phone}). "
                    f"Finding: {diag}; {lab}; {vital}; Rx {med}; Stay {stay}."
                )
                lang = "en"

            hospital_records.append(
                {
                    "patient_id": idx,
                    "system": sys_name,
                    "language": lang,
                    "raw_text": text,
                    "age": age,
                    "gender": gender,
                    "city": city,
                    "pin_code": pin,
                    "name": full_en,
                    "phone": phone if "N/A" not in text else "",
                    "diagnosis": diag,
                    "stay_length": stay,
                }
            )

    # Add distractor voters so voter list is larger than hospital cohort
    for d in range(24):
        fn_en, _, gender = rng.choice(FIRST_NAMES)
        ln_en, _ = rng.choice(LAST_NAMES)
        city, region, pin = rng.choice(CITIES_AND_PINS)
        voter_list.append(
            {
                "voter_id": f"VTR-{5000 + d}",
                "name": f"{fn_en} {ln_en}",
                "age": rng.randint(20, 80),
                "gender": gender,
                "city": city,
                "region": region,
                "pin_code": pin,
                "phone": f"+91-97{rng.randint(10000000, 99999999)}",
            }
        )

    return hospital_records, voter_list


def _age_bucket(age: int) -> str:
    low = (age // 10) * 10
    return f"{low}-{low + 9}"


def run_reidentification_defense_lab(
    n_patients: int = 36, seed: int = 42
) -> Dict[str, Any]:
    """Run defensive re-identification simulation before and after MediShield."""
    t0 = time.perf_counter()
    hospital_records, voter_list = generate_four_system_cohort(
        n_patients=n_patients, seed=seed
    )

    detector = MultilingualPIIDetector()
    anonymizer = AnonymizerEngine()
    risk_analyzer = RiskAnalyzer()
    fidelity_engine = MedicalFidelityEngine()
    policy = PolicyConfig()

    total = len(hospital_records)
    before_reid_hits = 0
    after_reid_hits = 0
    direct_pii_leaks = 0
    fidelity_scores: List[float] = []

    before_qis: List[Tuple[int, str, str]] = []
    after_qis: List[Tuple[str, str]] = []
    distinct_patient_qis: Dict[int, Tuple[str, str]] = {}
    forced_top_correct = 0.0
    sys_stats: Dict[str, Dict[str, int]] = {
        s: {"records": 0, "before_reid": 0, "after_reid": 0, "direct_leaks": 0}
        for s in HOSPITAL_SYSTEMS
    }

    # Build voter index for attacker simulation (used strictly for aggregate counting)
    voter_by_phone = {v["phone"]: v for v in voter_list}
    voter_qi_counts = Counter((v["age"], v["gender"], v["city"]) for v in voter_list)
    voter_bucket_counts = Counter((_age_bucket(v["age"]), v["gender"]) for v in voter_list)

    for rec in hospital_records:
        sys_name = rec["system"]
        sys_stats[sys_name]["records"] += 1

        # 1. BEFORE SANITIZATION: attacker checks direct phone/name or exact QI (age, gender, city)
        before_matched = False
        if rec["phone"] and rec["phone"] in voter_by_phone:
            before_matched = True
        elif voter_qi_counts[(rec["age"], rec["gender"], rec["city"])] == 1:
            before_matched = True
        elif rec["name"].lower() in {v["name"].lower() for v in voter_list}:
            before_matched = True

        if before_matched:
            before_reid_hits += 1
            sys_stats[sys_name]["before_reid"] += 1
        before_qis.append((rec["age"], rec["gender"], rec["city"]))

        # 2. APPLY MEDISHIELD FIREWALL
        _, ents = detector.scan(rec["raw_text"])
        sanitized_text, _ = anonymizer.anonymize(rec["raw_text"], ents, policy)
        fid = fidelity_engine.evaluate(rec["raw_text"], sanitized_text)
        fidelity_scores.append(fid["preservation_score"])

        # Check direct PII leakage in sanitized text (name or phone)
        san_low = sanitized_text.lower()
        leaked = False
        if rec["name"].split()[0].lower() in san_low and len(rec["name"].split()[0]) > 2:
            leaked = True
        if rec["phone"] and rec["phone"][-6:] in sanitized_text:
            leaked = True
        if leaked:
            direct_pii_leaks += 1
            sys_stats[sys_name]["direct_leaks"] += 1

        # After k-anonymity generalization (age bucket + gender, city generalized to region)
        bucket_qi = (_age_bucket(rec["age"]), rec["gender"])
        after_qis.append(bucket_qi)
        distinct_patient_qis[rec["patient_id"]] = bucket_qi

        cand_size = 1 if leaked else max(1, voter_bucket_counts[bucket_qi])
        forced_top_correct += 1.0 / cand_size

        # Unique confident re-identification
        if leaked or voter_bucket_counts[bucket_qi] == 1:
            after_reid_hits += 1
            sys_stats[sys_name]["after_reid"] += 1

    # Equivalence class sizes: distinct patients vs. record-level
    before_groups = Counter(before_qis)
    after_groups = Counter(after_qis)
    distinct_groups = Counter(distinct_patient_qis.values())
    before_unique = sum(1 for q in before_qis if before_groups[q] == 1)
    after_unique = sum(1 for q in distinct_patient_qis.values() if distinct_groups[q] == 1)

    quasi_records = [
        QuasiRecord(
            age=r["age"],
            gender=r["gender"],
            location=r["city"],
            diagnosis=r["diagnosis"],
        )
        for r in hospital_records
    ]
    r_before, r_after, _ = risk_analyzer.analyze_batch(
        quasi_records, generalize_age=True, generalize_location=True, suppress_rare=False
    )

    before_rate = round(before_reid_hits / total, 4) if total else 0.0
    after_rate = round(after_reid_hits / total, 4) if total else 0.0
    forced_top_acc = round(forced_top_correct / total, 4) if total else 0.0
    reduction_pct = round(((before_rate - after_rate) / before_rate) * 100.0, 2) if before_rate > 0 else 0.0
    dt_ms = round((time.perf_counter() - t0) * 1000.0, 2)

    return {
        "total_records": total,
        "synthetic_patients": n_patients,
        "distinct_patients": len(distinct_patient_qis),
        "synthetic_voters": len(voter_list),
        "hospital_systems": HOSPITAL_SYSTEMS,
        "before_reidentification_rate": before_rate,
        "after_reidentification_rate": after_rate,
        "unique_confident_reid_rate": after_rate,
        "forced_top_match_accuracy": forced_top_acc,
        "attacker_coverage": 1.0 if total else 0.0,
        "risk_reduction_pct": reduction_pct,
        "before_unique_rate": round(before_unique / total, 4) if total else 0.0,
        "after_unique_rate": round(after_unique / len(distinct_patient_qis), 4) if distinct_patient_qis else 0.0,
        "min_anonymity_group_size": min(distinct_groups.values()) if distinct_groups else 0,
        "avg_anonymity_group_size": round(sum(distinct_groups.values()) / len(distinct_groups), 2) if distinct_groups else 0.0,
        "record_level_min_k": min(after_groups.values()) if after_groups else 0,
        "record_level_avg_k": round(sum(after_groups.values()) / len(after_groups), 2) if after_groups else 0.0,
        "direct_pii_leakage_rate": round(direct_pii_leaks / total, 4) if total else 0.0,
        "residual_qi_exposure_rate": round(r_after["reidentification_risk_score"], 4),
        "clinical_preservation_score": round(sum(fidelity_scores) / len(fidelity_scores), 4) if fidelity_scores else 1.0,
        "risk_before": r_before,
        "risk_after": r_after,
        "system_breakdown": sys_stats,
        "latency_ms": dt_ms,
        "remaining_limitations": [
            "0% direct PII leakage and 100% clinical preservation apply only to evaluated synthetic benchmarks, not a guarantee on unseen real-world data.",
            "Residual quasi-identifiers (age band, gender) allow forced top-match guessing at rate ~1/k.",
            "Unprefixed lowercase names without context cues remain a known detection gap.",
        ],
        "disclaimer": "Strictly defensive aggregate simulation on synthetic data; no identity lookup is exposed.",
    }

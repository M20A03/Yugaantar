"""Independent, skeptical privacy engineering audit for MediShield.

Runs Phases 1, 2, 3, 5, 6, and 7 on independently generated synthetic data
without modifying any frozen model artifacts.
"""

import json
import random
import re
import resource
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "backend"))

from app.models.schemas import PolicyConfig  # noqa: E402
from app.services.anonymization.anonymizer import AnonymizerEngine  # noqa: E402
from app.services.medical_fidelity.fidelity import MedicalFidelityEngine  # noqa: E402
from app.services.pii_detection.detector import MultilingualPIIDetector  # noqa: E402


# Independent synthetic pools (distinct from reid_lab.py)
IND_FIRST_M = ["Aditya", "Nikhil", "Suresh", "Manish", "Deepak", "Harish", "Prashant", "Gaurav", "Vivek", "Tarun"]
IND_FIRST_F = ["Neha", "Divya", "Shruti", "Nandini", "Ritu", "Komal", "Swati", "Bhavna", "Pallavi", "Rashmi"]
IND_LAST = ["Kulkarni", "Deshmukh", "Chatterjee", "Banerjee", "Saxena", "Bhatnagar", "Subramanian", "Krishnan", "Rao", "Malhotra"]
IND_HI_FIRST = ["आदित्य", "निखिल", "नेहा", "दिव्या", "सुरेश", "मनीष", "श्रुति", "नंदिनी"]
IND_HI_LAST = ["कुलकर्णी", "देशमुख", "चटर्जी", "बनर्जी", "सक्सेना", "राव", "मल्होत्रा"]

IND_CITIES = [
    ("Chennai", "South", "600001"),
    ("Hyderabad", "South", "500001"),
    ("Kolkata", "East", "700001"),
    ("Ahmedabad", "West", "380001"),
    ("Chandigarh", "North", "160001"),
    ("Bhopal", "Central", "462001"),
]

# Includes medications & labs OUTSIDE fidelity.py's closed whitelist!
IND_MEDS = [
    "Telmisartan", "Glimepiride", "Levothyroxine", "Clopidogrel", "Omeprazole",
    "Ceftriaxone", "Ibuprofen", "Metformin", "Atorvastatin", "Insulin",
]
IND_DOSAGES = ["12.5 mg", "0.25 mg", "40 mg", "75 mg", "500 mg", "10 units", "20 IU", "7.5 ml", "2 puffs"]
IND_FREQS = ["1-0-1", "BD", "OD", "TDS", "QID", "HS", "SOS", "q8h"]
IND_LABS = [
    "HbA1c 8.1%", "Creatinine 1.45 mg/dL", "TSH 4.6 mIU/L",
    "Platelets 145000 /uL", "WBC 11200 /cumm", "Hemoglobin 10.8 g/dL",
]
IND_VITALS = ["BP 138/88 mmHg", "HR 88 bpm", "SpO2 95%", "Temp 100.8 F", "RR 18 /min"]
IND_STAYS = ["2 days", "4 days", "7 days", "12 days", "2 weeks"]
IND_ABBREVS = ["T2DM", "HTN", "CAD", "CKD", "COPD", "AKI"]


def generate_independent_cohort(n_patients: int, seed: int = 2026) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    rng = random.Random(seed)
    voters: List[Dict[str, Any]] = []
    records: List[Dict[str, Any]] = []

    for i in range(n_patients):
        gender = rng.choice(["M", "F"])
        fn = rng.choice(IND_FIRST_M if gender == "M" else IND_FIRST_F)
        ln = rng.choice(IND_LAST)
        full_name = f"{fn} {ln}"
        hi_name = f"{rng.choice(IND_HI_FIRST)} {rng.choice(IND_HI_LAST)}"
        age = rng.randint(19, 82)
        city, region, pin = rng.choice(IND_CITIES)
        phone = f"+91-9{rng.randint(100000000, 999999999)}"

        voters.append({
            "voter_id": f"INDV-{i}",
            "name": full_name,
            "first": fn.lower(),
            "last": ln.lower(),
            "age": age,
            "gender": gender,
            "city": city,
            "region": region,
            "pin": pin,
            "phone": phone,
        })

        systems = rng.sample(["Hosp_Alpha", "Hosp_Beta", "Hosp_Gamma", "Hosp_Delta"], k=rng.randint(2, 3))
        med = rng.choice(IND_MEDS)
        dose = rng.choice(IND_DOSAGES)
        freq = rng.choice(IND_FREQS)
        lab = rng.choice(IND_LABS)
        vital = rng.choice(IND_VITALS)
        stay = rng.choice(IND_STAYS)

        for sys_name in systems:
            if sys_name == "Hosp_Alpha":
                text = (
                    f"{full_name} ({age}/{gender}) from {city} {pin}, Tel {phone}, "
                    f"admitted for {stay}. Rx: {med} {dose} {freq}. {lab}; {vital}."
                )
            elif sys_name == "Hosp_Beta":
                text = (
                    f"Marez {full_name}, umar {age}, ling {gender}, pata {city} {pin}, "
                    f"mob {phone}. Dawai {med} {dose} {freq}, {lab}, {vital}, stay {stay}."
                )
            elif sys_name == "Hosp_Gamma":
                text = (
                    f"रोगी {hi_name}, उम्र {age}, शहर {city}, फोन {phone}. "
                    f"Rx {med} {dose} {freq}, {lab}, {vital}, {stay}."
                )
            else:
                # Unstructured note with attendant/relative & abbreviated name
                text = (
                    f"{full_name} was admitted for {stay}. Gender: {gender}, Age: {age}, "
                    f"City: {city}. Attendant phone: {phone}. {med} {dose} {freq}, {lab}, {vital}."
                )

            records.append({
                "patient_idx": i,
                "system": sys_name,
                "raw_text": text,
                "name": full_name,
                "first": fn.lower(),
                "last": ln.lower(),
                "age": age,
                "gender": gender,
                "city": city,
                "pin": pin,
                "phone": phone,
            })

    # Distractor voters (50% extra)
    for d in range(max(20, n_patients // 2)):
        gender = rng.choice(["M", "F"])
        fn = rng.choice(IND_FIRST_M if gender == "M" else IND_FIRST_F)
        ln = rng.choice(IND_LAST)
        city, region, pin = rng.choice(IND_CITIES)
        voters.append({
            "voter_id": f"DIST-{d}",
            "name": f"{fn} {ln}",
            "first": fn.lower(),
            "last": ln.lower(),
            "age": rng.randint(19, 82),
            "gender": gender,
            "city": city,
            "region": region,
            "pin": pin,
            "phone": f"+91-8{rng.randint(100000000, 999999999)}",
        })

    return records, voters


def evaluate_cohort(
    n_patients: int,
    detector: MultilingualPIIDetector,
    anonymizer: AnonymizerEngine,
    age_band_size: int = 5,
    seed: int = 2026,
) -> Dict[str, Any]:
    records, voters = generate_independent_cohort(n_patients, seed=seed)
    policy = PolicyConfig(age_band_size=age_band_size)
    rng = random.Random(seed + 1)

    t0 = time.perf_counter()
    latencies_ms: List[float] = []

    correct_unique = 0
    incorrect_confident = 0
    coverage = 0
    forced_top_correct = 0.0
    group_sizes: List[int] = []
    direct_leaks = 0
    qi_exposed = 0

    # Also track cross-record pseudonym correlation
    psn_to_candidates: Dict[str, set[int]] = defaultdict(set)
    psn_to_true_patient: Dict[str, set[int]] = defaultdict(set)

    # Index voters by (gender, age_low, age_high) or exact
    for rec in records:
        rt0 = time.perf_counter()
        _, ents = detector.scan(rec["raw_text"])
        san_text, _ = anonymizer.anonymize(rec["raw_text"], ents, policy)
        latencies_ms.append((time.perf_counter() - rt0) * 1000.0)

        san_low = san_text.lower()
        # Check direct PII leakage in sanitized text
        leaked_phone = rec["phone"][-6:] in san_text
        leaked_first = rec["first"] in san_low
        leaked_last = rec["last"] in san_low
        leaked_pin = rec["pin"] in san_text
        if leaked_phone or leaked_first or leaked_last or leaked_pin:
            direct_leaks += 1

        # Attacker parses whatever QIs & leaked identifiers remain in sanitized_text
        band_match = re.search(r"\b(\d{1,3})[–\-](\d{1,3})\b", san_text)
        gender_match = re.search(r"\b(M|F)\b", san_text)
        leaked_city = rec["city"].lower() in san_low
        if band_match or gender_match or leaked_city:
            qi_exposed += 1

        # Filter voters using ONLY what is visible in san_text
        cands = []
        for idx, v in enumerate(voters):
            if leaked_phone and v["phone"] != rec["phone"]:
                continue
            if leaked_first and v["first"] != rec["first"]:
                continue
            if leaked_last and v["last"] != rec["last"]:
                continue
            if leaked_pin and v["pin"] != rec["pin"]:
                continue
            if leaked_city and v["city"].lower() != rec["city"].lower():
                continue
            if band_match:
                lo, hi = int(band_match.group(1)), int(band_match.group(2))
                if not (lo <= v["age"] <= hi):
                    continue
            if gender_match and v["gender"] != gender_match.group(1):
                continue
            cands.append(idx)

        if not cands:
            # Attacker falls back to full voter list if parsed signal contradicted
            cands = list(range(len(voters)))

        k = len(cands)
        group_sizes.append(k)
        coverage += 1
        true_in_cands = rec["patient_idx"] in cands

        if k == 1:
            if true_in_cands:
                correct_unique += 1
            else:
                incorrect_confident += 1

        # Forced top-match accuracy (expected probability of picking true voter from candidate set)
        if true_in_cands:
            forced_top_correct += 1.0 / k

        # Cross-record correlation via deterministic [PATIENT_XXXXXXXX] pseudonym
        psn_match = re.search(r"\[PATIENT_([A-F0-9]+)\]", san_text)
        if psn_match:
            psn = psn_match.group(0)
            psn_to_true_patient[psn].add(rec["patient_idx"])
            if psn not in psn_to_candidates:
                psn_to_candidates[psn] = set(cands)
            else:
                psn_to_candidates[psn] &= set(cands)

    total_s = time.perf_counter() - t0
    n_rec = len(records)
    lat_sorted = sorted(latencies_ms)
    p95 = lat_sorted[int(0.95 * len(lat_sorted))] if lat_sorted else 0.0

    # Cross-record correlation: average candidate size after intersecting across hospitals
    cross_sizes = [len(s) for s in psn_to_candidates.values() if len(s) > 0]
    cross_unique = sum(1 for s in cross_sizes if s == 1)

    return {
        "n_patients": n_patients,
        "n_records": n_rec,
        "n_voters": len(voters),
        "age_band_size": age_band_size,
        "correct_unique_reid_rate": round(correct_unique / n_rec, 4),
        "incorrect_confident_rate": round(incorrect_confident / n_rec, 4),
        "attacker_coverage": round(coverage / n_rec, 4),
        "forced_top_match_accuracy": round(forced_top_correct / n_rec, 4),
        "unique_record_rate": round(sum(1 for g in group_sizes if g == 1) / n_rec, 4),
        "min_group_size": min(group_sizes),
        "median_group_size": sorted(group_sizes)[len(group_sizes) // 2],
        "avg_group_size": round(sum(group_sizes) / len(group_sizes), 2),
        "direct_pii_leakage_rate": round(direct_leaks / n_rec, 4),
        "residual_qi_exposure_rate": round(qi_exposed / n_rec, 4),
        "cross_record_pseudonyms": len(cross_sizes),
        "cross_record_unique_rate": round(cross_unique / len(cross_sizes), 4) if cross_sizes else 0.0,
        "records_per_sec": round(n_rec / total_s, 1),
        "avg_latency_ms": round(sum(latencies_ms) / len(latencies_ms), 2),
        "p95_latency_ms": round(p95, 2),
        "total_seconds": round(total_s, 2),
    }


def run_clinical_stress_test(
    n_examples: int,
    detector: MultilingualPIIDetector,
    anonymizer: AnonymizerEngine,
) -> Dict[str, Any]:
    rng = random.Random(9001)
    fidelity_engine = MedicalFidelityEngine()
    policy = PolicyConfig()

    cats = {
        "medication_name": [0, 0],
        "decimal_dosage": [0, 0],
        "dosage_unit": [0, 0],
        "frequency": [0, 0],
        "lab_measurement": [0, 0],
        "vital_measurement": [0, 0],
        "stay_length": [0, 0],
        "medical_abbrev": [0, 0],
        "clinical_num_like_id": [0, 0],
    }
    fidelity_scores: List[float] = []
    failures_sample: List[Dict[str, str]] = []

    for i in range(n_examples):
        fn = rng.choice(IND_FIRST_M + IND_FIRST_F)
        ln = rng.choice(IND_LAST)
        med = rng.choice(IND_MEDS)
        dose = rng.choice(["12.5 mg", "0.25 mg", "7.5 ml", "10 units", "20 IU", "2 puffs"])
        unit = dose.split()[1]
        freq = rng.choice(IND_FREQS)
        lab = rng.choice(IND_LABS)
        vital = rng.choice(IND_VITALS)
        stay = rng.choice(IND_STAYS)
        abbrev = rng.choice(IND_ABBREVS)
        clin_num = rng.choice(["145000", "11200", "981234", "2026112601"])

        text = (
            f"Patient {fn} {ln} ({abbrev}), admitted for {stay}. "
            f"Rx: {med} {dose} {freq}. Lab: {lab} (Specimen {clin_num}). "
            f"Vitals: {vital}."
        )
        _, ents = detector.scan(text)
        san_text, _ = anonymizer.anonymize(text, ents, policy)
        fid = fidelity_engine.evaluate(text, san_text)
        fidelity_scores.append(fid["preservation_score"])

        san_low = san_text.lower()
        checks = {
            "medication_name": med.lower() in san_low,
            "decimal_dosage": dose.lower() in san_low,
            "dosage_unit": unit.lower() in san_low,
            "frequency": freq.lower() in san_low,
            "lab_measurement": lab.lower() in san_low,
            "vital_measurement": vital.lower() in san_low,
            "stay_length": stay.lower() in san_low,
            "medical_abbrev": abbrev.lower() in san_low,
            "clinical_num_like_id": clin_num in san_text,
        }
        for k, ok in checks.items():
            cats[k][0] += 1
            if ok:
                cats[k][1] += 1
            elif len(failures_sample) < 10:
                failures_sample.append({"category": k, "expected": text, "sanitized": san_text})

    return {
        "n_examples": n_examples,
        "builtin_fidelity_avg": round(sum(fidelity_scores) / len(fidelity_scores), 4),
        "independent_category_preservation": {
            k: {
                "total": v[0],
                "preserved": v[1],
                "rate": round(v[1] / v[0], 4),
            }
            for k, v in cats.items()
        },
        "failures_sample": failures_sample[:5],
    }


def run_multilingual_pii_stress_test(
    n_examples: int,
    detector: MultilingualPIIDetector,
    anonymizer: AnonymizerEngine,
) -> Dict[str, Any]:
    rng = random.Random(777)
    policy = PolicyConfig()

    patterns = [
        ("spelling_mariz", lambda fn, ln, ph: f"Mariz {fn} {ln}, mob {ph}, Metformin 500 mg."),
        ("spelling_marez", lambda fn, ln, ph: f"Marez {fn} {ln}, mob {ph}, Metformin 500 mg."),
        ("spelling_pateint", lambda fn, ln, ph: f"Pateint {fn} {ln}, tel {ph}, BP 120/80 mmHg."),
        ("unstructured_admitted", lambda fn, ln, ph: f"{fn} {ln} was admitted for 4 days. Phone {ph}."),
        ("attendant_ctx", lambda fn, ln, ph: f"Pt admitted. Attendant: {fn} {ln}, contact {ph}."),
        ("hindi_no_nukta", lambda fn, ln, ph: f"मरीज आदित्य कुलकर्णी, फोन {ph}, BP 130/80 mmHg."),
        ("zero_width_obfuscation", lambda fn, ln, ph: f"Patient {fn[0]}\u200b{fn[1:]} {ln}, phone {ph}."),
    ]

    results: Dict[str, Dict[str, Any]] = {name: {"total": 0, "name_caught": 0, "phone_caught": 0} for name, _ in patterns}
    for i in range(n_examples):
        pname, builder = patterns[i % len(patterns)]
        fn = rng.choice(IND_FIRST_M + IND_FIRST_F)
        ln = rng.choice(IND_LAST)
        ph = f"+91-98{rng.randint(10000000, 99999999)}"
        txt = builder(fn, ln, ph)
        _, ents = detector.scan(txt)
        san, _ = anonymizer.anonymize(txt, ents, policy)

        results[pname]["total"] += 1
        target_name = "आदित्य" if pname == "hindi_no_nukta" else fn
        if target_name.lower() not in san.lower():
            results[pname]["name_caught"] += 1
        if ph[-6:] not in san:
            results[pname]["phone_caught"] += 1

    for st in results.values():
        st["name_recall"] = round(st["name_caught"] / st["total"], 4)
        st["phone_recall"] = round(st["phone_caught"] / st["total"], 4)
    return results


def main() -> None:
    t_load0 = time.perf_counter()
    detector = MultilingualPIIDetector()
    anonymizer = AnonymizerEngine(secret_key="audit-only-ephemeral-key", release_scope="audit")
    model_load_ms = round((time.perf_counter() - t_load0) * 1000.0, 2)

    cohort_results = []
    for n in [100, 500, 1000, 5000]:
        cohort_results.append(evaluate_cohort(n, detector, anonymizer, age_band_size=5, seed=2026 + n))

    # Phase 3: Adaptive k / age band comparison on 500 patients
    adaptive_results = []
    for band in [2, 5, 10, 20]:
        adaptive_results.append(evaluate_cohort(500, detector, anonymizer, age_band_size=band, seed=3030))

    clinical_stress = run_clinical_stress_test(5000, detector, anonymizer)
    pii_stress = run_multilingual_pii_stress_test(1400, detector, anonymizer)

    peak_rss_mb = round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0, 2)

    out = {
        "model_load_ms": model_load_ms,
        "peak_rss_mb": peak_rss_mb,
        "phase1_2_cohorts": cohort_results,
        "phase3_age_band_tradeoff": adaptive_results,
        "phase5_clinical_stress_5000": clinical_stress,
        "phase6_multilingual_pii_stress": pii_stress,
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()

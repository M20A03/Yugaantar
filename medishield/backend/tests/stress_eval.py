"""Independent 1,050-record stress test & benchmark for MediShield (BEFORE/AFTER).

Uses a fixed seed (42) and disjoint unseen names, addresses, phone formats,
spelling variants, medical abbreviations, and hard-negative linkage pairs.
"""

import json
import random
import sys
import time
import tracemalloc
from pathlib import Path
from typing import Any, Dict, List, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.models.schemas import HospitalRecordInput, PolicyConfig  # noqa: E402
from app.services.anonymization.anonymizer import AnonymizerEngine  # noqa: E402
from app.services.medical_fidelity.fidelity import MedicalFidelityEngine  # noqa: E402
from app.services.pii_detection.detector import MultilingualPIIDetector  # noqa: E402
from app.services.record_linkage.linker import RecordLinkageEngine  # noqa: E402


UNSEEN_FIRST_EN = [
    "Aarav", "Vivaan", "Aditya", "Kabir", "Rohan", "Siddharth", "Nikhil", "Pranav",
    "Ananya", "Kavya", "Diya", "Sneha", "Pooja", "Nandini", "Ishita", "Shruti",
    "Vikram", "Deepak", "Manish", "Harsh", "Kiran", "Swati", "Meghna", "Tarun",
]
UNSEEN_LAST_EN = [
    "Kulkarni", "Deshmukh", "Nair", "Iyer", "Chatterjee", "Banerjee", "Patel", "Mehta",
    "Malhotra", "Kapoor", "Chauhan", "Rathore", "Reddy", "Naidu", "Menon", "Joshi",
    "Agarwal", "Bansal", "Saxena", "Tiwari", "Mishra", "Pandey", "Thakur", "Bose",
]
UNSEEN_HI_NAMES = [
    ("आरव", "कुलकर्णी"), ("कबीर", "मेहता"), ("अदिति", "नायर"), ("स्नेहा", "पांडे"),
    ("विक्रम", "राठौर"), ("पूजा", "तिवारी"), ("रोहन", "देशमुख"), ("कविता", "मिश्रा"),
    ("मनीष", "अग्रवाल"), ("दीपक", "चौहान"), ("नंदिनी", "बोस"), ("इशिता", "जोशी"),
]
UNSEEN_ADDRESSES_EN = [
    "14 Linking Road, Bandra West, Mumbai",
    "22 Park Street, Kolkata",
    "88 Anna Salai, Teynampet, Chennai",
    "45 Sector 17, Chandigarh",
    "221B Baker Street, London, UK",
    "742 Evergreen Terrace, Austin, TX",
    "19 Civil Lines, Jaipur",
    "304 Banjara Hills, Hyderabad",
]
UNSEEN_ADDRESSES_HI = [
    "सिविल लाइंस, प्रयागराज",
    "गोमती नगर, लखनऊ",
    "राजा पार्क, जयपुर",
    "विजय नगर, इंदौर",
]
CLINICAL_SCENARIOS = [
    ("Type 2 Diabetes", "Metformin", "500 mg", "1-0-1", "BP 138/88 mmHg"),
    ("Hypertension", "Ramipril", "5 mg", "OD", "BP 152/94 mmHg"),
    ("Dengue", "Paracetamol", "650 mg", "BD x 5 days", "Temp 102.4 F"),
    ("Asthma", "Amoxicillin", "250 mg", "TDS", "SpO2 94%"),
    ("Parkinson's disease", "Aspirin", "75 mg", "OD", "HbA1c 6.8%"),
    ("Viral Fever", "Azithromycin", "500 mg", "OD", "BP 118/76 mmHg"),
]
DOCTOR_NAMES = ["Dr. Arvind Menon", "Dr. Kavita Iyer", "Dr. S. K. Bose", "Dr. Neha Kapoor"]


def _phone_variant(rng: random.Random) -> str:
    d = f"{rng.choice(['6','7','8','9'])}{rng.randint(100000000, 999999999)}"
    fmt = rng.choice([0, 1, 2, 3, 4])
    if fmt == 0:
        return d
    if fmt == 1:
        return f"+91 {d[:5]} {d[5:]}"
    if fmt == 2:
        return f"+91-{d}"
    if fmt == 3:
        return f"0{d[:5]}-{d[5:]}"
    return f"+1-555-{rng.randint(100,999)}-{rng.randint(1000,9999)}"


def generate_dataset(seed: int = 42, per_lang: int = 350) -> List[Dict[str, Any]]:
    rng = random.Random(seed)
    records: List[Dict[str, Any]] = []

    for i in range(per_lang):
        fn, ln = rng.choice(UNSEEN_FIRST_EN), rng.choice(UNSEEN_LAST_EN)
        full_name = f"{fn} {ln}"
        age = rng.randint(19, 82)
        phone = _phone_variant(rng)
        addr = rng.choice(UNSEEN_ADDRESSES_EN)
        pin = str(rng.randint(110001, 800020))
        dx, med, dose, freq, vital = rng.choice(CLINICAL_SCENARIOS)
        doc = rng.choice(DOCTOR_NAMES)
        mrn = f"UHID-{rng.randint(100000, 999999)}"
        email = f"{fn.lower()}.{ln.lower()}{rng.randint(1,99)}@mail.example"

        template = i % 5
        if template == 0:
            text = (
                f"Patient {full_name}, aged {age}, residing at {addr}, PIN {pin}. "
                f"Contact: {phone}. {mrn}. C/O fever and cough. {doc} diagnosed {dx} "
                f"and prescribed {med} {dose} {freq}. {vital}."
            )
            exp_pii = [full_name, str(age), addr, pin, phone, mrn]
        elif template == 1:
            rel = f"{rng.choice(UNSEEN_FIRST_EN)} {ln}"
            text = (
                f"OPD Note: {full_name} ({age} yrs), C/O {rel}, phone {phone}, "
                f"email {email}. {doc} advised {med} {dose} for {dx}. {vital}."
            )
            exp_pii = [full_name, str(age), rel, phone, email]
        elif template == 2:
            # Missing phone, unstructured free-text name
            text = (
                f"{full_name} presented with {dx} and fever. {vital}. "
                f"Prescribed {med} {dose} {freq}. Address: {addr}."
            )
            exp_pii = [full_name, addr]
        elif template == 3:
            # Spelling mistake in label + PAN
            pan = f"{''.join(rng.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=5))}{rng.randint(1000,9999)}K"
            text = (
                f"Pateint: {full_name}, Age {age}, PAN: {pan}, Mob: {phone}. "
                f"Dx: {dx}. Rx: {med} {dose} {freq}. {vital}."
            )
            exp_pii = [full_name, str(age), pan, phone]
        else:
            # International phone/address + Aadhaar
            aadhaar = f"{rng.randint(2,9)}{rng.randint(100,999)} {rng.randint(1000,9999)} {rng.randint(1000,9999)}"
            text = (
                f"Name: {full_name}, Aadhaar {aadhaar}, residing at {addr}, Contact {phone}. "
                f"{doc} noted {dx}, {med} {dose}, {vital}."
            )
            exp_pii = [full_name, aadhaar, addr, phone]

        records.append(
            {
                "id": f"en_{i:04d}",
                "lang": "en",
                "text": text,
                "expected_pii": exp_pii,
                "must_preserve": [dx, med, dose, vital, doc] if doc in text else [dx, med, dose, vital],
            }
        )

    # Hindi (Devanagari) records
    for i in range(per_lang):
        fn_hi, ln_hi = rng.choice(UNSEEN_HI_NAMES)
        full_hi = f"{fn_hi} {ln_hi}"
        rel_hi = f"{rng.choice(UNSEEN_HI_NAMES)[0]} {ln_hi}"
        age = rng.randint(20, 78)
        phone = _phone_variant(rng)
        addr = rng.choice(UNSEEN_ADDRESSES_HI)
        pin = str(rng.randint(110001, 800020))
        dx, med, dose, freq, vital = rng.choice(CLINICAL_SCENARIOS)
        text = (
            f"रोगी: {full_hi}, उम्र {age} साल, पता: {addr}, PIN {pin}, "
            f"मोबाइल {phone}, C/O {rel_hi}. {dx} diagnosed. {med} {dose} {freq}. {vital}."
        )
        records.append(
            {
                "id": f"hi_{i:04d}",
                "lang": "hi",
                "text": text,
                "expected_pii": [full_hi, str(age), addr, pin, phone, rel_hi],
                "must_preserve": [dx, med, dose, vital],
            }
        )

    # Hinglish records
    for i in range(per_lang):
        fn, ln = rng.choice(UNSEEN_FIRST_EN), rng.choice(UNSEEN_LAST_EN)
        full_name = f"{fn} {ln}"
        age = rng.randint(20, 78)
        phone = _phone_variant(rng)
        addr = rng.choice(UNSEEN_ADDRESSES_EN)
        dx, med, dose, freq, vital = rng.choice(CLINICAL_SCENARIOS)
        mrn = f"OPD/{rng.randint(10000,99999)}"
        if i % 2 == 0:
            text = (
                f"{fn} ji ka {vital} hai, bukhar aur cough bhi hai. "
                f"Patient {full_name}, umra {age} saal, {mrn}, mobile {phone}. "
                f"{dx} ke liye {med} {dose} {freq} di gayi."
            )
            exp_pii = [fn, full_name, str(age), mrn, phone]
        else:
            text = (
                f"Mareez {full_name}, pata {addr}, contact {phone}. "
                f"Unko {dx} hai, {med} {dose} {freq} aur {vital} note kiya."
            )
            exp_pii = [full_name, addr, phone]
        records.append(
            {
                "id": f"hg_{i:04d}",
                "lang": "hinglish",
                "text": text,
                "expected_pii": exp_pii,
                "must_preserve": [dx, med, dose, vital],
            }
        )

    return records


def run_stress_benchmark() -> Dict[str, Any]:
    records = generate_dataset(seed=42, per_lang=350)  # 1,050 records
    detector = MultilingualPIIDetector()
    anonymizer = AnonymizerEngine(secret_key="stress-eval-secret")
    fidelity = MedicalFidelityEngine()

    tracemalloc.start()
    by_lang: Dict[str, Dict[str, Any]] = {
        "en": {"tp": 0, "fp": 0, "fn": 0, "leaks": 0, "exp": 0, "med_ok": 0, "med_tot": 0, "lat": [], "fails": []},
        "hi": {"tp": 0, "fp": 0, "fn": 0, "leaks": 0, "exp": 0, "med_ok": 0, "med_tot": 0, "lat": [], "fails": []},
        "hinglish": {"tp": 0, "fp": 0, "fn": 0, "leaks": 0, "exp": 0, "med_ok": 0, "med_tot": 0, "lat": [], "fails": []},
    }

    for rec in records:
        lang_key = rec["lang"]
        bucket = by_lang[lang_key]
        t0 = time.perf_counter()
        _, entities = detector.scan(rec["text"])
        sanitized, _ = anonymizer.anonymize(rec["text"], entities, PolicyConfig())
        _ = fidelity.evaluate(rec["text"], sanitized)
        dt_ms = (time.perf_counter() - t0) * 1000.0
        bucket["lat"].append(dt_ms)

        det_texts = [e.text.lower() for e in entities]
        expected = rec["expected_pii"]
        bucket["exp"] += len(expected)
        matched = 0
        missed = []
        for exp in expected:
            el = exp.lower()
            if any(el in d or d in el for d in det_texts):
                matched += 1
            else:
                bucket["fn"] += 1
                missed.append(exp)
            if el.isdigit() and f"{el}–" in sanitized.lower():
                continue
            if el in sanitized.lower():
                bucket["leaks"] += 1

        bucket["tp"] += matched
        bucket["fp"] += max(0, len(det_texts) - matched)

        for mp in rec["must_preserve"]:
            bucket["med_tot"] += 1
            if mp.lower() in sanitized.lower():
                bucket["med_ok"] += 1

        if missed and len(bucket["fails"]) < 3:
            bucket["fails"].append({"id": rec["id"], "missed": missed, "text": rec["text"][:160], "sanitized": sanitized[:160]})

    _, peak_bytes = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Record linkage stress test: 100 true pairs + 100 hard-negative pairs (same name, diff person!)
    linker = RecordLinkageEngine(secret_key="stress-eval-secret")
    link_recs: List[HospitalRecordInput] = []
    true_pairs = set()
    for i in range(50):
        fn, ln = UNSEEN_FIRST_EN[i % len(UNSEEN_FIRST_EN)], UNSEEN_LAST_EN[i % len(UNSEEN_LAST_EN)]
        ph = f"98{i:08d}"
        a_id, b_id = f"T_{i}_A", f"T_{i}_B"
        link_recs.append(HospitalRecordInput(record_id=a_id, hospital="H1", name=f"{fn} {ln}", phone=ph, age=30 + (i % 20), gender="M"))
        link_recs.append(HospitalRecordInput(record_id=b_id, hospital="H2", name=f"{fn[:3]}. {ln}", phone=f"+91-{ph}", age=30 + (i % 20), gender="M"))
        true_pairs.add(tuple(sorted([a_id, b_id])))
    for i in range(50):
        fn, ln = UNSEEN_FIRST_EN[i % len(UNSEEN_FIRST_EN)], UNSEEN_LAST_EN[i % len(UNSEEN_LAST_EN)]
        # Same name, completely different age and missing/different phone!
        link_recs.append(HospitalRecordInput(record_id=f"N_{i}_A", hospital="H1", name=f"{fn} {ln}", phone=None, age=22, gender="M"))
        link_recs.append(HospitalRecordInput(record_id=f"N_{i}_B", hospital="H3", name=f"{fn} {ln}", phone=None, age=65, gender="M"))

    _, flagged, _ = linker.analyze(link_recs, threshold=0.72)
    pred_pairs = {tuple(sorted([p.record_a, p.record_b])) for p in flagged}
    l_tp = len(pred_pairs & true_pairs)
    l_fp = len(pred_pairs - true_pairs)
    l_fn = len(true_pairs - pred_pairs)
    l_prec = l_tp / (l_tp + l_fp) if (l_tp + l_fp) else 1.0
    l_rec = l_tp / (l_tp + l_fn) if (l_tp + l_fn) else 1.0

    summary: Dict[str, Any] = {"total_records": len(records), "peak_memory_mb": round(peak_bytes / (1024 * 1024), 2), "languages": {}}
    all_tp = all_fp = all_fn = all_leaks = all_exp = all_med_ok = all_med_tot = 0
    all_lat: List[float] = []

    for lk, b in by_lang.items():
        p = b["tp"] / (b["tp"] + b["fp"]) if (b["tp"] + b["fp"]) else 1.0
        r = b["tp"] / (b["tp"] + b["fn"]) if (b["tp"] + b["fn"]) else 1.0
        f1 = (2 * p * r / (p + r)) if (p + r) else 0.0
        summary["languages"][lk] = {
            "precision": round(p, 4),
            "recall": round(r, 4),
            "f1": round(f1, 4),
            "leakage_rate": round(b["leaks"] / b["exp"], 4),
            "fpr": round(b["fp"] / (b["tp"] + b["fp"]), 4) if (b["tp"] + b["fp"]) else 0.0,
            "medical_preservation": round(b["med_ok"] / b["med_tot"], 4),
            "avg_latency_ms": round(sum(b["lat"]) / len(b["lat"]), 3),
            "worst_latency_ms": round(max(b["lat"]), 3),
            "sample_failures": b["fails"],
        }
        all_tp += b["tp"]
        all_fp += b["fp"]
        all_fn += b["fn"]
        all_leaks += b["leaks"]
        all_exp += b["exp"]
        all_med_ok += b["med_ok"]
        all_med_tot += b["med_tot"]
        all_lat.extend(b["lat"])

    ov_p = all_tp / (all_tp + all_fp)
    ov_r = all_tp / (all_tp + all_fn)
    summary["overall"] = {
        "precision": round(ov_p, 4),
        "recall": round(ov_r, 4),
        "f1": round(2 * ov_p * ov_r / (ov_p + ov_r), 4),
        "pii_leakage_rate": round(all_leaks / all_exp, 4),
        "fpr": round(all_fp / (all_tp + all_fp), 4),
        "medical_preservation": round(all_med_ok / all_med_tot, 4),
        "avg_latency_ms": round(sum(all_lat) / len(all_lat), 3),
        "worst_latency_ms": round(max(all_lat), 3),
        "linkage_precision": round(l_prec, 4),
        "linkage_recall": round(l_rec, 4),
        "linkage_false_positives": l_fp,
    }
    return summary


if __name__ == "__main__":
    print(json.dumps(run_stress_benchmark(), indent=2, ensure_ascii=False))

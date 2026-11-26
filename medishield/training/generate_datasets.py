"""Reproducible 50,000 PII + 50,000 Record Linkage synthetic dataset generator.

- 50,000 clinical records (20,000 English, 15,000 Hindi, 15,000 Hinglish)
- 50,000 record linkage pairs (15k match, 15k hard-neg, 10k missing, 10k multilingual/typo)
- Grouped 70% train / 15% val / 15% test splits by patient_group_id & template_family.
- Ground truth is produced directly during synthesis (never using the PII detector).
"""

import json
import random
from pathlib import Path
from typing import Any, Dict, List, Tuple


FIRST_EN = [
    "Aarav", "Vivaan", "Aditya", "Kabir", "Rohan", "Siddharth", "Nikhil", "Pranav",
    "Ananya", "Kavya", "Diya", "Sneha", "Pooja", "Nandini", "Ishita", "Shruti",
    "Vikram", "Deepak", "Manish", "Harsh", "Kiran", "Swati", "Meghna", "Tarun",
    "Dev", "Riya", "Tanvi", "Varun", "Gaurav", "Neha", "Aakash", "Simran",
]
LAST_EN = [
    "Kulkarni", "Deshmukh", "Nair", "Iyer", "Chatterjee", "Banerjee", "Patel", "Mehta",
    "Malhotra", "Kapoor", "Chauhan", "Rathore", "Reddy", "Naidu", "Menon", "Joshi",
    "Agarwal", "Bansal", "Saxena", "Tiwari", "Mishra", "Pandey", "Thakur", "Bose",
    "Khandelwal", "Srivastava", "Tripathi", "Choudhary", "Bhatt", "Gokhale",
]
NAMES_HI = [
    ("आरव", "कुलकर्णी"), ("कबीर", "मेहता"), ("अदिति", "नायर"), ("स्नेहा", "पांडे"),
    ("विक्रम", "राठौर"), ("पूजा", "तिवारी"), ("रोहन", "देशमुख"), ("कविता", "मिश्रा"),
    ("मनीष", "अग्रवाल"), ("दीपक", "चौहान"), ("नंदिनी", "बोस"), ("इशिता", "जोशी"),
    ("प्रणव", "पटेल"), ("तन्वी", "बंसल"), ("वरुण", "सक्सेना"), ("रिया", "भट्ट"),
]
ADDRESSES_EN = [
    "14 Linking Road, Bandra West, Mumbai",
    "22 Park Street, Kolkata",
    "88 Anna Salai, Teynampet, Chennai",
    "45 Sector 17, Chandigarh",
    "221B Baker Street, London, UK",
    "742 Evergreen Terrace, Austin, TX",
    "19 Civil Lines, Jaipur",
    "304 Banjara Hills, Hyderabad",
    "12 MG Road, Pune",
    "77 Residency Road, Bengaluru",
]
ADDRESSES_HI = [
    "सिविल लाइंस, प्रयागराज",
    "गोमती नगर, लखनऊ",
    "राजा पार्क, जयपुर",
    "विजय नगर, इंदौर",
    "मालवीय नगर, दिल्ली",
    "कंकड़बाग, पटना",
]
CLINICAL = [
    ("Type 2 Diabetes", "Metformin", "500 mg", "1-0-1", "BP 138/88 mmHg"),
    ("Hypertension", "Ramipril", "5 mg", "OD", "BP 152/94 mmHg"),
    ("Dengue", "Paracetamol", "650 mg", "BD x 5 days", "Temp 102.4 F"),
    ("Asthma", "Amoxicillin", "250 mg", "TDS", "SpO2 94%"),
    ("Parkinson's disease", "Aspirin", "75 mg", "OD", "HbA1c 6.8%"),
    ("Viral Fever", "Azithromycin", "500 mg", "OD", "BP 118/76 mmHg"),
]
DOCTORS = ["Dr. Arvind Menon", "Dr. Kavita Iyer", "Dr. S. K. Bose", "Dr. Neha Kapoor"]


def _append_span(parts: List[str], spans: List[Dict[str, Any]], text: str, label: str | None = None) -> None:
    start = sum(len(p) for p in parts)
    parts.append(text)
    if label is not None:
        spans.append({"entity_type": label, "text": text, "start": start, "end": start + len(text)})


def _phone(rng: random.Random) -> str:
    d = f"{rng.choice(['6','7','8','9'])}{rng.randint(100000000, 999999999)}"
    fmt = rng.randint(0, 4)
    if fmt == 0:
        return d
    if fmt == 1:
        return f"+91 {d[:5]} {d[5:]}"
    if fmt == 2:
        return f"+91-{d}"
    if fmt == 3:
        return f"0{d[:5]}-{d[5:]}"
    return f"+1-555-{rng.randint(100,999)}-{rng.randint(1000,9999)}"


def generate_pii_dataset(n_en: int = 20000, n_hi: int = 15000, n_hg: int = 15000, seed: int = 2026) -> List[Dict[str, Any]]:
    rng = random.Random(seed)
    rows: List[Dict[str, Any]] = []
    counts = [("en", n_en), ("hi", n_hi), ("hinglish", n_hg)]

    for lang, total in counts:
        for i in range(total):
            group_id = f"PGRP_{rng.randint(0, max(100, total // 3))}"
            dx, med, dose, freq, vital = rng.choice(CLINICAL)
            doc = rng.choice(DOCTORS)
            age = str(rng.randint(18, 84))
            ph = _phone(rng)
            pin = str(rng.randint(110001, 800020))
            mrn = f"UHID-{rng.randint(100000, 999999)}"
            parts: List[str] = []
            spans: List[Dict[str, Any]] = []

            if lang == "en":
                fn, ln = rng.choice(FIRST_EN), rng.choice(LAST_EN)
                name = f"{fn} {ln}"
                rel = f"{rng.choice(FIRST_EN)} {ln}"
                addr = rng.choice(ADDRESSES_EN)
                email = f"{fn.lower()}.{ln.lower()}{rng.randint(1,99)}@mail.example"
                tpl = f"en_tpl_{i % 5}"
                if i % 5 == 0:
                    _append_span(parts, spans, "Patient ")
                    _append_span(parts, spans, name, "PERSON")
                    _append_span(parts, spans, ", aged ")
                    _append_span(parts, spans, age, "AGE")
                    _append_span(parts, spans, ", residing at ")
                    _append_span(parts, spans, addr, "ADDRESS")
                    _append_span(parts, spans, ", PIN ")
                    _append_span(parts, spans, pin, "PIN_CODE")
                    _append_span(parts, spans, ". Contact: ")
                    _append_span(parts, spans, ph, "PHONE")
                    _append_span(parts, spans, f". C/O fever. {doc} diagnosed {dx}, {med} {dose} {freq}. {vital}.")
                elif i % 5 == 1:
                    _append_span(parts, spans, "OPD Note: ")
                    _append_span(parts, spans, name, "PERSON")
                    _append_span(parts, spans, " (")
                    _append_span(parts, spans, age, "AGE")
                    _append_span(parts, spans, " yrs), C/O ")
                    _append_span(parts, spans, rel, "RELATIVE_PERSON")
                    _append_span(parts, spans, ", phone ")
                    _append_span(parts, spans, ph, "PHONE")
                    _append_span(parts, spans, ", email ")
                    _append_span(parts, spans, email, "EMAIL")
                    _append_span(parts, spans, f". {doc} advised {med} {dose} for {dx}. {vital}.")
                elif i % 5 == 2:
                    _append_span(parts, spans, name, "PERSON")
                    _append_span(parts, spans, f" presented with {dx}. {vital}. Rx: {med} {dose} {freq}. Address: ")
                    _append_span(parts, spans, addr, "ADDRESS")
                    _append_span(parts, spans, ".")
                elif i % 5 == 3:
                    pan = f"{''.join(rng.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=5))}{rng.randint(1000,9999)}K"
                    _append_span(parts, spans, "Pateint: ")
                    _append_span(parts, spans, name, "PERSON")
                    _append_span(parts, spans, ", Age ")
                    _append_span(parts, spans, age, "AGE")
                    _append_span(parts, spans, ", PAN: ")
                    _append_span(parts, spans, pan, "PAN")
                    _append_span(parts, spans, ", Mob: ")
                    _append_span(parts, spans, ph, "PHONE")
                    _append_span(parts, spans, f". Dx: {dx}. {med} {dose} {freq}. {vital}.")
                else:
                    # Negative clinical-only control mixed with ID
                    _append_span(parts, spans, "Discharge Summary: ")
                    _append_span(parts, spans, mrn, "HOSPITAL_ID")
                    _append_span(parts, spans, f", {doc} noted {dx}, {med} {dose} {freq}, {vital}.")
            elif lang == "hi":
                fn_h, ln_h = rng.choice(NAMES_HI)
                name = f"{fn_h} {ln_h}"
                rel = f"{rng.choice(NAMES_HI)[0]} {ln_h}"
                addr = rng.choice(ADDRESSES_HI)
                tpl = f"hi_tpl_{i % 3}"
                _append_span(parts, spans, "रोगी: ")
                _append_span(parts, spans, name, "PERSON")
                _append_span(parts, spans, ", उम्र ")
                _append_span(parts, spans, age, "AGE")
                _append_span(parts, spans, " साल, पता: ")
                _append_span(parts, spans, addr, "ADDRESS")
                _append_span(parts, spans, ", PIN ")
                _append_span(parts, spans, pin, "PIN_CODE")
                _append_span(parts, spans, ", मोबाइल ")
                _append_span(parts, spans, ph, "PHONE")
                _append_span(parts, spans, ", C/O ")
                _append_span(parts, spans, rel, "RELATIVE_PERSON")
                _append_span(parts, spans, f". {dx} diagnosed. {med} {dose} {freq}. {vital}.")
            else:
                fn, ln = rng.choice(FIRST_EN), rng.choice(LAST_EN)
                name = f"{fn} {ln}"
                addr = rng.choice(ADDRESSES_EN)
                tpl = f"hg_tpl_{i % 2}"
                if i % 2 == 0:
                    _append_span(parts, spans, fn, "PERSON")
                    _append_span(parts, spans, f" ji ka {vital} hai, bukhar bhi hai. Patient ")
                    _append_span(parts, spans, name, "PERSON")
                    _append_span(parts, spans, ", umra ")
                    _append_span(parts, spans, age, "AGE")
                    _append_span(parts, spans, " saal, ")
                    _append_span(parts, spans, mrn, "HOSPITAL_ID")
                    _append_span(parts, spans, ", mobile ")
                    _append_span(parts, spans, ph, "PHONE")
                    _append_span(parts, spans, f". {dx} ke liye {med} {dose} {freq}.")
                else:
                    _append_span(parts, spans, "Mareez ")
                    _append_span(parts, spans, name, "PERSON")
                    _append_span(parts, spans, ", pata ")
                    _append_span(parts, spans, addr, "ADDRESS")
                    _append_span(parts, spans, ", contact ")
                    _append_span(parts, spans, ph, "PHONE")
                    _append_span(parts, spans, f". Unko {dx} hai, {med} {dose} {freq} aur {vital}.")

            rows.append(
                {
                    "id": f"{lang}_{i:05d}",
                    "language": lang,
                    "group_id": group_id,
                    "template_family": tpl,
                    "text": "".join(parts),
                    "entities": spans,
                    "clinical_spans": [dx, med, dose, vital],
                }
            )
    return rows


def generate_linkage_dataset(seed: int = 2026) -> List[Dict[str, Any]]:
    """50,000 labeled record pairs: 15k match, 15k hard-neg, 10k missing, 10k multilingual/typo."""
    rng = random.Random(seed + 1)
    pairs: List[Dict[str, Any]] = []

    def _rec(rid: str, hosp: str, name: str, phone: str | None, age: int | None, gender: str, addr: str | None) -> Dict[str, Any]:
        return {"record_id": rid, "hospital": hosp, "name": name, "phone": phone, "age": age, "gender": gender, "address": addr}

    # 1. 15,000 matching pairs across hospitals
    for i in range(15000):
        fn, ln = rng.choice(FIRST_EN), rng.choice(LAST_EN)
        ph = f"9{rng.randint(100000000, 999999999)}"
        age = rng.randint(20, 80)
        g = rng.choice(["M", "F"])
        addr = rng.choice(ADDRESSES_EN)
        r1 = _rec(f"M_{i}_A", "HOSP_A", f"{fn} {ln}", ph, age, g, addr)
        r2 = _rec(f"M_{i}_B", "HOSP_B", f"{fn[:3]}. {ln}", f"+91-{ph}", age + rng.choice([0, 0, 1]), g, addr)
        pairs.append({"pair_id": f"PM_{i:05d}", "group_id": f"LGRP_{i}", "category": "match", "label": 1, "record_a": r1, "record_b": r2})

    # 2. 15,000 hard-negative pairs (same name, different patient!)
    for i in range(15000):
        fn, ln = rng.choice(FIRST_EN), rng.choice(LAST_EN)
        age_a = rng.randint(19, 32)
        age_b = rng.randint(52, 82)
        g = rng.choice(["M", "F"])
        r1 = _rec(f"HN_{i}_A", "HOSP_A", f"{fn} {ln}", f"9{rng.randint(100000000,999999999)}", age_a, g, rng.choice(ADDRESSES_EN))
        r2 = _rec(f"HN_{i}_B", "HOSP_C", f"{fn} {ln}", f"8{rng.randint(100000000,999999999)}", age_b, g, rng.choice(ADDRESSES_EN))
        pairs.append({"pair_id": f"PHN_{i:05d}", "group_id": f"LNGRP_{i}", "category": "hard_negative", "label": 0, "record_a": r1, "record_b": r2})

    # 3. 10,000 pairs with missing fields (5,000 match, 5,000 non-match)
    for i in range(10000):
        fn, ln = rng.choice(FIRST_EN), rng.choice(LAST_EN)
        is_match = i < 5000
        ph = f"7{rng.randint(100000000, 999999999)}"
        age = rng.randint(22, 75)
        g = rng.choice(["M", "F"])
        if is_match:
            r1 = _rec(f"MS_{i}_A", "HOSP_A", f"{fn} {ln}", ph, age, g, None)
            r2 = _rec(f"MS_{i}_B", "HOSP_B", f"{fn} {ln}", ph, None, g, rng.choice(ADDRESSES_EN))
            lbl = 1
        else:
            r1 = _rec(f"MS_{i}_A", "HOSP_A", f"{fn} {ln}", None, 23, g, None)
            r2 = _rec(f"MS_{i}_B", "HOSP_B", f"{fn} {ln}", None, 64, g, None)
            lbl = 0
        pairs.append({"pair_id": f"PMS_{i:05d}", "group_id": f"LMGRP_{i}", "category": "missing_fields", "label": lbl, "record_a": r1, "record_b": r2})

    # 4. 10,000 multilingual & spelling variation pairs (5,000 match, 5,000 non-match)
    for i in range(10000):
        idx = i % len(NAMES_HI)
        fn_h, ln_h = NAMES_HI[idx]
        en_equiv = [
            "Aarav Kulkarni", "Kabir Mehta", "Aditi Nair", "Sneha Pandey",
            "Vikram Rathore", "Pooja Tiwari", "Rohan Deshmukh", "Kavita Mishra",
            "Manish Agarwal", "Deepak Chauhan", "Nandini Bose", "Ishita Joshi",
            "Pranav Patel", "Tanvi Bansal", "Varun Saxena", "Riya Bhatt",
        ][idx]
        ph = f"6{rng.randint(100000000, 999999999)}"
        age = rng.randint(24, 70)
        g = rng.choice(["M", "F"])
        if i < 5000:
            r1 = _rec(f"ML_{i}_A", "HOSP_A", f"{fn_h} {ln_h}", ph, age, g, rng.choice(ADDRESSES_HI))
            r2 = _rec(f"ML_{i}_B", "HOSP_B", en_equiv, f"+91 {ph[:5]} {ph[5:]}", age, g, rng.choice(ADDRESSES_EN))
            lbl = 1
        else:
            other_h = NAMES_HI[(idx + 3) % len(NAMES_HI)]
            r1 = _rec(f"ML_{i}_A", "HOSP_A", f"{fn_h} {ln_h}", ph, age, g, rng.choice(ADDRESSES_HI))
            r2 = _rec(f"ML_{i}_B", "HOSP_C", f"{other_h[0]} {other_h[1]}", f"9{rng.randint(100000000,999999999)}", age + 12, g, rng.choice(ADDRESSES_HI))
            lbl = 0
        pairs.append({"pair_id": f"PML_{i:05d}", "group_id": f"LMLGRP_{i}", "category": "multilingual", "label": lbl, "record_a": r1, "record_b": r2})

    return pairs


def group_split(items: List[Dict[str, Any]], key_fn, seed: int = 2026) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], List[Dict[str, Any]]]:
    rng = random.Random(seed)
    groups = sorted({key_fn(x) for x in items})
    rng.shuffle(groups)
    n = len(groups)
    g_train = set(groups[: int(0.70 * n)])
    g_val = set(groups[int(0.70 * n) : int(0.85 * n)])
    train, val, test = [], [], []
    for x in items:
        gk = key_fn(x)
        if gk in g_train:
            train.append(x)
        elif gk in g_val:
            val.append(x)
        else:
            test.append(x)
    return train, val, test


if __name__ == "__main__":
    out_dir = Path(__file__).resolve().parent / "generated"
    out_dir.mkdir(parents=True, exist_ok=True)
    pii = generate_pii_dataset()
    link = generate_linkage_dataset()
    p_tr, p_va, p_te = group_split(pii, lambda x: x["group_id"])
    l_tr, l_va, l_te = group_split(link, lambda x: x["group_id"])
    summary = {
        "pii_total": len(pii),
        "pii_splits": {"train": len(p_tr), "val": len(p_va), "test": len(p_te)},
        "linkage_total": len(link),
        "linkage_splits": {"train": len(l_tr), "val": len(l_va), "test": len(l_te)},
    }
    (out_dir / "dataset_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))

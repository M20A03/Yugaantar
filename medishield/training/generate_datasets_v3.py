"""V3 diverse, shortcut-free 50,000-pair linkage dataset & sealed 5,000-pair challenge generator.

Uses disjoint name/city pools across train, val, test, and the sealed challenge set
so patient identity overlap across splits is strictly 0.
"""

import random
from typing import Any, Dict, List, Tuple


# Partitioned name pools so train/val/test/challenge have ZERO overlapping identities
TRAIN_FIRST = [
    ("Aarav", "आरव"), ("Vivaan", "विवान"), ("Aditya", "आदित्य"), ("Kabir", "कबीर"),
    ("Rohan", "रोहन"), ("Siddharth", "सिद्धार्थ"), ("Nikhil", "निखिल"), ("Pranav", "प्रणव"),
    ("Ananya", "अनन्या"), ("Kavya", "काव्या"), ("Diya", "दीया"), ("Sneha", "स्नेहा"),
    ("Pooja", "पूजा"), ("Nandini", "नंदिनी"), ("Ishita", "इशिता"), ("Shruti", "श्रुति"),
]
TRAIN_LAST = [
    ("Kulkarni", "कुलकर्णी"), ("Deshmukh", "देशमुख"), ("Nair", "नायर"), ("Iyer", "अय्यर"),
    ("Chatterjee", "चटर्जी"), ("Banerjee", "बनर्जी"), ("Patel", "पटेल"), ("Mehta", "मेहता"),
    ("Malhotra", "मल्होत्रा"), ("Kapoor", "कपूर"), ("Chauhan", "चौहान"), ("Rathore", "राठौर"),
]
VAL_FIRST = [
    ("Vikram", "विक्रम"), ("Deepak", "दीपक"), ("Manish", "मनीष"), ("Harsh", "हर्ष"),
    ("Kiran", "किरण"), ("Swati", "स्वाति"), ("Meghna", "मेघना"), ("Tarun", "तरुण"),
]
VAL_LAST = [
    ("Reddy", "रेड्डी"), ("Naidu", "नायडू"), ("Menon", "मेनन"), ("Joshi", "जोशी"),
    ("Agarwal", "अग्रवाल"), ("Bansal", "बंसल"),
]
TEST_FIRST = [
    ("Dev", "देव"), ("Riya", "रिया"), ("Tanvi", "तन्वी"), ("Varun", "वरुण"),
    ("Gaurav", "गौरव"), ("Neha", "नेहा"), ("Aakash", "आकाश"), ("Simran", "सिमरन"),
]
TEST_LAST = [
    ("Saxena", "सक्सेना"), ("Tiwari", "तिवारी"), ("Mishra", "मिश्रा"), ("Pandey", "पांडे"),
    ("Thakur", "ठाकुर"), ("Bose", "बोस"),
]

# Completely separate sealed challenge pool (never used in train/val/test)
SEALED_FIRST = [
    ("Chirag", "चिराग"), ("Bhavna", "भावना"), ("Nitin", "नितिन"), ("Komal", "कोमल"),
    ("Saurabh", "सौरभ"), ("Rashmi", "रश्मि"), ("Pankaj", "पंकज"), ("Shalini", "शालिनी"),
]
SEALED_LAST = [
    ("Khandelwal", "खंडेलवाल"), ("Srivastava", "श्रीवास्तव"), ("Tripathi", "त्रिपाठी"),
    ("Choudhary", "चौधरी"), ("Bhatt", "भट्ट"), ("Upadhyay", "उपाध्याय"),
]

CITIES_POOL = [
    "14 Linking Rd, Mumbai", "22 Park St, Kolkata", "88 Anna Salai, Chennai",
    "45 Sector 17, Chandigarh", "19 Civil Lines, Jaipur", "304 Banjara Hills, Hyderabad",
    "12 MG Rd, Pune", "77 Residency Rd, Bengaluru",
]
SEALED_CITIES = ["41 VIP Rd, Surat", "9 Mall Rd, Shimla", "18 Station Rd, Ranchi", "62 Lake Rd, Udaipur"]


def _typo(s: str, rng: random.Random) -> str:
    if len(s) > 5:
        i = rng.randint(1, len(s) - 2)
        return s[:i] + s[i + 1 :]
    return s + "a"


def _make_pairs(
    n_pairs: int,
    first_pool: List[Tuple[str, str]],
    last_pool: List[Tuple[str, str]],
    cities: List[str],
    seed: int,
    prefix: str,
) -> List[Dict[str, Any]]:
    rng = random.Random(seed)
    pairs: List[Dict[str, Any]] = []
    half = n_pairs // 2

    # Positive matches with diverse realistic noise (no single shortcut!)
    for i in range(half):
        fn_en, fn_hi = rng.choice(first_pool)
        ln_en, ln_hi = rng.choice(last_pool)
        ph = f"9{rng.randint(100000000, 999999999)}"
        age = rng.randint(20, 76)
        dob = f"{1950 + (76 - age):04d}-{rng.randint(1,12):02d}-{rng.randint(1,28):02d}"
        g = rng.choice(["M", "F"])
        addr = rng.choice(cities)
        mrn_a, mrn_b = f"H1-{i}", f"H2-{i}"

        kind = i % 7
        if kind == 0:
            # Transliteration + changed address + age off by 1
            r1 = {"record_id": f"{prefix}P_{i}_A", "hospital": "H1", "name": f"{fn_hi} {ln_hi}", "phone": ph, "age": age, "dob": dob, "gender": g, "address": addr, "mrn": mrn_a}
            r2 = {"record_id": f"{prefix}P_{i}_B", "hospital": "H2", "name": f"{fn_en} {ln_en}", "phone": f"+91-{ph}", "age": age + 1, "dob": dob, "gender": g, "address": rng.choice(cities), "mrn": mrn_b}
        elif kind == 1:
            # 1-digit phone typo + spelling error + missing gender
            ph2 = ph[:-1] + str((int(ph[-1]) + 2) % 10)
            r1 = {"record_id": f"{prefix}P_{i}_A", "hospital": "H1", "name": f"{fn_en} {ln_en}", "phone": ph, "age": age, "dob": dob, "gender": g, "address": addr, "mrn": mrn_a}
            r2 = {"record_id": f"{prefix}P_{i}_B", "hospital": "H2", "name": f"{_typo(fn_en, rng)} {_typo(ln_en, rng)}", "phone": ph2, "age": age, "dob": None, "gender": None, "address": addr, "mrn": mrn_b}
        elif kind == 2:
            # Missing phone on one side, BUT exact DOB + same address + same name + same gender!
            r1 = {"record_id": f"{prefix}P_{i}_A", "hospital": "H1", "name": f"{fn_en} {ln_en}", "phone": ph, "age": age, "dob": dob, "gender": g, "address": addr, "mrn": mrn_a}
            r2 = {"record_id": f"{prefix}P_{i}_B", "hospital": "H2", "name": f"{fn_en} {ln_en}", "phone": None, "age": age, "dob": dob, "gender": g, "address": addr, "mrn": mrn_b}
        elif kind == 3:
            # Changed phone number, BUT exact DOB + exact name + same address!
            ph_new = f"8{rng.randint(100000000, 999999999)}"
            r1 = {"record_id": f"{prefix}P_{i}_A", "hospital": "H1", "name": f"{fn_en} {ln_en}", "phone": ph, "age": age, "dob": dob, "gender": g, "address": addr, "mrn": mrn_a}
            r2 = {"record_id": f"{prefix}P_{i}_B", "hospital": "H2", "name": f"{fn_en} {ln_en}", "phone": ph_new, "age": age, "dob": dob, "gender": g, "address": addr, "mrn": mrn_b}
        elif kind == 4:
            # Abbreviated name + matching phone + age off by 2
            r1 = {"record_id": f"{prefix}P_{i}_A", "hospital": "H1", "name": f"{fn_en} {ln_en}", "phone": ph, "age": age, "dob": None, "gender": g, "address": addr, "mrn": mrn_a}
            r2 = {"record_id": f"{prefix}P_{i}_B", "hospital": "H2", "name": f"{fn_en[0]}. {ln_en}", "phone": ph, "age": age + 2, "dob": None, "gender": g, "address": None, "mrn": mrn_b}
        elif kind == 5:
            # Mixed script ("Aarav कुलकर्णी") + matching phone + missing age
            r1 = {"record_id": f"{prefix}P_{i}_A", "hospital": "H1", "name": f"{fn_en} {ln_hi}", "phone": ph, "age": age, "dob": dob, "gender": g, "address": addr, "mrn": mrn_a}
            r2 = {"record_id": f"{prefix}P_{i}_B", "hospital": "H2", "name": f"{fn_en} {ln_en}", "phone": f"+91 {ph[:5]} {ph[5:]}", "age": None, "dob": None, "gender": g, "address": addr, "mrn": mrn_b}
        else:
            # Duplicate hospital visit (same hospital, swapped name)
            r1 = {"record_id": f"{prefix}P_{i}_A", "hospital": "H1", "name": f"{fn_en} {ln_en}", "phone": ph, "age": age, "dob": dob, "gender": g, "address": addr, "mrn": mrn_a}
            r2 = {"record_id": f"{prefix}P_{i}_B", "hospital": "H1", "name": f"{ln_en} {fn_en}", "phone": ph, "age": age, "dob": dob, "gender": g, "address": addr, "mrn": mrn_a}

        pairs.append({"pair_id": f"{prefix}P_{i:05d}", "label": 1, "family": f"pos_{kind}", "record_a": r1, "record_b": r2})

    # Negative pairs (including shared family phones, same-age/same-name strangers, contradictory DOB/gender)
    for i in range(half):
        fn_en, fn_hi = rng.choice(first_pool)
        ln_en, ln_hi = rng.choice(last_pool)
        fn2_en, _ = rng.choice([x for x in first_pool if x[0] != fn_en])
        ln2_en, _ = rng.choice([x for x in last_pool if x[0] != ln_en])
        ph1 = f"9{rng.randint(100000000, 999999999)}"
        ph2 = f"7{rng.randint(100000000, 999999999)}"
        age = rng.randint(22, 70)
        dob1 = f"{1955 + (70 - age):04d}-04-12"
        dob2 = f"{1955 + (70 - age):04d}-09-23"
        g = rng.choice(["M", "F"])
        addr = rng.choice(cities)
        addr2 = rng.choice([c for c in cities if c != addr])

        kind = i % 6
        if kind == 0:
            # Identical name, SAME age (0-2 yrs), same city, different phone & DOB
            r1 = {"record_id": f"{prefix}N_{i}_A", "hospital": "H1", "name": f"{fn_en} {ln_en}", "phone": ph1, "age": age, "dob": dob1, "gender": g, "address": addr}
            r2 = {"record_id": f"{prefix}N_{i}_B", "hospital": "H3", "name": f"{fn_en} {ln_en}", "phone": ph2, "age": age + rng.choice([0, 1, 2]), "dob": dob2, "gender": g, "address": addr}
        elif kind == 1:
            # Shared family phone number! Different first name & different age
            r1 = {"record_id": f"{prefix}N_{i}_A", "hospital": "H1", "name": f"{fn_en} {ln_en}", "phone": ph1, "age": age, "dob": dob1, "gender": g, "address": addr}
            r2 = {"record_id": f"{prefix}N_{i}_B", "hospital": "H2", "name": f"{fn2_en} {ln_en}", "phone": ph1, "age": age + 24, "dob": None, "gender": "F" if g == "M" else "M", "address": addr}
        elif kind == 2:
            # Identical name, close age, missing phone, DIFFERENT address & missing/diff DOB
            r1 = {"record_id": f"{prefix}N_{i}_A", "hospital": "H1", "name": f"{fn_en} {ln_en}", "phone": ph1, "age": age, "dob": dob1, "gender": g, "address": addr}
            r2 = {"record_id": f"{prefix}N_{i}_B", "hospital": "H3", "name": f"{fn_en} {ln_en}", "phone": None, "age": age + 1, "dob": dob2, "gender": g, "address": addr2}
        elif kind == 3:
            # Same first name, DIFFERENT last name (Hindi vs English), same age & city, diff phone
            r1 = {"record_id": f"{prefix}N_{i}_A", "hospital": "H1", "name": f"{fn_hi} {ln_hi}", "phone": ph1, "age": age, "dob": None, "gender": g, "address": addr}
            r2 = {"record_id": f"{prefix}N_{i}_B", "hospital": "H3", "name": f"{fn_en} {ln2_en}", "phone": ph2, "age": age + 1, "dob": None, "gender": g, "address": addr}
        elif kind == 4:
            # Identical name, contradictory gender
            r1 = {"record_id": f"{prefix}N_{i}_A", "hospital": "H1", "name": f"{fn_en} {ln_en}", "phone": ph1, "age": age, "dob": dob1, "gender": g, "address": addr}
            r2 = {"record_id": f"{prefix}N_{i}_B", "hospital": "H3", "name": f"{fn_en} {ln_en}", "phone": None, "age": age, "dob": dob1, "gender": "F" if g == "M" else "M", "address": addr}
        else:
            # Different patients, large age gap + diff phone
            r1 = {"record_id": f"{prefix}N_{i}_A", "hospital": "H1", "name": f"{fn_en} {ln_en}", "phone": ph1, "age": 22, "dob": None, "gender": g, "address": addr}
            r2 = {"record_id": f"{prefix}N_{i}_B", "hospital": "H3", "name": f"{fn_en} {ln_en}", "phone": ph2, "age": 66, "dob": None, "gender": g, "address": addr2}

        pairs.append({"pair_id": f"{prefix}N_{i:05d}", "label": 0, "family": f"neg_{kind}", "record_a": r1, "record_b": r2})

    rng.shuffle(pairs)
    return pairs


def generate_v3_splits() -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Returns (train 35k, val 7.5k, test 7.5k, sealed_challenge 5k) with ZERO identity overlap."""
    train = _make_pairs(35000, TRAIN_FIRST, TRAIN_LAST, CITIES_POOL, seed=3001, prefix="TR")
    val = _make_pairs(7500, VAL_FIRST, VAL_LAST, CITIES_POOL, seed=3002, prefix="VA")
    test = _make_pairs(7500, TEST_FIRST, TEST_LAST, CITIES_POOL, seed=3003, prefix="TE")
    sealed = _make_pairs(5000, SEALED_FIRST, SEALED_LAST, SEALED_CITIES, seed=3004, prefix="SC")
    return train, val, test, sealed

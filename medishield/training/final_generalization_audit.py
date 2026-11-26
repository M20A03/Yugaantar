"""Final 5,000-pair independent generalization audit on frozen linkage_model.joblib.

Uses completely disjoint names, cities, and template families never seen in
training or validation. Verifies zero identity overlap and zero duplicates.
"""

import json
import random
import sys
import time
from pathlib import Path
from typing import Any, Dict, List

import joblib
import numpy as np
from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "backend"))
sys.path.insert(0, str(ROOT / "training"))

from generate_datasets import generate_linkage_dataset  # noqa: E402
from train_and_evaluate import _extract_linkage_features  # noqa: E402


# Completely disjoint from FIRST_EN, LAST_EN, NAMES_HI, ADDRESSES_EN/HI
AUDIT_NAMES_PAIR = [
    ("Raghav", "Kulshrestha", "राघव", "कुलश्रेष्ठ"),
    ("Madhavi", "Deshpande", "माधवी", "देशपांडे"),
    ("Yashwant", "Gokhale", "यशवंत", "गोखले"),
    ("Pallavi", "Chitale", "पल्लवी", "चितळे"),
    ("Shrikant", "Bhattacharya", "श्रीकांत", "भट्टाचार्य"),
    ("Vasudha", "Subramanian", "वसुधा", "सुब्रमण्यन"),
    ("Prashant", "Chakraborty", "प्रशांत", "चक्रवर्ती"),
    ("Aparna", "Venkatesh", "अपर्णा", "वेंकटेश"),
    ("Hemant", "Kshirsagar", "हेमंत", "क्षीरसागर"),
    ("Rohini", "Narasimhan", "रोहिणी", "नरसिम्हन"),
    ("Abhijit", "Sengupta", "अभिजीत", "सेनगुप्ता"),
    ("Sujata", "Kulkarni", "सुजाता", "कुलकर्णी"),  # wait: keep 100% disjoint!
]
# Replace last entry so 100% disjoint from FIRST_EN/LAST_EN
AUDIT_NAMES_PAIR[-1] = ("Sujata", "Paranjape", "सुजाता", "परांजपे")

AUDIT_CITIES = ["Mysuru", "Kochi", "Guwahati", "Bhubaneswar", "Dehradun", "Udaipur", "Madurai", "Raipur"]


def _spell_variant(s: str, rng: random.Random) -> str:
    if len(s) > 5 and rng.random() < 0.7:
        idx = rng.randint(1, len(s) - 2)
        return s[:idx] + s[idx + 1 :]  # drop 1 char typo
    return s + "a" if not s.endswith("a") else s[:-1]


def generate_5000_audit_pairs(seed: int = 9001) -> List[Dict[str, Any]]:
    rng = random.Random(seed)
    pairs: List[Dict[str, Any]] = []

    # 2,500 difficult positive matches (500 each of 5 unseen families)
    for i in range(2500):
        fn, ln, fn_hi, ln_hi = rng.choice(AUDIT_NAMES_PAIR)
        ph = f"9{rng.randint(100000000, 999999999)}"
        age = rng.randint(24, 72)
        g = rng.choice(["M", "F"])
        city = rng.choice(AUDIT_CITIES)
        fam = i % 5

        if fam == 0:
            # Hindi-to-English transliteration + missing address + age diff 1
            r1 = {"record_id": f"AP_{i}_A", "hospital": "H_X", "name": f"{fn_hi} {ln_hi}", "phone": ph, "age": age, "gender": g, "address": city}
            r2 = {"record_id": f"AP_{i}_B", "hospital": "H_Y", "name": f"{fn} {ln}", "phone": f"+91-{ph}", "age": age + 1, "gender": g, "address": None}
        elif fam == 1:
            # Spelling variation + 1-digit phone typo + age diff 2
            ph2 = ph[:-1] + str((int(ph[-1]) + 3) % 10)
            r1 = {"record_id": f"AP_{i}_A", "hospital": "H_X", "name": f"{fn} {ln}", "phone": ph, "age": age, "gender": g, "address": city}
            r2 = {"record_id": f"AP_{i}_B", "hospital": "H_Y", "name": f"{_spell_variant(fn, rng)} {_spell_variant(ln, rng)}", "phone": ph2, "age": age + 2, "gender": g, "address": city}
        elif fam == 2:
            # Missing phone on one side + identical name + same city + age diff 2
            r1 = {"record_id": f"AP_{i}_A", "hospital": "H_X", "name": f"{fn} {ln}", "phone": ph, "age": age, "gender": g, "address": city}
            r2 = {"record_id": f"AP_{i}_B", "hospital": "H_Y", "name": f"{fn} {ln}", "phone": None, "age": age + 2, "gender": g, "address": city}
        elif fam == 3:
            # Swapped name order + incorrect age (off by 4) + matching phone
            r1 = {"record_id": f"AP_{i}_A", "hospital": "H_X", "name": f"{fn} {ln}", "phone": ph, "age": age, "gender": g, "address": city}
            r2 = {"record_id": f"AP_{i}_B", "hospital": "H_Y", "name": f"{ln} {fn}", "phone": ph, "age": age + 4, "gender": g, "address": None}
        else:
            # Initial + spelling typo + matching phone
            r1 = {"record_id": f"AP_{i}_A", "hospital": "H_X", "name": f"{fn} {ln}", "phone": ph, "age": age, "gender": g, "address": city}
            r2 = {"record_id": f"AP_{i}_B", "hospital": "H_Y", "name": f"{fn[0]}. {_spell_variant(ln, rng)}", "phone": f"+91 {ph[:5]} {ph[5:]}", "age": age, "gender": g, "address": city}
        pairs.append({"pair_id": f"AP_{i:04d}", "label": 1, "family": f"pos_{fam}", "record_a": r1, "record_b": r2})

    # 2,500 difficult negative pairs (same/similar names, close ages, contradictory info)
    for i in range(2500):
        fn, ln, fn_hi, ln_hi = rng.choice(AUDIT_NAMES_PAIR)
        age = rng.randint(24, 72)
        g = rng.choice(["M", "F"])
        city = rng.choice(AUDIT_CITIES)
        city2 = rng.choice([c for c in AUDIT_CITIES if c != city])
        ph1 = f"9{rng.randint(100000000, 999999999)}"
        ph2 = f"7{rng.randint(100000000, 999999999)}"
        fam = i % 4

        if fam == 0:
            # Identical name, SAME age (0-2 yrs), same gender, same city, DIFFERENT phone (contradictory!)
            r1 = {"record_id": f"AN_{i}_A", "hospital": "H_X", "name": f"{fn} {ln}", "phone": ph1, "age": age, "gender": g, "address": city}
            r2 = {"record_id": f"AN_{i}_B", "hospital": "H_Z", "name": f"{fn} {ln}", "phone": ph2, "age": age + rng.choice([0, 1, 2]), "gender": g, "address": city}
        elif fam == 1:
            # Identical name, same age, DIFFERENT gender (contradictory!)
            g2 = "F" if g == "M" else "M"
            r1 = {"record_id": f"AN_{i}_A", "hospital": "H_X", "name": f"{fn} {ln}", "phone": ph1, "age": age, "gender": g, "address": city}
            r2 = {"record_id": f"AN_{i}_B", "hospital": "H_Z", "name": f"{fn} {ln}", "phone": None, "age": age, "gender": g2, "address": city}
        elif fam == 2:
            # Unrelated patients with identical name, close age (1 yr), missing phone, DIFFERENT city
            r1 = {"record_id": f"AN_{i}_A", "hospital": "H_X", "name": f"{fn} {ln}", "phone": ph1, "age": age, "gender": g, "address": city}
            r2 = {"record_id": f"AN_{i}_B", "hospital": "H_Z", "name": f"{fn} {ln}", "phone": None, "age": age + 1, "gender": g, "address": city2}
        else:
            # Hindi vs English different people with similar age & city, different phone
            _, ln2, _, _ = rng.choice([x for x in AUDIT_NAMES_PAIR if x[1] != ln])
            r1 = {"record_id": f"AN_{i}_A", "hospital": "H_X", "name": f"{fn_hi} {ln_hi}", "phone": ph1, "age": age, "gender": g, "address": city}
            r2 = {"record_id": f"AN_{i}_B", "hospital": "H_Z", "name": f"{fn} {ln2}", "phone": ph2, "age": age + 1, "gender": g, "address": city}
        pairs.append({"pair_id": f"AN_{i:04d}", "label": 0, "family": f"neg_{fam}", "record_a": r1, "record_b": r2})

    return pairs


def run_final_audit() -> None:
    train_pairs = generate_linkage_dataset(seed=2026)
    train_names = {p["record_a"]["name"] for p in train_pairs} | {p["record_b"]["name"] for p in train_pairs}

    audit_pairs = generate_5000_audit_pairs(seed=9001)
    audit_names = {p["record_a"]["name"] for p in audit_pairs} | {p["record_b"]["name"] for p in audit_pairs}
    overlap = train_names & audit_names

    # Duplicate pair signature check
    sigs = {
        (p["record_a"]["name"], p["record_b"]["name"], p["record_a"]["phone"], p["record_b"]["phone"], p["record_a"]["age"], p["record_b"]["age"])
        for p in audit_pairs
    }

    bundle = joblib.load(ROOT / "backend" / "artifacts" / "linkage_model.joblib")
    model = bundle["model"]
    thresh = float(bundle["high_threshold"])

    X_audit = np.array([_extract_linkage_features(p) for p in audit_pairs], dtype=np.float32)
    y_audit = np.array([p["label"] for p in audit_pairs], dtype=np.int32)

    t0 = time.perf_counter()
    probs = model.predict_proba(X_audit)[:, 1]
    preds = (probs >= thresh).astype(int)
    total_ms = (time.perf_counter() - t0) * 1000.0

    cm = confusion_matrix(y_audit, preds)
    tn, fp, fn, tp = int(cm[0, 0]), int(cm[0, 1]), int(cm[1, 0]), int(cm[1, 1])

    fp_samples = []
    fn_samples = []
    for p, yt, yp, pr in zip(audit_pairs, y_audit, preds, probs):
        if yt == 0 and yp == 1 and len(fp_samples) < 3:
            fp_samples.append({"pair_id": p["pair_id"], "family": p["family"], "prob": round(float(pr), 3), "a": p["record_a"], "b": p["record_b"]})
        if yt == 1 and yp == 0 and len(fn_samples) < 3:
            fn_samples.append({"pair_id": p["pair_id"], "family": p["family"], "prob": round(float(pr), 3), "a": p["record_a"], "b": p["record_b"]})

    report = {
        "audit_pairs_total": len(audit_pairs),
        "unique_pair_signatures": len(sigs),
        "train_audit_name_overlap_count": len(overlap),
        "frozen_model_type": type(model).__name__,
        "threshold": thresh,
        "precision": round(float(precision_score(y_audit, preds)), 4),
        "recall": round(float(recall_score(y_audit, preds)), 4),
        "f1_score": round(float(f1_score(y_audit, preds)), 4),
        "confusion_matrix": cm.tolist(),
        "false_positives": fp,
        "false_negatives": fn,
        "inference_total_ms": round(total_ms, 2),
        "inference_per_pair_ms": round(total_ms / len(audit_pairs), 5),
        "fp_samples": fp_samples,
        "fn_samples": fn_samples,
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    run_final_audit()

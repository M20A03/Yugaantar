"""Skeptical independent audit of frozen MediShield V2 & V3 linkage models.

Does NOT retrain or modify any model artifact.
Runs:
1. Feature ablation on sealed 5,000 pairs (phone, age/dob, name, address, contradictory)
2. 240 independent adversarial pairs (shared family phone, data-entry age error,
   ambiguous identical-observable-attribute pairs, contradictory pairs)
3. Direct V2 vs V3 comparison on the exact same 240 adversarial pairs
4. Complete pipeline latency (feature extraction + model prediction)
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

from app.services.record_linkage.features import FEATURE_NAMES, extract_pair_features  # noqa: E402
from generate_datasets_v3 import generate_v3_splits  # noqa: E402
from train_and_evaluate import _extract_linkage_features as extract_v2_features  # noqa: E402


def build_240_adversarial_pairs(seed: int = 2027) -> List[Dict[str, Any]]:
    """Completely independent generation logic (NOT using _make_pairs)."""
    rng = random.Random(seed)
    pairs: List[Dict[str, Any]] = []
    names = [
        ("Omkar", "Kulkarni", "ओंकार", "कुलकर्णी"),
        ("Tejas", "Gadgil", "तेजस", "गाडगीळ"),
        ("Gauri", "Bhave", "गौरी", "भावे"),
        ("Nikhil", "Sathe", "निखिल", "साठे"),
        ("Mrunal", "Kelkar", "मृणाल", "केळकर"),
        ("Aniruddha", "Joglekar", "अनिरुद्ध", "जोगळेकर"),
    ]
    cities = ["Solapur", "Kolhapur", "Amravati", "Aurangabad"]

    # 1. 60 hard positive matches (age entry error >5, 2-digit phone typo, missing phone+DOB)
    for i in range(60):
        fn, ln, fnh, lnh = names[i % len(names)]
        ph = f"98{rng.randint(10000000, 99999999)}"
        age = rng.randint(28, 65)
        g = "M" if i % 2 == 0 else "F"
        city = cities[i % len(cities)]
        if i < 20:
            # Data-entry age typo (off by 7 years!) + matching phone & name
            r1 = {"record_id": f"ADV_P{i}_A", "hospital": "H1", "name": f"{fn} {ln}", "phone": ph, "age": age, "gender": g, "address": city}
            r2 = {"record_id": f"ADV_P{i}_B", "hospital": "H2", "name": f"{fn} {ln}", "phone": ph, "age": age + 7, "gender": g, "address": city}
        elif i < 40:
            # 2-digit phone typo + Hindi-English transliteration
            ph2 = ph[:-2] + "00"
            r1 = {"record_id": f"ADV_P{i}_A", "hospital": "H1", "name": f"{fnh} {lnh}", "phone": ph, "age": age, "gender": g, "address": city}
            r2 = {"record_id": f"ADV_P{i}_B", "hospital": "H2", "name": f"{fn} {ln}", "phone": ph2, "age": age, "gender": g, "address": city}
        else:
            # Missing phone & missing DOB, only name + age + gender + city
            r1 = {"record_id": f"ADV_P{i}_A", "hospital": "H1", "name": f"{fn} {ln}", "phone": ph, "age": age, "gender": g, "address": city}
            r2 = {"record_id": f"ADV_P{i}_B", "hospital": "H2", "name": f"{fn} {ln}", "phone": None, "age": age, "gender": g, "address": city}
        pairs.append({"pair_id": f"ADV_P_{i:03d}", "label": 1, "group": "hard_positive", "record_a": r1, "record_b": r2})

    # 2. 60 shared family phone negatives (same phone, same last name, same city, same gender!)
    for i in range(60):
        fn1, ln, _, _ = names[i % len(names)]
        fn2, _, _, _ = names[(i + 1) % len(names)]
        ph = f"97{rng.randint(10000000, 99999999)}"
        age = rng.randint(25, 50)
        city = cities[i % len(cities)]
        r1 = {"record_id": f"ADV_F{i}_A", "hospital": "H1", "name": f"{fn1} {ln}", "phone": ph, "age": age, "gender": "M", "address": city}
        r2 = {"record_id": f"ADV_F{i}_B", "hospital": "H2", "name": f"{fn2} {ln}", "phone": ph, "age": age + 2, "gender": "M", "address": city}
        pairs.append({"pair_id": f"ADV_F_{i:03d}", "label": 0, "group": "shared_family_phone", "record_a": r1, "record_b": r2})

    # 3. 60 genuinely ambiguous negatives (different patients, IDENTICAL observable name/age/gender/city, missing phone!)
    for i in range(60):
        fn, ln, _, _ = names[i % len(names)]
        age = rng.randint(30, 60)
        city = cities[i % len(cities)]
        ph = f"96{rng.randint(10000000, 99999999)}"
        r1 = {"record_id": f"ADV_A{i}_A", "hospital": "H1", "name": f"{fn} {ln}", "phone": ph, "age": age, "gender": "F", "address": city}
        r2 = {"record_id": f"ADV_A{i}_B", "hospital": "H3", "name": f"{fn} {ln}", "phone": None, "age": age, "gender": "F", "address": city}
        pairs.append({"pair_id": f"ADV_A_{i:03d}", "label": 0, "group": "ambiguous_identical_attrs", "record_a": r1, "record_b": r2})

    # 4. 60 contradictory negatives (identical name & age, different phone)
    for i in range(60):
        fn, ln, _, _ = names[i % len(names)]
        age = rng.randint(30, 60)
        city = cities[i % len(cities)]
        ph1 = f"95{rng.randint(10000000, 99999999)}"
        ph2 = f"74{rng.randint(10000000, 99999999)}"
        r1 = {"record_id": f"ADV_C{i}_A", "hospital": "H1", "name": f"{fn} {ln}", "phone": ph1, "age": age, "gender": "M", "address": city}
        r2 = {"record_id": f"ADV_C{i}_B", "hospital": "H3", "name": f"{fn} {ln}", "phone": ph2, "age": age, "gender": "M", "address": city}
        pairs.append({"pair_id": f"ADV_C_{i:03d}", "label": 0, "group": "contradictory_phone", "record_a": r1, "record_b": r2})

    return pairs


def _eval_3stage(probs: np.ndarray, y: np.ndarray, hi: float, rev: float) -> Dict[str, Any]:
    auto_pos = probs >= hi
    review = (probs >= rev) & (probs < hi)
    tp = int(np.sum(auto_pos & (y == 1)))
    fp = int(np.sum(auto_pos & (y == 0)))
    fn = int(np.sum((~auto_pos) & (y == 1)))
    tn = int(np.sum((~auto_pos) & (y == 0)))
    prec = tp / (tp + fp) if (tp + fp) else 1.0
    rec = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = (2 * prec * rec / (prec + rec)) if (prec + rec) else 0.0
    return {
        "auto_precision": round(prec, 4),
        "auto_recall": round(rec, 4),
        "auto_f1": round(f1, 4),
        "fp": fp,
        "fn": fn,
        "tp": tp,
        "tn": tn,
        "review_count": int(np.sum(review)),
        "review_rate": round(float(np.mean(review)), 4),
    }


def run_audit() -> None:
    v2_bundle = joblib.load(ROOT / "backend" / "artifacts" / "linkage_model.joblib")
    v3_bundle = joblib.load(ROOT / "backend" / "artifacts" / "linkage_model_v3.joblib")

    v2_m, v2_hi, v2_rev = v2_bundle["model"], float(v2_bundle["high_threshold"]), float(v2_bundle["review_threshold"])
    v3_m, v3_hi, v3_rev = v3_bundle["model"], float(v3_bundle["high_threshold"]), float(v3_bundle["review_threshold"])

    # 1. Feature Ablation on V3 Sealed 5,000 pairs
    _, _, _, sealed = generate_v3_splits()
    X_sc = np.array([extract_pair_features(p["record_a"], p["record_b"]) for p in sealed], dtype=np.float32)
    y_sc = np.array([p["label"] for p in sealed], dtype=np.int32)

    ablation_groups = {
        "none (full_model)": [],
        "no_phone": [6, 7, 8],
        "no_age_dob": [9, 10, 11],
        "no_name": [0, 1, 2, 3, 4, 5],
        "no_address": [12],
        "no_contradictory": [15],
    }
    ablation_results: Dict[str, Any] = {}
    for gname, cols in ablation_groups.items():
        X_ab = X_sc.copy()
        if cols:
            X_ab[:, cols] = 0.0
        probs = v3_m.predict_proba(X_ab)[:, 1]
        ablation_results[gname] = _eval_3stage(probs, y_sc, v3_hi, v3_rev)

    # 2. Evaluate V2 vs V3 on 240 Independent Adversarial Pairs + Complete Pipeline Latency
    adv = build_240_adversarial_pairs(seed=2027)
    y_adv = np.array([p["label"] for p in adv], dtype=np.int32)

    t0 = time.perf_counter()
    X_adv_v2 = np.array([extract_v2_features(p) for p in adv], dtype=np.float32)
    v2_probs = v2_m.predict_proba(X_adv_v2)[:, 1]
    v2_total_ms = (time.perf_counter() - t0) * 1000.0

    t1 = time.perf_counter()
    X_adv_v3 = np.array([extract_pair_features(p["record_a"], p["record_b"]) for p in adv], dtype=np.float32)
    v3_probs = v3_m.predict_proba(X_adv_v3)[:, 1]
    v3_total_ms = (time.perf_counter() - t1) * 1000.0

    # Per-group breakdown for V3
    group_breakdown: Dict[str, Any] = {}
    for grp in ("hard_positive", "shared_family_phone", "ambiguous_identical_attrs", "contradictory_phone"):
        mask = np.array([p["group"] == grp for p in adv])
        g_probs = v3_probs[mask]
        group_breakdown[grp] = {
            "count": int(np.sum(mask)),
            "auto_match": int(np.sum(g_probs >= v3_hi)),
            "human_review": int(np.sum((g_probs >= v3_rev) & (g_probs < v3_hi))),
            "non_match": int(np.sum(g_probs < v3_rev)),
        }

    out = {
        "sealed_5000_ablation": ablation_results,
        "adversarial_240_v2": {**_eval_3stage(v2_probs, y_adv, v2_hi, v2_rev), "complete_pipeline_ms": round(v2_total_ms, 2)},
        "adversarial_240_v3": {**_eval_3stage(v3_probs, y_adv, v3_hi, v3_rev), "complete_pipeline_ms": round(v3_total_ms, 2)},
        "adversarial_240_v3_by_group": group_breakdown,
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    run_audit()

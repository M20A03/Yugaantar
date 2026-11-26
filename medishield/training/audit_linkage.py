"""Independent audit of MediShield Record Linkage training, splits, and generalization.

Preserves existing backend/artifacts/*.joblib untouched.
Checks:
1. Sequential vs. stratified class distributions
2. Identity/name overlap & synthetic separability
3. Stratified, patient-disjoint validation learning curve (never touching test set)
4. Fresh independent hard challenge dataset (2,000 pairs) evaluation
"""

import json
import random
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List

import joblib
import numpy as np
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "backend"))
sys.path.insert(0, str(ROOT / "training"))

from generate_datasets import generate_linkage_dataset, group_split  # noqa: E402
from train_and_evaluate import _extract_linkage_features  # noqa: E402


CHALLENGE_FIRST = [
    "Harish", "Suresh", "Mahesh", "Ramesh", "Ganesh", "Lokesh", "Dinesh", "Naresh",
    "Savita", "Anita", "Babita", "Mamta", "Geeta", "Seema", "Rekha", "Lata",
]
CHALLENGE_LAST = [
    "Shukla", "Dwivedi", "Chaturvedi", "Trivedi", "Upadhyay", "Dubey", "Pathak", "Ojha",
    "Kamble", "Pawar", "Shinde", "Jadhav", "Gaikwad", "More", "Sawant", "Chavan",
]
CHALLENGE_CITIES = ["Nagpur", "Nashik", "Varanasi", "Kanpur", "Surat", "Vadodara", "Bhopal", "Patna"]


def generate_hard_challenge_set(n_pairs: int = 2000, seed: int = 7777) -> List[Dict[str, Any]]:
    """Fresh, unseen challenge set with overlapping ages and noisy/missing phones."""
    rng = random.Random(seed)
    pairs: List[Dict[str, Any]] = []
    half = n_pairs // 2

    # 1,000 difficult positive matches (noisy phone, missing phone, age off by 1-3, swapped name)
    for i in range(half):
        fn, ln = rng.choice(CHALLENGE_FIRST), rng.choice(CHALLENGE_LAST)
        ph = f"9{rng.randint(100000000, 999999999)}"
        age = rng.randint(25, 70)
        g = rng.choice(["M", "F"])
        city = rng.choice(CHALLENGE_CITIES)
        mode = i % 4
        if mode == 0:
            # 1-digit phone typo + exact name + age diff 1
            ph2 = ph[:-1] + str((int(ph[-1]) + 1) % 10)
            r1 = {"record_id": f"CP_{i}_A", "hospital": "H1", "name": f"{fn} {ln}", "phone": ph, "age": age, "gender": g, "address": city}
            r2 = {"record_id": f"CP_{i}_B", "hospital": "H2", "name": f"{fn} {ln}", "phone": ph2, "age": age + 1, "gender": g, "address": city}
        elif mode == 1:
            # Missing phone on one side, matching name + city + age diff 2
            r1 = {"record_id": f"CP_{i}_A", "hospital": "H1", "name": f"{fn} {ln}", "phone": ph, "age": age, "gender": g, "address": city}
            r2 = {"record_id": f"CP_{i}_B", "hospital": "H2", "name": f"{fn[:3]}. {ln}", "phone": None, "age": age + 2, "gender": g, "address": city}
        elif mode == 2:
            # Name order swapped ("Shukla Harish") + matching phone
            r1 = {"record_id": f"CP_{i}_A", "hospital": "H1", "name": f"{fn} {ln}", "phone": ph, "age": age, "gender": g, "address": city}
            r2 = {"record_id": f"CP_{i}_B", "hospital": "H2", "name": f"{ln} {fn}", "phone": f"+91 {ph}", "age": age, "gender": g, "address": None}
        else:
            # Initial + last name + matching phone + age diff 3
            r1 = {"record_id": f"CP_{i}_A", "hospital": "H1", "name": f"{fn} {ln}", "phone": ph, "age": age, "gender": g, "address": city}
            r2 = {"record_id": f"CP_{i}_B", "hospital": "H2", "name": f"{fn[0]} {ln}", "phone": ph, "age": age + 3, "gender": g, "address": city}
        pairs.append({"pair_id": f"CP_{i:04d}", "label": 1, "mode": f"pos_{mode}", "record_a": r1, "record_b": r2})

    # 1,000 difficult negative pairs (same name, SAME age within 0-2 yrs, same gender, same city!)
    for i in range(half):
        fn, ln = rng.choice(CHALLENGE_FIRST), rng.choice(CHALLENGE_LAST)
        age = rng.randint(25, 70)
        g = rng.choice(["M", "F"])
        city = rng.choice(CHALLENGE_CITIES)
        ph1 = f"9{rng.randint(100000000, 999999999)}"
        ph2 = f"8{rng.randint(100000000, 999999999)}"
        if i % 2 == 0:
            # Different phone, same name, same age, same city
            r1 = {"record_id": f"CN_{i}_A", "hospital": "H1", "name": f"{fn} {ln}", "phone": ph1, "age": age, "gender": g, "address": city}
            r2 = {"record_id": f"CN_{i}_B", "hospital": "H3", "name": f"{fn} {ln}", "phone": ph2, "age": age + rng.choice([0, 1, 2]), "gender": g, "address": city}
        else:
            # Missing phone on one side, different city, same name & age (twins/namesakes)
            city2 = rng.choice([c for c in CHALLENGE_CITIES if c != city])
            r1 = {"record_id": f"CN_{i}_A", "hospital": "H1", "name": f"{fn} {ln}", "phone": ph1, "age": age, "gender": g, "address": city}
            r2 = {"record_id": f"CN_{i}_B", "hospital": "H3", "name": f"{fn} {ln}", "phone": None, "age": age + 1, "gender": g, "address": city2}
        pairs.append({"pair_id": f"CN_{i:04d}", "label": 0, "mode": f"neg_{i%2}", "record_a": r1, "record_b": r2})

    return pairs


def run_audit() -> None:
    link_all = generate_linkage_dataset(seed=2026)
    l_train, l_val, l_test = group_split(link_all, lambda x: x["group_id"], seed=2026)

    # 1. Sequential class distribution check (explains why 1k & 10k gave 0.0!)
    seq_dist = {
        n: dict(Counter(p["label"] for p in l_train[:n]))
        for n in (1000, 10000, 25000, len(l_train))
    }

    # 2. Identity/name overlap check between train and test
    train_names = {p["record_a"]["name"] for p in l_train} | {p["record_b"]["name"] for p in l_train}
    test_names = {p["record_a"]["name"] for p in l_test} | {p["record_b"]["name"] for p in l_test}
    name_overlap_pct = round(len(train_names & test_names) / max(1, len(test_names)) * 100, 1)

    # 3. Stratified, patient-disjoint validation learning curve (never touching test set!)
    rng = random.Random(42)
    pos_groups = sorted({p["group_id"] for p in l_train if p["label"] == 1})
    neg_groups = sorted({p["group_id"] for p in l_train if p["label"] == 0})
    rng.shuffle(pos_groups)
    rng.shuffle(neg_groups)

    X_val = np.array([_extract_linkage_features(p) for p in l_val], dtype=np.float32)
    y_val = np.array([p["label"] for p in l_val], dtype=np.int32)

    val_learning_curve = []
    for n_samples in (1000, 5000, 10000, 25000, len(l_train)):
        half_g = max(1, n_samples // 2)
        chosen_g = set(pos_groups[:half_g]) | set(neg_groups[:half_g])
        sub = [p for p in l_train if p["group_id"] in chosen_g]
        X_sub = np.array([_extract_linkage_features(p) for p in sub], dtype=np.float32)
        y_sub = np.array([p["label"] for p in sub], dtype=np.int32)
        clf = HistGradientBoostingClassifier(max_iter=80, max_depth=6, random_state=42)
        clf.fit(X_sub, y_sub)
        vp = clf.predict(X_val)
        val_learning_curve.append({
            "train_samples": len(sub),
            "class_counts": dict(Counter(int(y) for y in y_sub)),
            "val_precision": round(float(precision_score(y_val, vp)), 4),
            "val_recall": round(float(recall_score(y_val, vp)), 4),
            "val_f1": round(float(f1_score(y_val, vp)), 4),
        })

    # 4. Evaluate existing preserved linkage_model.joblib on fresh 2,000-pair hard challenge set
    bundle = joblib.load(ROOT / "backend" / "artifacts" / "linkage_model.joblib")
    model = bundle["model"]
    thresh = float(bundle["high_threshold"])

    challenge = generate_hard_challenge_set(2000, seed=7777)
    X_ch = np.array([_extract_linkage_features(p) for p in challenge], dtype=np.float32)
    y_ch = np.array([p["label"] for p in challenge], dtype=np.int32)
    ch_probs = model.predict_proba(X_ch)[:, 1]
    ch_preds = (ch_probs >= thresh).astype(int)

    failures = []
    for p, yt, yp, pr in zip(challenge, y_ch, ch_preds, ch_probs):
        if yt != yp and len(failures) < 6:
            failures.append({
                "pair_id": p["pair_id"],
                "mode": p["mode"],
                "true_label": int(yt),
                "pred_label": int(yp),
                "prob": round(float(pr), 3),
                "record_a": p["record_a"],
                "record_b": p["record_b"],
            })

    out = {
        "sequential_train_class_distributions": seq_dist,
        "train_test_name_overlap_percent": name_overlap_pct,
        "stratified_validation_learning_curve": val_learning_curve,
        "independent_hard_challenge_2000": {
            "precision": round(float(precision_score(y_ch, ch_preds)), 4),
            "recall": round(float(recall_score(y_ch, ch_preds)), 4),
            "f1": round(float(f1_score(y_ch, ch_preds)), 4),
            "confusion_matrix": confusion_matrix(y_ch, ch_preds).tolist(),
            "sample_failures": failures,
        },
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    run_audit()

"""Offline CPU training, learning curves, threshold calibration, and artifact export.

Trains on 50,000 PII records + 50,000 linkage pairs (70/15/15 grouped splits)
and exports trusted .joblib artifacts + JSON evaluation reports.
"""

import json
import sys
import time
import tracemalloc
from pathlib import Path
from typing import Any, Dict, List, Tuple

import joblib
import numpy as np
from rapidfuzz import fuzz
from rapidfuzz.distance import JaroWinkler, Levenshtein
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score
from sklearn.pipeline import Pipeline

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "backend"))
sys.path.insert(0, str(ROOT / "training"))

from app.services.pii_detection.detector import MultilingualPIIDetector, normalize_text, transliterate_devanagari  # noqa: E402
from app.services.record_linkage.linker import _char_ngram_jaccard, _norm_name, _norm_phone, _soundex_token  # noqa: E402
from generate_datasets import generate_linkage_dataset, generate_pii_dataset, group_split  # noqa: E402


ARTIFACTS_DIR = ROOT / "backend" / "artifacts"
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)


def _extract_pii_windows(records: List[Dict[str, Any]]) -> Tuple[List[str], List[int]]:
    texts: List[str] = []
    labels: List[int] = []
    for rec in records:
        txt = rec["text"]
        for ent in rec["entities"]:
            s, e = ent["start"], ent["end"]
            win = txt[max(0, s - 24) : min(len(txt), e + 24)]
            texts.append(win)
            labels.append(1)
        for clin in rec["clinical_spans"]:
            idx = txt.lower().find(clin.lower())
            if idx != -1:
                win = txt[max(0, idx - 24) : min(len(txt), idx + len(clin) + 24)]
                texts.append(win)
                labels.append(0)
    return texts, labels


def _extract_linkage_features(pair: Dict[str, Any]) -> List[float]:
    ra, rb = pair["record_a"], pair["record_b"]
    na, nb = _norm_name(ra.get("name")), _norm_name(rb.get("name"))
    pa, pb = _norm_phone(ra.get("phone")), _norm_phone(rb.get("phone"))
    aa, ab = _norm_name(ra.get("address")), _norm_name(rb.get("address"))

    jw = JaroWinkler.normalized_similarity(na, nb) if (na and nb) else 0.0
    lev = Levenshtein.normalized_similarity(na, nb) if (na and nb) else 0.0
    tok = (fuzz.token_set_ratio(na, nb) / 100.0) if (na and nb) else 0.0
    ngram = _char_ngram_jaccard(na, nb, 3)

    sa = {_soundex_token(t) for t in na.split() if t}
    sb = {_soundex_token(t) for t in nb.split() if t}
    phonetic = (len(sa & sb) / max(1, len(sa | sb))) if (sa and sb) else 0.0

    age_a, age_b = ra.get("age"), rb.get("age")
    age_diff = abs(age_a - age_b) / 100.0 if (age_a is not None and age_b is not None) else 0.5
    missing_age = 1.0 if (age_a is None or age_b is None) else 0.0

    phone_sim = (1.0 if pa == pb else fuzz.ratio(pa, pb) / 100.0) if (pa and pb) else 0.0
    missing_phone = 1.0 if (not pa or not pb) else 0.0

    addr_sim = (fuzz.token_set_ratio(aa, ab) / 100.0) if (aa and ab) else 0.0

    contra_age = 1.0 if (age_a is not None and age_b is not None and abs(age_a - age_b) > 5) else 0.0
    contra_gender = 1.0 if (ra.get("gender") and rb.get("gender") and ra["gender"][:1].lower() != rb["gender"][:1].lower()) else 0.0
    contra_phone = 1.0 if (pa and pb and phone_sim < 0.60) else 0.0
    contradictory = max(contra_age, contra_gender, contra_phone)

    return [jw, lev, tok, ngram, phonetic, age_diff, phone_sim, addr_sim, missing_phone, missing_age, contradictory]


def train_and_evaluate() -> Dict[str, Any]:
    t_start = time.perf_counter()
    tracemalloc.start()

    print("Generating 50,000 PII records and 50,000 linkage pairs...")
    pii_all = generate_pii_dataset(20000, 15000, 15000, seed=2026)
    link_all = generate_linkage_dataset(seed=2026)

    p_train, p_val, p_test = group_split(pii_all, lambda x: x["group_id"], seed=2026)
    l_train, l_val, l_test = group_split(link_all, lambda x: x["group_id"], seed=2026)

    # --- PHASE 4: PII Context Models ---
    X_p_tr, y_p_tr = _extract_pii_windows(p_train)
    X_p_va, y_p_va = _extract_pii_windows(p_val)
    X_p_te, y_p_te = _extract_pii_windows(p_test)

    word_pipe = Pipeline([
        ("tfidf", TfidfVectorizer(analyzer="word", ngram_range=(1, 2), max_features=20000)),
        ("clf", LogisticRegression(C=2.0, max_iter=300)),
    ])
    char_pipe = Pipeline([
        ("tfidf", TfidfVectorizer(analyzer="char_wb", ngram_range=(2, 4), max_features=25000)),
        ("clf", LogisticRegression(C=2.0, max_iter=300)),
    ])

    word_pipe.fit(X_p_tr, y_p_tr)
    char_pipe.fit(X_p_tr, y_p_tr)

    w_val_f1 = f1_score(y_p_va, word_pipe.predict(X_p_va))
    c_val_f1 = f1_score(y_p_va, char_pipe.predict(X_p_va))
    best_pii_name, best_pii_model = ("char_tfidf_lr", char_pipe) if c_val_f1 >= w_val_f1 else ("word_tfidf_lr", word_pipe)

    pii_te_pred = best_pii_model.predict(X_p_te)
    pii_metrics = {
        "word_tfidf_val_f1": round(float(w_val_f1), 4),
        "char_tfidf_val_f1": round(float(c_val_f1), 4),
        "selected_model": best_pii_name,
        "test_precision": round(float(precision_score(y_p_te, pii_te_pred)), 4),
        "test_recall": round(float(recall_score(y_p_te, pii_te_pred)), 4),
        "test_f1": round(float(f1_score(y_p_te, pii_te_pred)), 4),
    }

    pii_path = ARTIFACTS_DIR / "pii_model.joblib"
    joblib.dump(best_pii_model, pii_path, compress=3)

    # --- Existing Hybrid Detector Evaluation on held-out test slice (1,500 records across langs) ---
    detector = MultilingualPIIDetector()
    per_lang_eval: Dict[str, Any] = {}
    latencies: List[float] = []
    for lang in ("en", "hi", "hinglish"):
        sub = [r for r in p_test if r["language"] == lang][:500]
        tp = fp = fn = leaks = exp_tot = 0
        for rec in sub:
            t0 = time.perf_counter()
            _, ents = detector.scan(rec["text"])
            latencies.append((time.perf_counter() - t0) * 1000.0)
            det_t = [e.text.lower() for e in ents]
            exps = [e["text"] for e in rec["entities"]]
            exp_tot += len(exps)
            matched = 0
            for ex in exps:
                if any(ex.lower() in d or d in ex.lower() for d in det_t):
                    matched += 1
                else:
                    fn += 1
            tp += matched
            fp += max(0, len(det_t) - matched)
        pr = tp / (tp + fp) if (tp + fp) else 1.0
        rc = tp / (tp + fn) if (tp + fn) else 1.0
        per_lang_eval[lang] = {
            "records_evaluated": len(sub),
            "precision": round(pr, 4),
            "recall": round(rc, 4),
            "f1": round(2 * pr * rc / (pr + rc), 4) if (pr + rc) else 0.0,
        }

    # --- PHASE 5: Record Linkage Models ---
    X_l_tr = np.array([_extract_linkage_features(p) for p in l_train], dtype=np.float32)
    y_l_tr = np.array([p["label"] for p in l_train], dtype=np.int32)
    X_l_va = np.array([_extract_linkage_features(p) for p in l_val], dtype=np.float32)
    y_l_va = np.array([p["label"] for p in l_val], dtype=np.int32)
    X_l_te = np.array([_extract_linkage_features(p) for p in l_test], dtype=np.float32)
    y_l_te = np.array([p["label"] for p in l_test], dtype=np.int32)

    link_candidates = {
        "logistic_regression": LogisticRegression(C=2.0, max_iter=300),
        "random_forest": RandomForestClassifier(n_estimators=80, max_depth=10, random_state=42, n_jobs=-1),
        "gradient_boosting": HistGradientBoostingClassifier(max_iter=100, max_depth=6, random_state=42),
    }

    val_scores: Dict[str, float] = {}
    for name, clf in link_candidates.items():
        clf.fit(X_l_tr, y_l_tr)
        val_scores[name] = round(float(f1_score(y_l_va, clf.predict(X_l_va))), 4)

    best_link_name = max(val_scores, key=lambda k: val_scores[k])
    best_link_clf = link_candidates[best_link_name]

    # Calibrate high-confidence & uncertain thresholds on validation set
    val_probs = best_link_clf.predict_proba(X_l_va)[:, 1]
    best_thresh = 0.80
    best_cal_f1 = -1.0
    for th in (0.65, 0.75, 0.80, 0.85, 0.90):
        f1_th = f1_score(y_l_va, (val_probs >= th).astype(int))
        if f1_th > best_cal_f1:
            best_cal_f1 = f1_th
            best_thresh = th

    te_probs = best_link_clf.predict_proba(X_l_te)[:, 1]
    te_preds = (te_probs >= best_thresh).astype(int)
    cm = confusion_matrix(y_l_te, te_preds).tolist()

    linkage_path = ARTIFACTS_DIR / "linkage_model.joblib"
    joblib.dump(
        {"model": best_link_clf, "high_threshold": best_thresh, "review_threshold": 0.50},
        linkage_path,
        compress=3,
    )

    # --- PHASE 6: Learning Curves (1k, 10k, 25k, 50k total dataset scale) ---
    learning_curve = []
    for n_samples in (1000, 10000, 25000, len(l_train)):
        idx = min(n_samples, len(X_l_tr))
        sub_clf = HistGradientBoostingClassifier(max_iter=80, max_depth=6, random_state=42)
        sub_clf.fit(X_l_tr[:idx], y_l_tr[:idx])
        sub_pred = (sub_clf.predict_proba(X_l_te)[:, 1] >= best_thresh).astype(int)
        learning_curve.append({
            "train_samples": idx,
            "test_precision": round(float(precision_score(y_l_te, sub_pred)), 4),
            "test_recall": round(float(recall_score(y_l_te, sub_pred)), 4),
            "test_f1": round(float(f1_score(y_l_te, sub_pred)), 4),
        })

    _, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    report = {
        "dataset_sizes": {"pii_records": len(pii_all), "linkage_pairs": len(link_all)},
        "pii_context_models": pii_metrics,
        "hybrid_detector_per_language_test": per_lang_eval,
        "linkage_models_val_f1": val_scores,
        "selected_linkage_model": best_link_name,
        "calibrated_high_threshold": best_thresh,
        "linkage_test_metrics": {
            "precision": round(float(precision_score(y_l_te, te_preds)), 4),
            "recall": round(float(recall_score(y_l_te, te_preds)), 4),
            "f1": round(float(f1_score(y_l_te, te_preds)), 4),
            "confusion_matrix": cm,
        },
        "learning_curve": learning_curve,
        "performance": {
            "avg_detector_latency_ms": round(float(np.mean(latencies)), 3),
            "worst_detector_latency_ms": round(float(np.max(latencies)), 3),
            "peak_traced_memory_mb": round(peak_mem / (1024 * 1024), 2),
            "total_training_seconds": round(time.perf_counter() - t_start, 2),
            "pii_model_size_kb": round(pii_path.stat().st_size / 1024, 1),
            "linkage_model_size_kb": round(linkage_path.stat().st_size / 1024, 1),
        },
    }
    metadata = {
        "pii_model": best_pii_name,
        "linkage_model": best_link_name,
        "high_threshold": best_thresh,
        "review_threshold": 0.50,
        "offline_only": True,
        "zero_llm": True,
    }
    (ARTIFACTS_DIR / "evaluation_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    (ARTIFACTS_DIR / "model_metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return report


if __name__ == "__main__":
    train_and_evaluate()

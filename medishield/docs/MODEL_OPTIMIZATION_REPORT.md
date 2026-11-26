# MediShield V3 Model Optimization & Evaluation Report

**Project:** MediShield — Healthcare Privacy Firewall (Track 3: Secret Wards)  
**Note:** All metrics below are measured on synthetic datasets generated offline; they do not claim clinical validation on real-world hospital production data.

---

## 1. Why the Initial 100% F1 Score Was Misleading
1. **Unshuffled Sequential Slicing:** In V2, `generate_linkage_dataset()` put all positive pairs first, causing `1k` and `10k` subsets to score `0.0` F1 before jumping to `1.0` at `25k`.
2. **Shortcut Separability:** Every negative pair in the V2 50k dataset had a large age gap (`>= 20` years) or a clearly mismatched phone, while `100%` of test names overlapped with training names.
3. **Partial Phone Flaw:** Using `fuzz.ratio < 0.60` on random 10-digit phones allowed unrelated patients (`neg_0`, `neg_3`) to pass without triggering contradictory evidence, causing **19 False Positives** on the historical 5,000-pair audit.

---

## 2. Progression Comparison Table

| Stage / Benchmark | Precision | Recall | F1 Score | False Positives | False Negatives | Notes |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Original Rule-Based Baseline (V1, 100 pairs)** | `0.0667` | `1.0000` | `0.1250` | `700` | `0` | Merged strangers sharing names |
| **V2 50k Validation (7,500 pairs)** | `1.0000` | `1.0000` | `1.0000` | `0` | `0` | Misleading due to name overlap & age shortcuts |
| **V2 Historical 5,000-Pair Challenge** | `0.9906` | `0.8000` | `0.8852` | `19` | `500` | Exposed partial-phone FPs & missing-phone FNs |
| **V3 Calibrated Validation (`7,500` pairs, 0 overlap)** | `1.0000` | `1.0000` | `1.0000` | `0` | `0` | `logistic_regression_calibrated`, Brier `0.0` |
| **V3 on Historical 5,000-Pair Challenge** | **`1.0000`** | `0.8000` | `0.8889` | **`0`** | `500` | Eliminated all **19** False Positives |
| **V3 on Fresh Sealed 5,000-Pair Challenge** | **`1.0000`** | **`1.0000`** | **`1.0000`** | **`0`** | **`0`** | `[[2500, 0], [0, 2500]]`, 0 identity overlap |

---

## 3. Model Comparison on V3 Validation (`7,500` pairs)

| Model | Val F1 | Brier Score | Size (KB) | Train Time | Val Predict Time |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **`logistic_regression_calibrated` (Selected)** | `1.0000` | `0.0000` | **`1.4 KB`** | `0.78 s` | `27.86 ms` |
| `hist_gradient_boosting` | `1.0000` | `0.0000` | `18.5 KB` | `0.51 s` | `12.11 ms` |
| `gradient_boosting` | `1.0000` | `0.0000` | `20.8 KB` | `1.39 s` | `9.13 ms` |
| `random_forest` | `1.0000` | `0.0000` | `34.3 KB` | `1.26 s` | `85.73 ms` |
| `fellegi_sunter_baseline` | `0.8571` | `0.1222` | `0.2 KB` | `0.00 s` | `0.50 ms` |

---

## 4. End-to-End Timing, Memory & PII Pipeline Audit
- **5,000-Pair Complete Linkage Time:** **`684.97 ms`** (`681.13 ms` feature extraction + `3.85 ms` model prediction; `1.83 ms` model load).
- **Single-Record PII Pipeline Latency (500 records):** Mean `2.063 ms`, Median `2.302 ms`, P95 `2.576 ms`, Max `26.12 ms`.
- **Peak Traced Memory:** `89.92 MB`.
- **PII Pipeline Per-Language (500 records):** English (`1.0` F1, `99.48%` fidelity), Hindi (`1.0` F1, `100%` fidelity), Hinglish (`1.0` F1, `99.16%` fidelity).

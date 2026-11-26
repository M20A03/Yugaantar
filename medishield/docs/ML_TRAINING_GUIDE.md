# MediShield ML Training Guide (Simple English for BCA Viva)

## 1. How the Datasets Were Created (`training/generate_datasets.py`)
- We generated **50,000 synthetic clinical records** (20,000 English, 15,000 Devanagari Hindi, 15,000 Hinglish) across registration notes, OPD/IPD notes, prescriptions, and discharge summaries.
- Ground-truth character offsets (`start`, `end`) were recorded **directly when building each synthetic sentence**—we never used our detector to label its own training data.
- We also generated **50,000 labeled record pairs** (15,000 matching, 15,000 hard-negatives with the same name but different age/phone, 10,000 missing-field pairs, and 10,000 multilingual/Devanagari-English pairs).
- Both datasets were split **70% Train / 15% Validation / 15% Test** grouped by `group_id` so the same synthetic patient family never leaks across splits.

## 2. Why Each Algorithm Was Selected
- **Character-level TF-IDF (`char_wb`, 2–4) + Logistic Regression (`pii_model.joblib`):** Looks at 2–4 letter chunks instead of whole words, so typos like `Pateint` or Hinglish spelling variations are still recognized. Runs in <2 ms on CPU.
- **HistGradientBoosting / Random Forest / Logistic Regression (`linkage_model.joblib`):** Uses 11 engineered features (Jaro-Winkler, Levenshtein, token similarity, 3-gram Jaccard, Soundex phonetic match, age difference, phone similarity, address similarity, missing-field flags, and contradictory-evidence flags) to classify pairs into **High-Confidence Match**, **Uncertain Review**, or **Non-Match**.

## 3. How Training & Backend Integration Work
1. Run `python training/train_and_evaluate.py` (locally or in `notebooks/MediShield_Advanced_Training.ipynb` on Google Colab CPU).
2. It trains all candidate models, selects the best on the validation set, calibrates thresholds, computes learning curves (`1k`, `10k`, `25k`, `50k`), and saves `pii_model.joblib` + `linkage_model.joblib` into `backend/artifacts/`.
3. At runtime, `detector.py` and `linker.py` load these local `.joblib` files **100% offline**—no internet, no Colab, and no LLM needed.

## 4. Pre-Event Training vs. Competition Submission
- Pre-event training happens offline in `training/` or Google Colab, producing compact `.joblib` files (< 2 MB total).
- At evaluation time, the backend and `main.py` CLI only load those trusted local `.joblib` artifacts offline. (Always confirm with hackathon organizers whether pre-trained classical ML weights are allowed under Track 3 rules.)

## 5. Possible Viva Questions on the ML Upgrade
1. **Why did you group splits by `group_id`?** To prevent the same synthetic patient or template from appearing in both training and test sets (data leakage).
2. **Why compare 1k, 10k, 25k, and 50k samples?** Learning curves prove whether more training data actually improves unseen test F1 or if the model has already plateaued.
3. **Why not auto-merge `uncertain_review` pairs?** Because merging two different patients in healthcare is dangerous; uncertain pairs should be reviewed by a human operator.

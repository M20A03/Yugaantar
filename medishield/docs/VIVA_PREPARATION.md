# MediShield — Viva Preparation Guide (Simple English)

**Project:** MediShield — Healthcare Privacy Firewall  
**Tagline:** Protecting Identities. Preserving Medical Intelligence.  
**Audience:** Beginner-friendly guide for BCA students preparing for hackathon demo & technical Q&A.

---

## 1. Explanation of Every Important Project File

- **`medishield/main.py` & `raksha.toml`**: The offline command-line runner. Judges or automated scripts can run `python main.py --input <folder> --output <folder>` with no internet. It reads `.csv`, `.tsv`, `.json`, and `.txt` files, cleans every record, and writes `sanitized/`, `report.json`, and `records.jsonl`.
- **`medishield/backend/app/main.py`**: Starts the FastAPI web server and allows our React frontend (`localhost:5173`) to talk to the Python backend (`localhost:8000`).
- **`medishield/backend/app/api/routes.py`**: Defines all API endpoints (`/health`, `/scan`, `/anonymize`, `/batch-process`, `/linkage/analyze`, `/risk/analyze`, `/fidelity/evaluate`, `/metrics`, `/evaluation/run`).
- **`medishield/backend/app/models/schemas.py`**: Uses Pydantic to check that every request and response has the exact right data types (strings, numbers, lists).
- **`medishield/backend/app/services/pii_detection/detector.py`**: The brain that finds personal information (names, phones, Aadhaar, PAN, emails, addresses, ages, hospital IDs) in English, Hindi (Devanagari), and Hinglish without using any LLM.
- **`medishield/backend/app/services/anonymization/anonymizer.py`**: Replaces detected PII using 5 strategies: Redaction, Masking, HMAC Pseudonymization, Generalization (age bands), and Suppression.
- **`medishield/backend/app/services/record_linkage/linker.py`**: Checks whether records from different hospitals belong to the same patient using Soundex blocking and `RapidFuzz` text similarity.
- **`medishield/backend/app/services/risk_analysis/risk_analyzer.py`**: Calculates *k*-anonymity and re-identification risk before and after cleaning.
- **`medishield/backend/app/services/medical_fidelity/fidelity.py`**: Verifies that diagnoses, medicines, dosages, symptoms, and vitals were NOT accidentally deleted.
- **`medishield/backend/app/services/storage/audit_db.py`**: Saves only safe, non-PII numbers (counts, fidelity score, latency) into SQLite. Never saves raw patient text.
- **`medishield/backend/app/services/evaluation/evaluator.py` & `tests/stress_eval.py`**: Runs automated benchmarks (including a 1,050-record synthetic stress test) to measure real Precision, Recall, F1, Leakage Rate, and Latency.
- **`medishield/frontend/src/App.tsx`**: The dark-themed React + TypeScript dashboard with 9 pages including the split-screen Record Scanner, Batch Upload, Risk Analysis, Record Linkage, Medical Fidelity, Audit Logs, and Evaluation Lab.

---

## 2. Explanation of Every Core Algorithm

1. **Unicode NFKC Normalization & Devanagari Transliteration:**
   - First we normalize weird Unicode characters (`NFKC`) so both `detector.py` and `anonymizer.py` work on the exact same character positions.
   - To compare Hindi names (`मोहम्मद आरिफ`) with English names (`Mohammad Arif`), we convert each Devanagari letter to Latin letters (`a`, `k`, `kh`, `m`, etc.) and normalize common spellings (`mohammad`, `mohammed`, `mohd`, `md` -> `mohd`).
2. **Hybrid PII Detection (Regex + Context Rules + Tiny ML):**
   - **Regex** catches structured IDs (Indian & international phone numbers, Aadhaar, PAN, ABHA, UHID/MRN, emails, dates, PIN codes).
   - **Context rules** catch names after labels (`Patient`, `Pateint`, `Pt.`, `Mareez`, `रोगी`), Hinglish honorifics (`Arif sahab`, `Meera ji`), and unstructured sentences (`Ananya Kulkarni presented with...`).
   - **Meaning disambiguation** checks `"C/O"` — `"C/O Ramesh"` is a relative (remove), while `"C/O fever"` is a medical complaint (keep). `"Dr. Rajesh Gupta"` is a doctor (keep).
   - **Tiny offline ML classifier** (`TfidfVectorizer` + `LogisticRegression` from `scikit-learn`) scores whether a text window looks like a patient identity or a medical phrase.
   - **Overlap resolution** keeps the longest, highest-confidence match when two rules overlap.
3. **HMAC-SHA256 Pseudonymization:**
   - Uses a secret key (`RAKSHA_SECRET`) + SHA-256 HMAC so the same patient gets the same fake ID (`[PATIENT_868679]`) across files, but attackers cannot reverse the hash back to the real name.
4. **Cross-Hospital Record Linkage (Blocking + RapidFuzz):**
   - Instead of comparing every record to every other record ($O(N^2)$), we group records by Soundex name codes, last 4 phone digits, and gender (**blocking**).
   - Then we compute **Jaro-Winkler** + **token-set similarity** on names, phone similarity, and age proximity.
   - **Hard negative guards:** If gender differs or age differs by more than 5 years, we reject the match so two strangers with the same name are not merged.
5. **k-Anonymity Risk Analysis:**
   - Groups records by quasi-identifiers (age, gender, location, diagnosis). If a group has size $k=1$, that person is unique and easy to re-identify. Generalizing age into 5-year bands (`45–49`) and locations into cities increases $k$ and lowers risk.

---

## 3. Complete Data Flow

1. **Input** (Text, CSV, TSV, or JSON in English/Hindi/Hinglish) arrives at `/anonymize`, `/batch-process`, or `main.py`.
2. **Normalization** converts text to NFKC Unicode and detects language (`en`, `hi`, `hinglish`, `mixed`).
3. **PII Detection** scans for direct & quasi-identifiers while protecting whitelisted medical terms (`Metformin 500 mg`, `130/85 mmHg`, `1-0-1`, `Type 2 Diabetes`).
4. **Anonymization** replaces detected spans with redactions, masks, age bands, or HMAC pseudonyms.
5. **Verification** runs Medical Fidelity (checking clinical terms survived) and Risk Analysis (comparing before vs. after risk).
6. **Output & Audit** returns the sanitized record + metrics, and stores only non-PII counts in SQLite.

---

## 4. Why Each Technology Was Selected

- **Python + FastAPI:** Fast to write, automatic input validation with Pydantic, and native access to Python NLP/ML libraries.
- **Regex + Custom Rules:** Deterministic, fast (< 2 ms per record), works 100% offline, and handles Indian formats (Aadhaar, PAN, Hinglish) that generic English models miss.
- **scikit-learn (TF-IDF + LogisticRegression):** Lightweight classical ML (~0.16 MB memory), trains in milliseconds, zero GPU or LLM needed.
- **RapidFuzz:** C++-backed fuzzy string matching (Jaro-Winkler & Levenshtein), much faster than pure Python `difflib`.
- **React + TypeScript + Tailwind CSS + Recharts:** Clean, type-safe enterprise dashboard with responsive split-screen scanner and real-time charts.
- **SQLite:** Built into Python, zero external database server needed, ideal for offline audit metadata.

---

## 5. Advantages & Disadvantages

**Advantages:**
- 100% offline, CPU-only, zero LLM cost or data leakage to cloud APIs.
- Very fast (~1.4 ms average per record, < 1 MB memory).
- Handles English, Devanagari Hindi, and Hinglish together.
- Preserves clinical data (100% medical fidelity on our synthetic benchmark).

**Disadvantages / Limitations:**
- Unseen free-text names without any prefix, honorific, or clinical verb (`"visited"`, `"presented"`) can still be missed because no large NER transformer is used.
- *k*-anonymity is a heuristic on the current batch, not a mathematical guarantee against external datasets.
- The official Track 3 Secret Wards starter kit/validator was not present in the workspace, and the updated 2-page PDF mentioned Zero-Knowledge Proofs (ZKPs), so exact official evaluation scripts could not be run.

---

## 6. 50 Technical Viva Questions & Simple Answers

1. **What is MediShield?** An offline, LLM-free privacy firewall that removes personal data from hospital records while keeping medical facts safe.
2. **Why did you avoid LLMs like GPT or Gemini?** Sending patient data to cloud APIs violates privacy, and Track 3 rules forbid LLMs and internet access.
3. **What is PII?** Personally Identifiable Information — anything that identifies a person (name, phone, Aadhaar, PAN, email, address).
4. **What is PHI?** Protected Health Information — PII combined with medical details.
5. **What is a quasi-identifier?** A field like age, gender, village, or visit date that cannot identify someone alone, but can identify them when combined.
6. **What is a linkage attack?** Matching an anonymized medical record with a public list (like a voter list) using age, gender, location, and stay length.
7. **What is *k*-anonymity?** A rule where every record looks identical to at least $k-1$ other records on quasi-identifiers.
8. **How does MediShield reduce quasi-identifier risk?** It groups ages into 5-year bands (`45–49`), generalizes addresses, and can suppress rare diagnoses.
9. **What is the difference between Redaction and Masking?** Redaction replaces text with a label (`[PHONE_REDACTED]`); masking hides middle characters (`98******10`).
10. **What is Pseudonymization?** Replacing a real name with a consistent fake ID (`[PATIENT_868679]`).
11. **Why use HMAC-SHA256 instead of plain SHA-256?** Plain SHA-256 can be guessed using a rainbow table of Indian names; HMAC requires a secret key (`RAKSHA_SECRET`).
12. **What is Unicode NFKC normalization?** A standard way to clean equivalent Unicode characters before scanning so offsets match.
13. **How do you handle Hindi (Devanagari) records?** Regex + Devanagari character ranges (`\u0900-\u097F`) + a Devanagari-to-Latin transliteration table.
14. **How do you handle Hinglish?** By matching Hinglish keywords (`umra`, `saal`, `pata`, `mareez`, `ji`, `sahab`) alongside English medical terms.
15. **How do you solve `"C/O Ramesh"` vs `"C/O fever"`?** A disambiguation list checks the word after `C/O`: clinical complaints (`fever`, `cough`, `pain`) are kept; person names are removed.
16. **Why do you keep `"Dr. Rajesh Gupta"`?** Doctor names are clinical metadata, not patient PII, so a doctor-prefix check protects them.
17. **Why do you keep `"1-0-1"` and `"500 mg"`?** They are medicine dosages; our regex and unit-suffix check prevent them from being treated as phone numbers.
18. **What is Precision?** Out of everything we flagged as PII, how much was actually PII ($\frac{TP}{TP+FP}$).
19. **What is Recall?** Out of all real PII in the text, how much did we catch ($\frac{TP}{TP+FN}$).
20. **What is F1 Score?** The harmonic mean of Precision and Recall ($2 \cdot \frac{P \cdot R}{P+R}$).
21. **What is PII Leakage Rate?** The percentage of real PII items that survived into the sanitized output.
22. **What is False Positive Rate?** How often normal medical text is wrongly flagged as PII.
23. **Why did we use `RapidFuzz`?** For fast C++-optimized Jaro-Winkler and token-set string matching in record linkage.
24. **What is Jaro-Winkler similarity?** A string similarity score (0 to 1) that gives extra weight to matching prefixes, great for spelling variations.
25. **What is Soundex blocking?** Converting names into phonetic codes so we only compare records that sound similar, avoiding slow $O(N^2)$ comparisons.
26. **How do you prevent merging two different people with the same name?** We require at least 2 agreeing fields (or strong phone match) and block links if gender differs or age differs by > 5 years.
27. **What is TF-IDF?** Term Frequency–Inverse Document Frequency — turns words into numbers based on how important they are in a text.
28. **What is Logistic Regression doing in `detector.py`?** It gives a probability score (0 to 1) for whether a text window is a person context or a medical context.
29. **What is `overlap resolution`?** If two rules match overlapping text (e.g., `"Rahul"` and `"Rahul Sharma"`), we keep the longer, higher-confidence span.
30. **What is Medical Data Fidelity?** A score measuring how many clinical items (diagnoses, drugs, dosages, vitals) survived anonymization.
31. **What is FastAPI?** A modern, fast Python web framework that uses type hints for automatic validation and Swagger docs.
32. **What is Pydantic?** A Python library that validates JSON request/response schemas and catches bad inputs early.
33. **What is CORS and why did you configure it?** Cross-Origin Resource Sharing lets the React app (`5173`) safely call FastAPI (`8000`) locally.
34. **What does SQLite store in MediShield?** Only sanitized counts, fidelity scores, risk scores, and latencies — never raw patient text.
35. **Why is raw PII never logged?** Because if logs are breached, patient privacy is compromised.
36. **What is `raksha.toml`?** The configuration file telling the offline evaluator how to install dependencies and run `main.py`.
37. **What are the 3 outputs of `main.py`?** `sanitized/` (cleaned files), `report.json` (SHA-256 hashes & counts), and `records.jsonl` (record-to-pseudonym map).
38. **Why does `report.json` use SHA-256 of input files instead of filenames?** Because filenames themselves might contain patient names!
39. **What happens if `main.py` sees an unsupported file like `.exe` or `.pdf`?** It quarantines it (`status: "quarantined"`) instead of copying it out uncleaned.
40. **Why did `main.py` originally report 5 records instead of 7?** It counted a 2-item JSON list as 1 record and a 2-line TXT file as 1 record; we fixed it to count per-record.
41. **What is `Vite`?** A fast frontend build tool and dev server for React + TypeScript.
42. **Why use `TypeScript` instead of plain JavaScript?** TypeScript catches data shape mismatches at compile time before the app runs.
43. **What is `Recharts`?** A React charting library used on the Overview page for PII category and language charts.
44. **What is `pytest`?** Python's testing framework used to run our 6 automated unit/integration tests.
45. **How fast is MediShield per record?** ~1.4 ms on average on CPU in our 1,050-record stress test.
46. **How much memory does the stress test use?** ~0.16 MB traced Python memory during the 1,050-record run.
47. **What is the difference between `GET` and `POST` in your API?** `GET` reads status/metrics (`/health`, `/metrics`); `POST` sends data to process (`/scan`, `/anonymize`).
48. **What is `FormData` used for?** Uploading `.csv`, `.json`, and `.txt` files in `/batch-process`.
49. **What is the `10 MB` limit in `routes.py`?** A security guard to prevent oversized file uploads from crashing memory (DoS protection).
50. **What is your honest disclaimer on Risk Analysis?** It is a batch-level heuristic, not a formal guarantee against external auxiliary datasets.

---

## 7. 10 Difficult Questions Judges Might Ask (With Answers)

1. **"If `RAKSHA_SECRET` is reused across two separate hospitals, couldn't an attacker link pseudonyms across datasets?"**  
   *Answer:* Yes—deterministic HMAC allows linking records *within* the authorized scope of that key. In production, each data-sharing release should use a **per-release or per-study salted key** so pseudonyms cannot be correlated across unrelated releases.
2. **"Why did your 1,050-record stress test still show a 3.66% leakage rate when Recall was 1.0?"**  
   *Answer:* Because of our strict substring check in the benchmark: for example, when an age like `50` or `30` is generalized or matches digits inside `500 mg` or `130/85`, a naive substring check flags it, and some overlapping multi-token spans need exact boundary checks. We report the raw number honestly rather than hiding it.
3. **"Why was your Record Linkage precision only 25.8% on the stress test?"**  
   *Answer:* Our stress test intentionally created 50 pairs of *different* patients who shared the exact same name, same gender, and *missing* phone numbers. Even after adding a hard age-gap guard (`diff > 5`), records that wrapped around to the same age with no phone number cannot be separated by name+age alone—showing why automated linkage should flag low-evidence pairs for human review rather than auto-merging.
4. **"How do you handle a completely unseen Indian name in the middle of a sentence with no prefix like `Patient` or `ji`?"**  
   *Answer:* Right now, `detector.py` catches prefixed names, Hinglish honorifics, `C/O` relatives, and sentence-initial clinical subjects (`"X presented with..."`). Truly unprefixed mid-sentence names without an LLM/large NER model are a known limitation of our lightweight <50M-param rule+ML design.
5. **"Your updated 2-page hackathon PDF mentioned Zero-Knowledge Proofs for Track 3. Does MediShield have ZKPs?"**  
   *Answer:* No—MediShield implements the full offline English/Hindi/Hinglish PII Firewall & Record Linkage specification. Because the updated 2-page PDF did not include a ZKP detail tab or starter kit, we documented that gap honestly rather than faking a ZKP module.
6. **"What happens if an attacker puts a patient's name inside a CSV column header or JSON key?"**  
   *Answer:* In `routes.py` and `main.py`, string values are scanned, but JSON keys and CSV headers are currently preserved as-is—that is an area we identified in our code audit for future hardening.
7. **"Can your system handle broken UTF-8 or Latin-1 legacy hospital CSVs?"**  
   *Answer:* Yes, `main.py` tries strict UTF-8 first and falls back to `latin-1` with replacement so legacy exports don't crash the pipeline.
8. **"How do you ensure `Dr. Sharma` is not redacted while `Patient Rahul Sharma` is?"**  
   *Answer:* `_valid_person_name()` checks the 8 characters before a match for `Dr.` / `Doctor` / `डॉ.` and skips doctor names.
9. **"Why didn't you use a 400MB spaCy transformer or BERT model?"**  
   *Answer:* Track 3 rules forbid LLMs and large pretrained transformers (>50M parameters) and enforce strict offline CPU/RAM limits. Our hybrid engine runs in ~1.4 ms with <1 MB traced memory.
10. **"What if a patient has a rare disease like `Autoimmune Vasculitis`—doesn't that single them out even after removing their name?"**  
    *Answer:* Yes. That's why `risk_analyzer.py` includes a `suppress_rare` option that suppresses diagnoses appearing fewer than `rare_threshold` times in a batch.

---

## 8. Live Demonstration Instructions

1. **Start Backend:**
   ```bash
   cd medishield/backend
   ./.venv/bin/uvicorn app.main:app --host 127.0.0.1 --port 8000
   ```
2. **Start Frontend:**
   ```bash
   cd medishield/frontend
   npm run dev
   ```
3. **Demo Flow in Browser (`http://localhost:5173`):**
   - Open **Record Scanner** -> click **Load Hinglish Sample** -> click **Anonymize** -> show highlighted PII on left, sanitized output + `45–49` age band + preserved `Type 2 Diabetes` / `Metformin 500 mg` / `130/85 mmHg` on right.
   - Switch to **Load Hindi Sample** -> show Devanagari detection.
   - Open **Record Linkage** -> click **Analyze Cross-Hospital Linkage** -> show `Mohammad Arif`, `मोहम्मद आरिफ`, and `Md. Arif` linked into one pseudonymized cluster.
   - Open **Evaluation Lab** -> click **Run Evaluation Suite** -> show live Precision, Recall, F1, Leakage, and Latency.
   - Open **Overview** -> show real metrics updated from your live actions.

---

## 9. 3-Minute Project Presentation Script

> **0:00 – 0:40 (Problem):**  
> "Hello judges. Indian hospitals store patient records across messy CSVs, JSONs, and notes mixing English, Hindi, and Hinglish. Standard PII tools fail here—they miss Devanagari names like *मोहम्मद आरिफ*, confuse *C/O Ramesh* with *C/O fever*, and accidentally redact medicine doses like *1-0-1*. Worse, even after removing names, attackers can re-identify patients using age, village, and cross-hospital records."
>
> **0:40 – 1:40 (Solution & Architecture):**  
> "We built **MediShield**, a 100% offline, CPU-only, zero-LLM healthcare privacy firewall. Every record goes through four stages: First, Unicode normalization and Devanagari-to-Latin transliteration. Second, a hybrid detection engine combining regex, Indian context rules, clinical whitelists, and a lightweight scikit-learn classifier. Third, configurable anonymization using keyed HMAC-SHA256 pseudonyms and 5-year age bands. Fourth, cross-hospital linkage detection using Soundex blocking and RapidFuzz, plus *k*-anonymity risk and medical fidelity checks."
>
> **1:40 – 2:30 (Live Demo & Benchmarks):**  
> "In our live split-screen scanner, you can see Hinglish and Hindi notes sanitized in under 2 milliseconds while keeping *Type 2 Diabetes*, *Metformin 500 mg*, and *130/85 mmHg* 100% intact. We also audited our system with an independent 1,050-record synthetic stress test across English, Hindi, and Hinglish—catching real gaps in international phones, Hinglish `umra`/`pata` labels, and linkage false positives, raising overall recall from 84.1% to 100% on the stress suite."
>
> **2:30 – 3:00 (Closing):**  
> "MediShield runs via both a FastAPI + React dashboard and an offline `raksha.toml` CLI outputting `sanitized/`, `report.json`, and `records.jsonl`. Thank you—I am ready for your questions."

---

## 10. Phase 2–7 Improvements Explained Simply (For BCA Viva)

1. **Fellegi-Sunter 3-Tier Record Linkage (`linker.py`):**
   - *What it does:* Scores pairs of hospital records using Jaro-Winkler, token similarity, character 3-grams, phone match, age, and gender, then computes a **Fellegi-Sunter Log-Likelihood Ratio (LLR)**.
   - *Why we need it:* Prevents merging two strangers who share a name (`Rahul Sharma`) when their ages differ by > 5 years or phones are missing.
   - *3 Tiers:* `high_confidence_match` (auto-clustered), `uncertain_review` (needs human check), and `non_match`.
   - *Result:* False positives dropped from **700 → 64**, Precision rose from **6.7% → 43.9%** with **100% Recall**.
2. **Leakage Investigation (`stress_eval.py`):**
   - *What we found:* The earlier `3.66%` (182 flagged leaks) was **not** real leaked names or phones — **179** were age digits matching the upper bound of generalized 5-year bands (e.g., `19` inside `15–19`), and **3** were age `76` matching the clinical reading `BP 118/76 mmHg`. True PII leakage on the 1,050-record suite is **0.0%**.
3. **Metadata Privacy (`main.py`):**
   - *What it does:* Scans filenames and JSON dictionary keys for PII. If a filename contains a patient's name, it renames the output file to `redacted_<sha256_8>.<ext>` instead of leaking the name.
4. **Domain-Separated HKDF/HMAC (`anonymizer.py`):**
   - *What it does:* Derives a release-specific subkey from `RAKSHA_SECRET` + `release_scope` so pseudonyms cannot be linked across two unrelated hospital data releases, and checks for hash collisions. *(Note: HMAC is pseudonymization, NOT a Zero-Knowledge Proof.)*
5. **Character N-Gram TF-IDF (`detector.py`):**
   - *What it does:* Uses `char_wb` (2–4 character chunks) instead of only whole words so typos like `Pateint` or transliteration spellings are still scored accurately.

---

## 11. Learning Curve Audit Findings (Simple English)

- **Why did `1,000` and `10,000` give `0.0` F1 earlier?**  
  Our generator created all `15,000` positive `match` pairs first, followed by negative pairs. Even though `group_split()` shuffled group IDs, it appended rows in original order—so the first `10,000` training rows had **100% `1`s and 0% `0`s**. A model cannot learn to separate two classes if it only sees one class.
- **Why did the test confusion matrix show `[[3712, 0], [0, 3788]]` (100%)?**  
  In the 50k dataset, negative pairs always had large age gaps (`>= 20` years) or different phones, making them linearly separable. Also, `100%` of test names (`FIRST_EN` × `LAST_EN`) overlapped with training names.
- **What happened on the fresh 2,000-pair hard challenge set (`audit_linkage.py`)?**  
  Using completely unseen names (`Harish Shukla`, `Rekha Pathak`, etc.), 1-digit phone typos, missing phones, and hard negatives with the **same name, same age (0–2 yrs), and same city**, the preserved `linkage_model.joblib` achieved **Precision `0.9960`**, **Recall `0.9840`**, **F1 `0.9899`**, Confusion Matrix **`[[996, 4], [16, 984]]`** (4 false positives, 16 false negatives like `Rekha Pathak` vs `Rek. Pathak` with `phone: null` scoring `0.648` just below `0.65`).
- **Rule for ML Evaluation:** Always build learning curves on the **validation set** using **stratified, patient-disjoint** subsets, keeping the final test set untouched until the end.

# MediShield — Healthcare Privacy Firewall (2-Page Project Brief)

**Tagline:** Protecting Identities. Preserving Medical Intelligence.  
**Track:** Track 3 — Secret Wards (Offline, CPU-Only, LLM-Free Privacy Firewall)

---

## Page 1 — Unique Selling Proposition & System Architecture

### 1. Unique Selling Proposition (USP)
Standard PII redactors fail on Indian clinical data: they miss Devanagari (`मोहम्मद आरिफ`) and Hinglish (`Arif sahab ka BP 150/90`), confuse `"C/O Ramesh"` (relative) with `"C/O fever"` (symptom), redact `"1-0-1"` dosages as phone numbers, and ignore cross-hospital record linkage and *k*-anonymity risks.  
**MediShield** solves all five in a **100% offline, CPU-only, zero-LLM pipeline** that strips direct and quasi-identifiers while preserving clinical diagnoses, medications, dosages, vitals, and stay durations.

### 2. System Architecture
1. **Multilingual Ingestion & Normalization:** Reads CSV, TSV, JSON, and TXT with UTF-8/Latin-1 fallback and Unicode NFKC normalization + Devanagari-to-Latin transliteration.
2. **Hybrid PII Detection Engine:** Combines precision regex (Phone, Aadhaar, PAN, ABHA, UHID/MRN, Email, DOB, PIN), contextual disambiguation (`C/O` relative vs. complaint, `Dr.` whitelist vs. patient), and an offline `scikit-learn` TF-IDF + LogisticRegression context classifier.
3. **Intelligent Anonymization Engine:** Overlap-resolved transformations supporting Redaction, Masking, Keyed HMAC-SHA256 Pseudonymization (`RAKSHA_SECRET`), 5-year Age Banding, and Suppression.
4. **Cross-Hospital Record Linkage:** Phonetic/Soundex + phone-suffix blocking, Devanagari transliteration, and `RapidFuzz` Jaro-Winkler + token-set similarity with negative-evidence gender guards.
5. **Risk & Medical Fidelity Engines:** Equivalence-class *k*-anonymity risk scoring (before vs. after) and automated clinical entity preservation scoring.

---

## Page 2 — Evaluation, Privacy-Utility Trade-Offs & Demonstration

### 3. Privacy vs. Utility Trade-Offs
- **Clinical Preservation First:** Whitelisted medical terms (`Type 2 Diabetes`, `Metformin 500 mg`, `130/85 mmHg`, `1-0-1`) are explicitly protected from numeric/entity over-redaction.
- **Quasi-Identifier Generalization:** Exact ages generalize to 5-year bands (`45–49`), street addresses generalize to city/region, and rare diagnoses below threshold can be suppressed.
- **Honest Heuristic Limits:** Risk scores are clearly labeled as batch-level equivalence-class heuristics, never false guarantees against external auxiliary datasets.
- **Zero-Leakage Audit:** SQLite stores only aggregated sanitized metrics (counts, fidelity, latency)—never raw text or original identifiers.

### 4. Live Demonstration Flow
1. **Split-Screen Record Scanner:** Paste or load English, Hindi, or Hinglish clinical notes; inspect inline highlighted PII, detection method/confidence, sanitized output, risk reduction, and medical fidelity score.
2. **Batch & Offline CLI (`raksha.toml`):** Run `python main.py --input data/synthetic --output /tmp/out` or upload CSV/JSON/TXT in the dashboard to produce `sanitized/`, `report.json`, and `records.jsonl`.
3. **Evaluation Lab:** Live benchmark across multilingual and disambiguation edge cases reporting Precision, Recall, F1, PII Leakage Rate, Medical Preservation Rate, Linkage Accuracy, and Latency.

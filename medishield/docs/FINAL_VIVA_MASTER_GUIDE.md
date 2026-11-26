# MediShield — Final Viva Master Guide (Beginner-Friendly)

## 1. What Problem Does MediShield Solve?
Hospitals store patient records in English, Hindi, and Hinglish across multiple systems. Even if you erase a name inside a note, it can still leak in the **filename**, **folder name**, **CSV header**, or **JSON key** — or an attacker can match age + gender + city against a **Voter List** to re-identify the patient. MediShield stops this **completely offline on CPU without LLMs**, while keeping every medicine, dosage, lab value, vital, and hospital stay length intact.

## 2. How Does Each Layer Work? (Simple Explanations)
- **Multilingual PII Detector (`detector.py`):** Uses Unicode normalization (`NFKC`), regex rules (phones, Aadhaar, PAN, emails), Indian first+last name & Hinglish context rules (catching lowercase names like `"met rahul sharma"` while protecting `"Dr. Rajesh Gupta"`, `"C/O fever"`, and `"marez was admitted"`), plus a frozen character TF-IDF + Logistic Regression model.
- **Structured JSON Sanitizer (`structured.py`):** Automatically detects serialized JSON in both the CLI and `/anonymize` API, recursively sanitizing keys and values with depth protection (`<= 32` levels).
- **Keyed Metadata & Pseudonyms (`anonymizer.py`, `main.py`):** Uses standard **HMAC-SHA256** (`RAKSHA_SECRET` + `release_scope`) — never unkeyed hashes and never custom cryptography — so metadata tokens (`dir_`, `redacted_`, `field_`, `key_`) cannot be reversed by dictionary lookup or linked across releases.
- **Fail-Closed Clinical Integrity Gate (`fidelity.py`, `main.py`):** Checks that medicines (`Warfarin 2.5 mg`), units (`145000 /uL`), labs (`HbA1c 7.8%`), vitals (`130/85 mmHg`), and stay lengths (`4 days`) survive. If anything is lost, it tries a safe recovery pass; if still unresolved, it **quarantines** the file instead of releasing corrupted medical data.
- **Distinct-Patient $k$-Anonymity (`reid_lab.py`):** Deduplicates multi-hospital visits by `patient_id` so 3 visits by 1 person never pretend to be 3 distinct people.
- **Safe Internal Record Linkage (`linker.py`):** Uses frozen V2/V3 models + RapidFuzz with a **shared-family-phone guardrail** so two family members with different first names sharing one phone number are routed to `uncertain_review` instead of auto-merging.

## 3. Honest Limitations (Never Overclaim in Viva)
1. **Synthetic vs. Official Results:** Our `0%` direct PII leakage and `100%` clinical preservation come from our synthetic benchmarks; official organizer validation (`validate_output.py`) is **pending**.
2. **Unprefixed Lowercase Edge Cases:** Rare lowercase names not in our dictionary and without strong verb cues can still be missed (`0%` on one un-tuned handwritten slice).
3. **Residual Quasi-Identifiers:** Age bands and gender remain, so a forced guesser succeeds at rate $\approx 1/k$.

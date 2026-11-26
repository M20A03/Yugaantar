# MediShield — Healthcare Privacy Firewall (PRD, TRD, UI/UX & Schema)

## 1. Product Requirements Document (PRD)
- **Product Name:** MediShield — Healthcare Privacy Firewall
- **Tagline:** Protecting Identities. Preserving Medical Intelligence.
- **Problem:** Fragmented Indian hospital records (CSV, JSON, TXT, clinical notes) mix English, Devanagari Hindi, and Hinglish, contain overlapping PII and quasi-identifiers, and risk cross-hospital linkage attacks while requiring clinical fidelity (diagnoses, dosages, vitals, stay length) to remain intact.
- **Core Capabilities:**
  1. **Multilingual PII Detection (Offline, LLM-Free):** Hybrid Regex + Unicode/Devanagari transliteration + contextual rules + classical ML (`scikit-learn`) for English, Hindi, and Hinglish.
  2. **Intelligent Anonymization:** Redaction, masking, keyed HMAC pseudonymization, age/date generalization, and suppression with overlap resolution.
  3. **Cross-Hospital Record Linkage:** Blocking + phonetic/transliteration + `RapidFuzz` weighted similarity to detect linkage risk without exposing raw identities.
  4. **Re-identification Risk Assessment:** Heuristic *k*-anonymity & equivalence-class risk before vs. after anonymization, with explicit limitations.
  5. **Medical Data Fidelity Engine:** Measures exact preservation of diagnoses, medications, dosages, vitals, and lab values.
  6. **Batch Processing & Offline CLI (`raksha.toml`):** Supports CSV, JSON, and TXT uploads in UI and offline `main.py --input ... --output ...` batch execution.
  7. **Evaluation Lab:** Real precision, recall, F1, leakage rate, false positive rate, medical fidelity, linkage accuracy, and latency on synthetic multilingual test cases.

## 2. Technical Requirements Document (TRD)
- **Strict Constraints:** 100% offline core processing; zero LLM/external API calls; zero raw PII in logs or SQLite audit metadata; bounded file uploads (<= 10 MB).
- **Backend Stack:** Python 3.13, FastAPI, Pydantic v2, RapidFuzz, scikit-learn, Pandas, NumPy, SQLite (sanitized metadata only).
- **Frontend Stack:** React 18, TypeScript, Vite, Tailwind CSS, Recharts, custom inline SVG icons (per `.agents/rules/rule.md` — no Lucide icons, no purple gradients, no glass cards, no fake stats).
- **API Endpoints:** `GET /health`, `POST /scan`, `POST /anonymize`, `POST /batch-process`, `POST /linkage/analyze`, `POST /risk/analyze`, `POST /fidelity/evaluate`, `GET /metrics`, `GET /audit-logs`, `GET /evaluation/run`.

## 3. UI/UX Design Document
- **Visual System:** Dark navy (`#0B111A`) & charcoal (`#111827`) surfaces, subtle slate borders (`#1F2937`), teal (`#14B8A6`) & emerald (`#10B981`) accents, amber/crimson semantic risk badges.
- **Typography:** `Plus Jakarta Sans` (headings/UI) and `JetBrains Mono` (code, offsets, tokens, metrics).
- **Layout:** Left sidebar navigation (`Overview`, `Record Scanner`, `Batch Processing`, `Privacy Risk Analysis`, `Record Linkage`, `Medical Fidelity`, `Audit Logs`, `Evaluation Lab`, `Settings`) + top status bar showing offline mode & real processed counts.
- **Record Scanner:** Split-screen (Left: original text with inline entity highlights; Right: sanitized output with copy/export, entity table, risk comparison, and fidelity score).

## 4. Backend Schema
- **SQLite (`audit_logs` table):** `id`, `created_at`, `operation`, `language`, `records_count`, `entities_detected`, `entities_removed`, `fidelity_score`, `risk_before`, `risk_after`, `latency_ms` (zero raw PII or original text).
- **Pydantic Multi-Model Contracts:** `DetectedEntity`, `ScanRequest/Response`, `AnonymizeRequest/Response`, `LinkageRequest/Response`, `RiskAnalyzeRequest/Response`, `FidelityRequest/Response`, `BatchProcessResponse`, `MetricsResponse`, `EvaluationResponse`.

## 5. Research & Assumptions
- **Track 3 Alignment:** Built to the MediShield Track 3 specification (offline English/Hindi/Hinglish privacy firewall + `raksha.toml` CLI contract). Note: The later 2-page overview PDF mentioned ZKP for Track 3 without a detail tab; this implementation fulfills the full MediShield specification and documents heuristic risk limitations transparently.
- **Disambiguation Rules:** `"C/O Ramesh"` (care of relative) is PII; `"C/O fever"` (complaint of) is clinical. `"Dr. Ramesh"` is preserved; `"Patient Rahul"` is redacted. `"1-0-1"` and `"500 mg"` are preserved dosages, never phone numbers.

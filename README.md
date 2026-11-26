# MediShield — Healthcare Privacy Firewall

**Yugaantar DevForge Hackathon · Track 3: Secret Wards**  
*Protecting Identities. Preserving Medical Intelligence.*

MediShield is an offline, CPU-only, LLM-free healthcare privacy firewall designed for fragmented Indian hospital records across English, Hindi (Devanagari), and Hinglish. It removes direct and quasi-identifying personal information from unstructured clinical notes, structured tables (CSV/TSV), JSON/FHIR R4 bundles, and file/folder/header/key metadata while preserving exact clinical data (medications, decimal dosages, laboratory values and units, vitals, diagnoses, and hospital stay lengths).

## Repository Structure
- `raksha.toml` — Official submission entrypoint (`setup` and `run` commands).
- `main.py` — Root CLI entrypoint delegating to `medishield/main.py`.
- `requirements.txt` — Pinned CPU-only Python dependencies (zero LLM or external AI packages).
- `config/policy.yaml` — Privacy policy configuration (10-year age band default, 180-day max date shift, `min_group_size: 5`, release scope).
- `MediShield_Project_Brief.pdf` — Two-page project brief covering architecture, USP, privacy-utility trade-offs, and limitations.
- `medishield/` — Full backend (`FastAPI`, `scikit-learn`, `RapidFuzz`), frozen V2/V3 `.joblib` artifacts, offline CLI, React + TypeScript dashboard, QA test suites, and consolidated documentation (`medishield/docs/README.md`).

## Reproducible Offline Setup & Execution
```bash
pip install -r requirements.txt
export RAKSHA_SECRET="your-release-secret"
python main.py --input <input_dir> --output <output_dir>
```
The pipeline generates `output/sanitized/`, `output/report.json`, and `output/records.jsonl`, preserving relative folder structure and file formats while renaming metadata that contains PII.

## Architecture & How Each Component Works
1. **Fail-Safe Quarantine Gate:** Rejects symlinks, files over 10 MB, invalid UTF-8 encodings, empty files, malformed CSV/TSV rows, invalid or deeply nested JSON (`> 32` levels), and unsupported extensions. Quarantined files are logged in `report.json` by `input_sha256` only and are never copied into `sanitized/`.
2. **Multilingual PII Detection (`medishield/backend/app/services/pii_detection/detector.py`):** Combines Unicode NFKC normalization, zero-width character stripping, Devanagari transliteration, precision regexes (phones, emails, Aadhaar, PAN, ABHA, MRN), sliding-window Indian name-pair matching, English/Hinglish/Hindi prepositional and clinical context rules, and a frozen character-level TF-IDF + Logistic Regression classifier. Clinical disambiguation protects `Dr.` names, `C/O fever`, `Parkinson's disease`, `Wilson's disease`, and `"marez was admitted"`.
3. **Keyed Pseudonymization & Metadata Protection (`anonymizer.py`, `structured.py`):** Uses standard domain-separated HMAC-SHA256 keyed by `RAKSHA_SECRET` and `release_scope` so identical inputs with the same secret produce identical outputs, while different secrets produce distinct pseudonyms and metadata tokens (`dir_`, `redacted_`, `field_`, `key_`).
4. **Independent Privacy Verifier & Fail-Closed Clinical Integrity Gate (`release_gate.py`, `fidelity.py`):** Runs a second-pass residual PII check and verifies exact preservation of medications, dosages, labs, vitals, and stay lengths. Unresolved clinical loss triggers safe recovery or fail-closed quarantine (`status: "quarantined"`).
5. **Cross-Hospital Record Linkage (`linker.py`):** Links fragmented patient records across hospitals using frozen V2/V3 models and RapidFuzz with a shared-family-phone + distinct-first-name guardrail that routes ambiguous family-phone pairs to human review instead of auto-merging.

## Security Design & Honest Limitations
- **Security:** No custom cryptography, no hardcoded secrets, no raw PII in SQLite `AuditStore` or `report.json`, and depth/size/symlink/traversal guards.
- **Limitations:** Unfamiliar lowercase names without contextual cues or lexicon entries can still escape detection; 10-year age bands and gender remain as residual quasi-identifiers (~1/k forced-guess accuracy); 10-digit numeric specimen IDs starting with 6–9 may be conservatively redacted as phone numbers. Observed 0% leakage and 100% clinical preservation apply only to evaluated synthetic benchmarks.

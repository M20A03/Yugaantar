# MediShield — Final Live Demonstration Script (2–3 Minutes)

1. **Opening (15s):**
   *"MediShield is an offline, CPU-only, LLM-free healthcare privacy firewall for Track 3: Secret Wards. It strips patient identities across English, Hindi, and Hinglish — including filenames, folders, CSV headers, and JSON keys — while keeping exact medicines, dosages, lab units, vitals, and stay lengths 100% intact."*
2. **Record Scanner + Live Demo Presets (45s):**
   - Select **Demo 1: Hinglish** -> click **Scan & Anonymize**. Show side-by-side Original vs. Sanitized output, Privacy Explainability Summary, and Medical Fidelity `100%`.
   - Select **Demo 3: Lowercase** -> show lowercase names (`met rahul sharma...`, `ananya kulkarni`) are caught while `Warfarin 2.5 mg`, `HbA1c 7.8%`, `Platelets 145000 /uL` stay untouched.
   - Select **Demo 4: JSON String** -> show automatic structural JSON key+value sanitization.
3. **Metadata Security Tab (30s):**
   - Click **Inspect Metadata** -> show keyed HMAC-SHA256 tokens (`redacted_`, `dir_`, `field_`, `key_`), path-traversal blocking, and fail-safe quarantine rules.
4. **Privacy Defense Lab Tab (45s):**
   - Select **1,000 patients** / **10-year age band** -> click **Run Defense Simulation**.
   - Highlight **Unique Confident Re-ID (0.0%)**, **Forced Top-Match Accuracy**, **Attacker Coverage**, **Distinct-Patient Min/Avg $k$**, and **Remaining Limitations** (explicitly noting synthetic-only scope).
5. **Offline CLI (`raksha.toml`) & Closing (15s):**
   - Show `python main.py --input <in> --output <out>` producing `sanitized/`, `report.json` (with `output_completeness` & `clinical_integrity_flagged`), and quarantined broken files.

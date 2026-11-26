"""Tests for Privacy Defense Lab, Clinical Integrity, Metadata Sanitization, and Quarantine."""

import csv
import json
import sys
from pathlib import Path

from fastapi.testclient import TestClient

ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT_DIR / "backend"))
sys.path.insert(0, str(ROOT_DIR))

from app.main import app  # noqa: E402
from app.services.medical_fidelity.fidelity import MedicalFidelityEngine  # noqa: E402
import main as cli_main  # noqa: E402


client = TestClient(app)


def test_privacy_defense_lab_endpoint():
    res = client.post("/privacy-defense/evaluate?n_patients=24&seed=7")
    assert res.status_code == 200
    data = res.json()
    assert data["total_records"] >= 48
    assert len(data["hospital_systems"]) == 4
    assert data["before_reidentification_rate"] > data["after_reidentification_rate"]
    assert data["risk_reduction_pct"] > 50.0
    assert data["clinical_preservation_score"] >= 0.90
    assert "voter_id" not in json.dumps(data)


def test_clinical_integrity_preserves_units_labs_vitals_and_stay():
    engine = MedicalFidelityEngine()
    orig = (
        "Patient Rahul Sharma diagnosed with Type 2 Diabetes. "
        "Rx: Metformin 500 mg 1-0-1, Insulin 10 units BD. "
        "Labs: HbA1c 7.8%, Creatinine 1.2 mg/dL. "
        "Vitals: BP 130/85 mmHg. Hospital stay: 4 days."
    )
    sanitized = (
        "Patient [PERSON_1] diagnosed with Type 2 Diabetes. "
        "Rx: Metformin 500 mg 1-0-1, Insulin 10 units BD. "
        "Labs: HbA1c 7.8%, Creatinine 1.2 mg/dL. "
        "Vitals: BP 130/85 mmHg. Hospital stay: 4 days."
    )
    res = engine.evaluate(orig, sanitized)
    assert res["preservation_score"] == 1.0
    assert res["lost_items"] == []
    assert "stay_length" in res["breakdown"]


def test_cli_metadata_sanitization_and_quarantine(tmp_path: Path):
    in_dir = tmp_path / "in"
    out_dir = tmp_path / "out"
    pii_dir = in_dir / "Aarav_Sharma_9876543210"
    pii_dir.mkdir(parents=True)

    # 1. Valid TXT with PII in directory and filename
    (pii_dir / "Rahul_Verma_9811223344.txt").write_text(
        "Patient Rahul Verma took Metformin 500 mg for 4 days.", encoding="utf-8"
    )

    # 2. CSV with PII in column header
    csv_path = in_dir / "labs.csv"
    csv_path.write_text(
        "Aarav_Sharma_9876543210,diagnosis,stay\nRahul Verma,Hypertension,3 days\n",
        encoding="utf-8",
    )

    # 3. JSON with colliding PII keys
    (in_dir / "nested.json").write_text(
        json.dumps(
            {
                "Rahul Sharma": "Metformin 500 mg",
                "Priya Verma": "Insulin 10 units",
            }
        ),
        encoding="utf-8",
    )

    # 4. Quarantined files: broken UTF-8, empty txt, invalid json, unsupported ext, malformed csv
    (in_dir / "bad_bytes.txt").write_bytes(b"\xff\xfe\xfd\x80")
    (in_dir / "empty.txt").write_text("   \n", encoding="utf-8")
    (in_dir / "broken.json").write_text("{bad json", encoding="utf-8")
    (in_dir / "payload.exe").write_bytes(b"MZ90")
    (in_dir / "malformed.csv").write_text("a,b\n1,2,3,4\n", encoding="utf-8")

    cli_main.run_pipeline(in_dir, out_dir)

    report = json.loads((out_dir / "report.json").read_text(encoding="utf-8"))
    assert report["counts"]["files_sanitized"] == 3
    assert report["counts"]["files_quarantined"] == 5

    # Ensure raw PII names/phones from filenames or directories never leak into report.json
    report_str = json.dumps(report)
    assert "Aarav_Sharma" not in report_str
    assert "Rahul_Verma" not in report_str
    assert "9876543210" not in report_str
    assert "bad_bytes" not in report_str

    # Ensure sanitized directory contains only 3 files and none of the quarantined ones
    sanitized_files = [p for p in (out_dir / "sanitized").rglob("*") if p.is_file()]
    assert len(sanitized_files) == 3

    # Check CSV header sanitized & clinical data preserved
    san_csv = (out_dir / "sanitized" / "labs.csv").read_text(encoding="utf-8")
    reader = list(csv.reader(san_csv.splitlines()))
    assert "Aarav_Sharma" not in reader[0][0]
    assert "Hypertension" in san_csv
    assert "3 days" in san_csv

    # Check colliding JSON keys did not overwrite either clinical value
    san_json = (out_dir / "sanitized" / "nested.json").read_text(encoding="utf-8")
    assert "Metformin 500 mg" in san_json
    assert "Insulin 10 units" in san_json

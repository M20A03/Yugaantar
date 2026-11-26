"""Grand Finale QA tests: lowercase/multilingual PII, JSON API routing, fail-closed gate, linkage guardrail, metadata inspect."""

import json
import sys
from pathlib import Path

from fastapi.testclient import TestClient

ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT_DIR / "backend"))
sys.path.insert(0, str(ROOT_DIR))

from app.main import app  # noqa: E402
from app.models.schemas import HospitalRecordInput  # noqa: E402
from app.services.record_linkage.linker import RecordLinkageEngine  # noqa: E402
import main as cli_main  # noqa: E402


client = TestClient(app)


def test_lowercase_and_multilingual_pii_examples():
    cases = [
        ("met rahul sharma yesterday for Warfarin 2.5 mg", "rahul"),
        ("spoke with ananya kulkarni regarding Metformin 500 mg", "ananya"),
        ("ravi kumar was brought to hospital with SpO2 95%", "ravi"),
        ("kal priya singh hospital aayi thi, BP 130/85 mmHg", "priya"),
        ("मरीज सुनीता देवी को बुखार है", "सुनीता"),
        ("attendant: mohammed arif, stay 4 days", "mohammed"),
    ]
    for text, target in cases:
        res = client.post("/anonymize", json={"text": text})
        assert res.status_code == 200
        san = res.json()["sanitized_text"]
        assert target.lower() not in san.lower(), f"Failed to strip {target} in: {san}"

    # Negative check: 'marez was admitted yesterday' must NOT strip 'was admitted'
    neg = client.post("/anonymize", json={"text": "marez was admitted yesterday for 4 days, HbA1c 7.8%."})
    assert neg.status_code == 200
    assert "was admitted" in neg.json()["sanitized_text"]
    assert "HbA1c 7.8%" in neg.json()["sanitized_text"]


def test_raw_json_string_routed_to_structural_sanitization():
    payload = json.dumps({
        "patient_rahul_sharma": "Insulin 10 units BD",
        "contact": "+91-9811223344",
        "labs": {"hba1c": "7.8%", "platelets": "145000 /uL"},
    })
    res = client.post("/anonymize", json={"text": payload})
    assert res.status_code == 200
    data = res.json()
    assert data["language"] == "structured_json"
    assert "rahul_sharma" not in data["sanitized_text"].lower()
    assert "9811223344" not in data["sanitized_text"]
    assert "Insulin 10 units BD" in data["sanitized_text"]
    assert "145000 /uL" in data["sanitized_text"]


def test_deep_json_rejected_and_quarantined(tmp_path: Path):
    # Build >35-level nested JSON
    deep: dict = {"a": "val"}
    for _ in range(36):
        deep = {"n": deep}
    res = client.post("/anonymize", json={"text": json.dumps(deep)})
    assert res.status_code == 400

    in_d = tmp_path / "in"
    out_d = tmp_path / "out"
    in_d.mkdir()
    (in_d / "deep.json").write_text(json.dumps(deep), encoding="utf-8")
    cli_main.run_pipeline(in_d, out_d)
    rep = json.loads((out_d / "report.json").read_text(encoding="utf-8"))
    assert rep["counts"]["files_quarantined"] == 1
    assert rep["counts"]["output_completeness"] == 0.0


def test_shared_family_phone_never_auto_merges():
    linker = RecordLinkageEngine()
    records = [
        HospitalRecordInput(record_id="A1", hospital="H1", name="Aarav Sharma", phone="9811223344", age=34, gender="M"),
        HospitalRecordInput(record_id="B1", hospital="H2", name="Rohan Sharma", phone="9811223344", age=35, gender="M"),
    ]
    _, pairs, clusters = linker.analyze(records, threshold=0.72)
    assert clusters == [], "Distinct first names sharing family phone must not auto-cluster"
    for p in pairs:
        assert p.decision != "high_confidence_match"


def test_metadata_inspect_endpoint():
    res = client.post("/metadata/inspect", json={
        "filename": "Rahul_Sharma_9876543210.csv",
        "directory": "Aarav_Sharma_9811223344",
        "headers": ["patient_rahul_sharma", "diagnosis"],
        "json_sample": {"Rahul Sharma": "Metformin 500 mg"},
    })
    assert res.status_code == 200
    data = res.json()
    assert data["filename_pii_detected"] is True
    assert "Rahul_Sharma" not in data["sanitized_filename"]
    assert "Aarav_Sharma" not in data["sanitized_directory"]
    assert "Rahul" not in json.dumps(data["sanitized_json_preview"])
    assert "Metformin 500 mg" in json.dumps(data["sanitized_json_preview"])

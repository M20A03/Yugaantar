"""Unit and integration tests for MediShield privacy firewall."""

import sys
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.main import app  # noqa: E402

client = TestClient(app)


def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    body = res.json()
    assert body["status"] == "ready"
    assert body["offline_mode"] is True
    assert body["llm_usage"] is False


def test_scan_and_anonymize_hinglish_preserves_clinical():
    sample = (
        "Patient Rahul Sharma, aged 45, residing at MG Road, Bengaluru. "
        "Contact: 9876543210. Patient ko Type 2 Diabetes hai. "
        "Metformin 500 mg prescribed. Blood pressure: 130/85 mmHg."
    )
    res = client.post("/anonymize", json={"text": sample})
    assert res.status_code == 200
    data = res.json()
    san = data["sanitized_text"]
    assert "Rahul Sharma" not in san
    assert "9876543210" not in san
    assert "MG Road" not in san
    assert "45–49" in san
    assert "Type 2 Diabetes" in san
    assert "Metformin 500 mg" in san
    assert "130/85 mmHg" in san
    assert data["fidelity"]["preservation_score"] == 1.0


def test_meaning_disambiguation_co_and_doctor():
    sample = "Pt. Meera Devi, C/O fever and cough. Dr. Rajesh Gupta prescribed Dolo 650 mg 1-0-1. C/O Rajan Kumar."
    res = client.post("/anonymize", json={"text": sample})
    assert res.status_code == 200
    san = res.json()["sanitized_text"]
    assert "Meera Devi" not in san
    assert "Rajan Kumar" not in san
    assert "Dr. Rajesh Gupta" in san
    assert "fever" in san
    assert "Dolo 650 mg" in san
    assert "1-0-1" in san


def test_hindi_devanagari_detection():
    sample = "रोगी: मीरा देवी, उम्र 47 साल, पता: रामपुर गाँव, PIN 226001. Dengue diagnosed."
    res = client.post("/anonymize", json={"text": sample})
    assert res.status_code == 200
    san = res.json()["sanitized_text"]
    assert "मीरा देवी" not in san
    assert "226001" not in san
    assert "Dengue" in san


def test_cross_hospital_record_linkage():
    payload = {
        "records": [
            {"record_id": "R1", "hospital": "HOSP_A", "name": "Mohammad Arif", "phone": "9811223344", "age": 44, "gender": "M"},
            {"record_id": "R2", "hospital": "HOSP_B", "name": "मोहम्मद आरिफ", "phone": "+91 9811223344", "age": 44, "gender": "M"},
            {"record_id": "R3", "hospital": "HOSP_C", "name": "Sunita Yadav", "phone": "9988776655", "age": 38, "gender": "F"},
        ],
        "threshold": 0.72,
    }
    res = client.post("/linkage/analyze", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert len(data["flagged_pairs"]) >= 1
    assert len(data["clusters"]) == 1
    assert set(data["clusters"][0]["record_ids"]) == {"R1", "R2"}


def test_risk_analysis_and_evaluation_lab():
    risk_res = client.post(
        "/risk/analyze",
        json={
            "records": [
                {"age": 45, "gender": "M", "location": "MG Road, Bengaluru", "diagnosis": "Type 2 Diabetes"},
                {"age": 46, "gender": "M", "location": "Indiranagar, Bengaluru", "diagnosis": "Type 2 Diabetes"},
                {"age": 29, "gender": "F", "location": "Rampur, Lucknow", "diagnosis": "Dengue"},
            ]
        },
    )
    assert risk_res.status_code == 200
    r_data = risk_res.json()
    assert r_data["risk_after"]["reidentification_risk_score"] <= r_data["risk_before"]["reidentification_risk_score"]

    eval_res = client.get("/evaluation/run")
    assert eval_res.status_code == 200
    e_data = eval_res.json()
    assert e_data["f1_score"] >= 0.8
    assert e_data["pii_leakage_rate"] == 0.0
    assert e_data["medical_preservation_rate"] == 1.0


def test_v3_linkage_hard_negative_and_features():
    from app.services.record_linkage.features import extract_pair_features

    # Shared family phone but different first name, gender, and 24-year age gap -> contradictory!
    a = {"name": "Aarav Kulkarni", "phone": "9876543210", "age": 25, "gender": "M", "address": "Mumbai"}
    b = {"name": "Pooja Kulkarni", "phone": "9876543210", "age": 49, "gender": "F", "address": "Mumbai"}
    feats = extract_pair_features(a, b)
    assert feats[-1] == 1.0  # contradictory_evidence must trigger

    # Missing phone should NOT be marked contradictory when other fields agree
    c = {"name": "Aarav Kulkarni", "phone": None, "age": 25, "gender": "M", "address": "Mumbai", "dob": "2001-04-12"}
    a["dob"] = "2001-04-12"
    feats_miss = extract_pair_features(a, c)
    assert feats_miss[8] == 0.0   # phone_available == 0
    assert feats_miss[-1] == 0.0  # contradictory_evidence == 0
    assert feats_miss[11] == 1.0  # dob_agree == 1

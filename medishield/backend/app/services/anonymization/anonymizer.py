"""Intelligent anonymization engine supporting 5 transformation modes."""

import hashlib
import hmac
import os
import secrets
from typing import Dict, List, Tuple

from app.models.schemas import DetectedEntity, PolicyConfig, TransformMode
from app.services.pii_detection.detector import normalize_text


class AnonymizerEngine:
    """Applies configurable transformations with domain-separated HKDF/HMAC keys."""

    def __init__(self, secret_key: str | None = None, release_scope: str = "default-release") -> None:
        self._master = (
            secret_key
            or os.environ.get("RAKSHA_SECRET")
            or secrets.token_hex(32)
        ).encode("utf-8")
        self._release_scope = release_scope
        self._issued_pseudonyms: Dict[str, str] = {}

    def _derive_release_key(self) -> bytes:
        return hmac.new(
            self._master,
            f"medishield:hkdf:v1:{self._release_scope}".encode("utf-8"),
            hashlib.sha256,
        ).digest()

    def pseudonym_for(self, entity_type: str, value: str) -> str:
        norm_val = value.strip().lower()
        subkey = self._derive_release_key()
        digest = hmac.new(
            subkey,
            f"medishield:v1:{self._release_scope}:{entity_type}:{norm_val}".encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()[:8].upper()
        prefix = "PATIENT" if entity_type in {"PERSON", "RELATIVE_PERSON"} else entity_type
        token = f"[{prefix}_{digest}]"
        # Collision guard within release scope
        prev = self._issued_pseudonyms.get(token)
        if prev is not None and prev != f"{entity_type}:{norm_val}":
            digest = hmac.new(subkey, f"{entity_type}:{norm_val}:c".encode("utf-8"), hashlib.sha256).hexdigest()[:10].upper()
            token = f"[{prefix}_{digest}]"
        self._issued_pseudonyms[token] = f"{entity_type}:{norm_val}"
        return token

    def opaque_metadata_id(self, kind: str, value: str) -> str:
        """Generate a keyed, release-scoped opaque identifier for metadata (dirs/files/headers/keys)."""
        subkey = self._derive_release_key()
        digest = hmac.new(
            subkey,
            f"medishield:meta:v1:{self._release_scope}:{kind}:{value}".encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()[:10]
        return f"{kind}_{digest}"

    def transform_entity(self, ent: DetectedEntity, mode: TransformMode, age_band_size: int) -> str:
        if mode == "suppression":
            return "[SUPPRESSED]"
        if mode == "redaction":
            label_map = {
                "PERSON": "[PERSON_REDACTED]",
                "RELATIVE_PERSON": "[RELATIVE_REDACTED]",
                "PHONE": "[PHONE_REDACTED]",
                "ADDRESS": "[LOCATION_REDACTED]",
                "PIN_CODE": "[PIN_REDACTED]",
                "EMAIL": "[EMAIL_REDACTED]",
                "AADHAAR": "[AADHAAR_REDACTED]",
                "PAN": "[PAN_REDACTED]",
                "ABHA_ID": "[ABHA_REDACTED]",
                "HOSPITAL_ID": "[ID_REDACTED]",
                "DOB": "[DOB_REDACTED]",
                "AGE": "[AGE_REDACTED]",
            }
            return label_map.get(ent.entity_type, f"[{ent.entity_type}_REDACTED]")
        if mode == "masking":
            val = ent.text.strip()
            if len(val) <= 4:
                return "*" * len(val)
            return val[:2] + ("*" * (len(val) - 4)) + val[-2:]
        if mode == "generalization":
            if ent.entity_type == "AGE" and ent.text.isdigit():
                age = int(ent.text)
                low = (age // age_band_size) * age_band_size
                return f"{low}–{low + age_band_size - 1}"
            if ent.entity_type == "ADDRESS":
                return "[LOCATION_GENERALIZED]"
            if ent.entity_type == "DOB":
                parts = [p for p in ent.text.replace("-", "/").replace(".", "/").split("/") if p.isdigit()]
                years = [p for p in parts if len(p) == 4]
                return years[0] if years else "[YEAR_REDACTED]"
            return f"[{ent.entity_type}_GENERALIZED]"
        # Default: pseudonymization
        return self.pseudonym_for(ent.entity_type, ent.text)

    def anonymize(
        self, text: str, entities: List[DetectedEntity], policy: PolicyConfig
    ) -> Tuple[str, int]:
        text = normalize_text(text)
        if not entities:
            return text, 0

        pieces: List[str] = []
        cursor = 0
        count = 0

        for ent in sorted(entities, key=lambda e: e.start):
            if ent.start < cursor:
                continue
            pieces.append(text[cursor : ent.start])
            mode: TransformMode = policy.entity_modes.get(
                ent.entity_type,
                "generalization" if ent.entity_type == "AGE" else policy.default_mode,
            )
            # Default safe behavior for phones/locations in redaction-style policies
            if ent.entity_type in {"PHONE", "ADDRESS"} and ent.entity_type not in policy.entity_modes and policy.default_mode == "pseudonymization":
                mode = "redaction"
            pieces.append(self.transform_entity(ent, mode, policy.age_band_size))
            cursor = ent.end
            count += 1

        pieces.append(text[cursor:])
        return "".join(pieces), count

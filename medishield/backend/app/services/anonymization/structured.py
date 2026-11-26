"""Shared structural JSON/dict/list sanitization for both CLI and FastAPI routes."""

import json
from typing import Any, List, Optional, Tuple

from app.models.schemas import DetectedEntity, PolicyConfig
from app.services.anonymization.anonymizer import AnonymizerEngine
from app.services.pii_detection.detector import MultilingualPIIDetector


MAX_JSON_DEPTH = 32


class StructuredDepthError(ValueError):
    """Raised when nested JSON exceeds safe recursion depth."""


def _check_depth(obj: Any, depth: int = 0, max_depth: int = MAX_JSON_DEPTH) -> None:
    if depth > max_depth:
        raise StructuredDepthError(f"JSON nesting exceeds maximum safe depth ({max_depth})")
    if isinstance(obj, dict):
        for v in obj.values():
            _check_depth(v, depth + 1, max_depth)
    elif isinstance(obj, list):
        for item in obj:
            _check_depth(item, depth + 1, max_depth)


def try_parse_json_payload(text: str, max_depth: int = MAX_JSON_DEPTH) -> Optional[Any]:
    """Return parsed dict/list if text is valid serialized JSON, else None."""
    stripped = text.strip()
    if not (stripped.startswith("{") or stripped.startswith("[")):
        return None
    try:
        obj = json.loads(stripped)
    except json.JSONDecodeError:
        return None
    if not isinstance(obj, (dict, list)):
        return None
    _check_depth(obj, 0, max_depth)
    return obj


def sanitize_structured_payload(
    obj: Any,
    detector: MultilingualPIIDetector,
    anonymizer: AnonymizerEngine,
    policy: PolicyConfig,
    *,
    max_depth: int = MAX_JSON_DEPTH,
) -> Tuple[Any, List[DetectedEntity], int]:
    """Recursively sanitize JSON keys (keyed HMAC, collision-safe) and string values."""
    _check_depth(obj, 0, max_depth)
    collected_entities: List[DetectedEntity] = []
    total_applied = 0

    def _clean_key(key: str, used: set[str]) -> str:
        nonlocal total_applied
        _, k_ents = detector.scan(key.replace("_", " ").replace("-", " "))
        if k_ents:
            collected_entities.extend(k_ents)
            total_applied += len(k_ents)
            base_k = anonymizer.opaque_metadata_id("key", key)
        else:
            base_k = key
        cand = base_k
        suffix = 2
        while cand in used:
            cand = f"{base_k}_{suffix}"
            suffix += 1
        used.add(cand)
        return cand

    def _clean(node: Any) -> Any:
        nonlocal total_applied
        if isinstance(node, str):
            _, ents = detector.scan(node)
            if ents:
                collected_entities.extend(ents)
            san_val, applied = anonymizer.anonymize(node, ents, policy)
            total_applied += applied
            return san_val
        if isinstance(node, list):
            return [_clean(item) for item in node]
        if isinstance(node, dict):
            used_keys: set[str] = set()
            return {_clean_key(str(k), used_keys): _clean(v) for k, v in node.items()}
        return node

    sanitized = _clean(obj)
    return sanitized, collected_entities, total_applied

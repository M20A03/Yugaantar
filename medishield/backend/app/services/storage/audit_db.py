"""Sanitized-only SQLite audit metadata store (never stores raw PII)."""

import os
import sqlite3
from datetime import datetime, timezone
from typing import Any, Dict, List


class AuditStore:
    """Persists non-sensitive processing statistics and category counts."""

    def __init__(self, db_path: str | None = None) -> None:
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        self.db_path = db_path or os.path.join(base_dir, "medishield_audit.db")
        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS audit_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    created_at TEXT NOT NULL,
                    operation TEXT NOT NULL,
                    language TEXT NOT NULL,
                    records_count INTEGER NOT NULL,
                    entities_detected INTEGER NOT NULL,
                    entities_removed INTEGER NOT NULL,
                    linkage_flagged INTEGER NOT NULL DEFAULT 0,
                    fidelity_score REAL NOT NULL,
                    risk_before REAL NOT NULL,
                    risk_after REAL NOT NULL,
                    latency_ms REAL NOT NULL
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS category_stats (
                    category TEXT PRIMARY KEY,
                    count INTEGER NOT NULL
                )
                """
            )

    def log_event(
        self,
        *,
        operation: str,
        language: str,
        records_count: int,
        entities_detected: int,
        entities_removed: int,
        linkage_flagged: int = 0,
        fidelity_score: float = 1.0,
        risk_before: float = 0.0,
        risk_after: float = 0.0,
        latency_ms: float = 0.0,
        category_counts: Dict[str, int] | None = None,
    ) -> None:
        now = datetime.now(timezone.utc).isoformat()
        with self._connect() as conn:
            conn.execute(
                """
                INSERT INTO audit_logs (
                    created_at, operation, language, records_count,
                    entities_detected, entities_removed, linkage_flagged,
                    fidelity_score, risk_before, risk_after, latency_ms
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    now, operation, language, records_count,
                    entities_detected, entities_removed, linkage_flagged,
                    fidelity_score, risk_before, risk_after, round(latency_ms, 2),
                ),
            )
            if category_counts:
                for cat, cnt in category_counts.items():
                    conn.execute(
                        """
                        INSERT INTO category_stats (category, count) VALUES (?, ?)
                        ON CONFLICT(category) DO UPDATE SET count = count + excluded.count
                        """,
                        (cat, cnt),
                    )

    def get_metrics(self) -> Dict[str, Any]:
        with self._connect() as conn:
            agg = conn.execute(
                """
                SELECT
                    COALESCE(SUM(records_count), 0) AS total_records,
                    COALESCE(SUM(entities_detected), 0) AS total_detected,
                    COALESCE(SUM(entities_removed), 0) AS total_removed,
                    COALESCE(SUM(linkage_flagged), 0) AS total_linkage,
                    COALESCE(AVG(fidelity_score), 1.0) AS avg_fidelity,
                    COALESCE(AVG(latency_ms), 0.0) AS avg_latency,
                    COALESCE(AVG(risk_before - risk_after), 0.0) AS avg_risk_red
                FROM audit_logs
                """
            ).fetchone()

            cats = {
                r["category"]: r["count"]
                for r in conn.execute("SELECT category, count FROM category_stats").fetchall()
            }
            langs = {
                r["language"]: r["cnt"]
                for r in conn.execute(
                    "SELECT language, SUM(records_count) AS cnt FROM audit_logs GROUP BY language"
                ).fetchall()
            }
            recent = [
                dict(r)
                for r in conn.execute(
                    "SELECT * FROM audit_logs ORDER BY id DESC LIMIT 25"
                ).fetchall()
            ]

        return {
            "total_records_processed": int(agg["total_records"]),
            "total_entities_detected": int(agg["total_detected"]),
            "total_identifiers_removed": int(agg["total_removed"]),
            "records_flagged_linkage": int(agg["total_linkage"]),
            "avg_medical_fidelity": round(float(agg["avg_fidelity"]), 4),
            "avg_latency_ms": round(float(agg["avg_latency"]), 2),
            "avg_risk_reduction": round(float(agg["avg_risk_red"]), 4),
            "category_distribution": cats,
            "language_distribution": langs,
            "recent_activity": recent,
        }

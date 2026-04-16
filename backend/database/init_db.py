import csv
from pathlib import Path

from sqlalchemy import text

from database.connection import engine


CSV_PATTERNS_PATH = Path(__file__).resolve().parent.parent / "data" / "patrones.csv"


def _create_patterns_table() -> None:
    with engine.begin() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS patterns (
                id SERIAL PRIMARY KEY,
                pattern TEXT NOT NULL UNIQUE,
                category TEXT NOT NULL,
                risk_level TEXT NOT NULL,
                suggestion TEXT NOT NULL
            )
        """))


def _seed_patterns_from_csv() -> None:
    if not CSV_PATTERNS_PATH.exists():
        return

    with CSV_PATTERNS_PATH.open("r", encoding="utf-8", newline="") as csv_file:
        rows = list(csv.DictReader(csv_file))

    if not rows:
        return

    with engine.begin() as conn:
        insert_query = text("""
            INSERT INTO patterns (pattern, category, risk_level, suggestion)
            VALUES (:pattern, :category, :risk_level, :suggestion)
            ON CONFLICT (pattern) DO UPDATE
            SET category = EXCLUDED.category,
                risk_level = EXCLUDED.risk_level,
                suggestion = EXCLUDED.suggestion
        """)

        for row in rows:
            pattern = (row.get("patron") or "").strip()
            category = (row.get("categoria") or "").strip()
            risk_level = (row.get("nivel_alerta") or "").strip()
            suggestion = (row.get("sugerencia") or "").strip()

            if not pattern:
                continue

            conn.execute(
                insert_query,
                {
                    "pattern": pattern,
                    "category": category,
                    "risk_level": risk_level,
                    "suggestion": suggestion,
                },
            )


def initialize_database() -> None:
    _create_patterns_table()
    _seed_patterns_from_csv()

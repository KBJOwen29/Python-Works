import sqlite3
from datetime import datetime
from pathlib import Path


DATABASE_PATH = Path(__file__).resolve().parent.parent / "calculator.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_connection()
    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS calculation_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                expression TEXT NOT NULL,
                result TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        """)
        connection.commit()
    finally:
        connection.close()


def save_calculation(expression, result):
    connection = get_connection()
    try:
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor = connection.execute(
            """
            INSERT INTO calculation_history (expression, result, created_at)
            VALUES (?, ?, ?)
            """,
            (expression, str(result), created_at),
        )
        connection.commit()
        return cursor.lastrowid
    finally:
        connection.close()


def get_all_calculations():
    connection = get_connection()
    try:
        rows = connection.execute(
            """
            SELECT id, expression, result, created_at
            FROM calculation_history
            ORDER BY id DESC
            """
        ).fetchall()
        return [dict(row) for row in rows]
    finally:
        connection.close()


def get_calculation(calculation_id):
    connection = get_connection()
    try:
        row = connection.execute(
            """
            SELECT id, expression, result, created_at
            FROM calculation_history
            WHERE id = ?
            """,
            (calculation_id,),
        ).fetchone()
        return dict(row) if row else None
    finally:
        connection.close()


def search_calculations(term):
    connection = get_connection()
    try:
        pattern = f"%{term}%"
        rows = connection.execute(
            """
            SELECT id, expression, result, created_at
            FROM calculation_history
            WHERE expression LIKE ? OR result LIKE ?
            ORDER BY id DESC
            """,
            (pattern, pattern),
        ).fetchall()
        return [dict(row) for row in rows]
    finally:
        connection.close()


def delete_calculation(calculation_id):
    connection = get_connection()
    try:
        cursor = connection.execute(
            "DELETE FROM calculation_history WHERE id = ?",
            (calculation_id,),
        )
        connection.commit()
        return cursor.rowcount > 0
    finally:
        connection.close()


def clear_history():
    connection = get_connection()
    try:
        connection.execute("DELETE FROM calculation_history")
        connection.commit()
    finally:
        connection.close()

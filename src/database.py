import sqlite3
from pathlib import Path

DB_PATH = Path("data/snippets.db")

def init_db():
    """Initialize the database and create table if it doesn't exist."""
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS snippets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_snippets(snippets):
    """Save a list of snippets to the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO snippets (content) VALUES (?)", [(s,) for s in snippets])
    conn.commit()
    conn.close()

def load_snippets():
    """Load all snippets from the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM snippets")
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]

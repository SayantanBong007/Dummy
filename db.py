import sqlite3
from contextlib import contextmanager


@contextmanager
def get_connection(db_path: str = "app.db"):
    conn = sqlite3.connect(db_path)
    try:
        yield conn
    finally:
        conn.close()

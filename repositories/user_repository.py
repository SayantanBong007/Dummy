from db import get_connection
from models.user import User
from exceptions import UserNotFoundError, UserAlreadyExistsError


class UserRepository:
    def create(self, username: str, password_hash: str) -> User:
        with get_connection() as conn:
            cursor = conn.cursor()

            existing = cursor.execute(
                "SELECT id FROM users WHERE username = ?",
                (username,)
            ).fetchone()

            if existing:
                raise UserAlreadyExistsError(f"User '{username}' already exists")

            cursor.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, password_hash)
            )
            conn.commit()

            return User(id=cursor.lastrowid, username=username, password_hash=password_hash)

    def find_by_username(self, username: str) -> User:
        with get_connection() as conn:
            cursor = conn.cursor()

            row = cursor.execute(
                "SELECT id, username, password_hash FROM users WHERE username = ?",
                (username,)
            ).fetchone()

            if not row:
                raise UserNotFoundError(f"User '{username}' not found")

            return User(id=row[0], username=row[1], password_hash=row[2])

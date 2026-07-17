from repositories.user_repository import UserRepository
from utils import hash_password, verify_password
from exceptions import InvalidCredentialsError
from config import PASSWORD_MIN_LENGTH


class UserService:
    def __init__(self, repository: UserRepository = None):
        self.repository = repository or UserRepository()

    def register(self, username: str, password: str):
        if len(password) < PASSWORD_MIN_LENGTH:
            raise ValueError(f"Password must be at least {PASSWORD_MIN_LENGTH} characters")

        password_hash = hash_password(password)
        return self.repository.create(username, password_hash)

    def authenticate(self, username: str, password: str):
        user = self.repository.find_by_username(username)

        if not verify_password(password, user.password_hash):
            raise InvalidCredentialsError("Incorrect password")

        return user

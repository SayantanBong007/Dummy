from services.user_service import UserService
from models.user import User


class FakeRepository:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def create(self, username, password_hash):
        user = User(id=self.next_id, username=username, password_hash=password_hash)
        self.users[username] = user
        self.next_id += 1
        return user

    def find_by_username(self, username):
        return self.users[username]


def test_register_and_authenticate():
    service = UserService(repository=FakeRepository())
    service.register("alice", "supersecret")
    user = service.authenticate("alice", "supersecret")
    assert user.username == "alice"

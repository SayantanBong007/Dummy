from services.user_service import UserService
from exceptions import UserNotFoundError, InvalidCredentialsError, UserAlreadyExistsError

service = UserService()


def register_route(username: str, password: str):
    try:
        user = service.register(username, password)
        return {"status": "created", "user_id": user.id}
    except UserAlreadyExistsError as e:
        return {"status": "error", "message": str(e)}


def login_route(username: str, password: str):
    try:
        user = service.authenticate(username, password)
        return {"status": "ok", "user_id": user.id}
    except (UserNotFoundError, InvalidCredentialsError):
        return {"status": "error", "message": "Invalid username or password"}

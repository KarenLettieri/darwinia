from domain.repositories.user_repository import UserRepository
from core.exceptions import UserNotWhitelistedError

class CheckWhitelist:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, telegram_id: str):
        user = self.user_repository.get_user_by_telegram_id(telegram_id)
        if user is None:
            raise UserNotWhitelistedError("El usuario no está en la whitelist.")
        return user

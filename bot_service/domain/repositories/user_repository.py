from abc import ABC, abstractmethod
from typing import Optional
from domain.entities.user import User

class UserRepository(ABC):
    @abstractmethod
    def get_user_by_telegram_id(self, telegram_id: str) -> Optional[User]:
        pass

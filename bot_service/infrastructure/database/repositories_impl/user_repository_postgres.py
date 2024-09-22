from domain.repositories.user_repository import UserRepository
from domain.entities.user import User

class UserRepositoryPostgres(UserRepository):
    def __init__(self, pool):
        self.pool = pool

    async def get_user_by_telegram_id(self, telegram_id: str) -> User:
        async with self.pool.acquire() as connection:
            row = await connection.fetchrow("SELECT * FROM users WHERE telegram_id = $1", telegram_id)
            if row:
                return User(telegram_id=row['telegram_id'])
            return None

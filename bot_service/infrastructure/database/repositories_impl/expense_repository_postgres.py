from domain.repositories.expense_repository import ExpenseRepository
from domain.entities.expense import Expense

class ExpenseRepositoryPostgres(ExpenseRepository):
    def __init__(self, pool):
        self.pool = pool

    async def add(self, expense: Expense):
        async with self.pool.acquire() as connection:
            await connection.execute(
                "INSERT INTO expenses (user_id, description, amount, category, added_at) VALUES ($1, $2, $3, $4, $5)",
                expense.user_id, expense.description, expense.amount, expense.category, expense.added_at
            )

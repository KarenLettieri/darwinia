from domain.entities.expense import Expense
from domain.repositories.expense_repository import ExpenseRepository

class AddExpense:
    def __init__(self, expense_repository: ExpenseRepository):
        self.expense_repository = expense_repository

    def execute(self, user_id: int, description: str, amount: float, category: str):
        expense = Expense(user_id, description, amount, category)
        self.expense_repository.add(expense)

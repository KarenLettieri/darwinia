from abc import ABC, abstractmethod
from domain.entities.expense import Expense

class ExpenseRepository(ABC):
    @abstractmethod
    def add(self, expense: Expense):
        pass

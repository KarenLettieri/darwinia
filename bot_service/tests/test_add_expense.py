import unittest
from domain.entities.expense import Expense
from domain.use_cases.add_expense import AddExpense

class MockExpenseRepository:
    def __init__(self):
        self.expenses = []

    def add(self, expense: Expense):
        self.expenses.append(expense)

class TestAddExpense(unittest.TestCase):
    def test_add_expense(self):
        repository = MockExpenseRepository()
        use_case = AddExpense(repository)

        use_case.execute(1, "Pizza", 20.0, "Food")

        self.assertEqual(len(repository.expenses), 1)
        self.assertEqual(repository.expenses[0].description, "Pizza")

if __name__ == '__main__':
    unittest.main()

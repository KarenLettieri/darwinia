from datetime import datetime

class Expense:
    def __init__(self, user_id: int, description: str, amount: float, category: str, added_at: datetime = None):
        self.user_id = user_id
        self.description = description
        self.amount = amount
        self.category = category
        self.added_at = added_at or datetime.now()

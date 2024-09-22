from core.constants import CATEGORIES

#This function takes a description of an expense and returns the category it belongs to.
def categorize_expense(description: str) -> str:
    description_lower = description.lower()
    for category in CATEGORIES:
        if category.lower() in description_lower:
            return category
    return "Other"

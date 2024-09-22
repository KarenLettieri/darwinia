from aiogram import types, Dispatcher
from core.utilities import categorize_expense
from core.exceptions import InvalidExpenseError, UserNotWhitelistedError
from domain.use_cases.add_expense import AddExpense
from domain.use_cases.check_whitelist import CheckWhitelist
from infrastructure.database.repositories_impl.user_repository_postgres import UserRepositoryPostgres
from infrastructure.database.repositories_impl.expense_repository_postgres import ExpenseRepositoryPostgres


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(handle_expense)

async def handle_expense(message: types.Message):
    telegram_id = message.from_user.id
    text = message.text

    pool = await create_db_pool()
    user_repository = UserRepositoryPostgres(pool)
    expense_repository = ExpenseRepositoryPostgres(pool)

    check_whitelist_use_case = CheckWhitelist(user_repository)
    add_expense_use_case = AddExpense(expense_repository)

    try:
        # Check if the user is whitelisted
        check_whitelist_use_case.execute(telegram_id)

        # Parse the expense to get the description and amount
        description, amount_str = text.rsplit(' ', 1)
        amount = float(amount_str)

        # Auto-categor
        category = categorize_expense(description)

        add_expense_use_case.execute(telegram_id, description, amount, category)

        await message.reply(f"{category} expense added ✅")

    except UserNotWhitelistedError:
        await message.reply("You're not authorized.")
    except InvalidExpenseError:
        await message.reply("Invalid format.")
    except Exception as e:
        await message.reply(f"Error: {e}")

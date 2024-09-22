from aiogram import Bot, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from app.bot_config import TELEGRAM_TOKEN
from infrastructure.telegram.bot_handler import register_handlers

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

# Middleware for logging
dp.middleware.setup(LoggingMiddleware())

# Start polling
def start_polling():
    register_handlers(dp)
    executor.start_polling(dp, skip_updates=True)

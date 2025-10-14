import os

from telegram import Update
from telegram.ext import Application, CommandHandler

import handlers


BOT_TOKEN: str = os.getenv("BOT_TOKEN")


def run_bot() -> None:
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("info", handlers.info))
    application.run_polling(allowed_updates=Update.ALL_TYPES)

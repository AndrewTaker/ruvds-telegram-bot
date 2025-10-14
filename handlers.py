import os
import locale
import logging
from datetime import datetime

from telegram import Update, constants
from telegram.ext import ContextTypes
from requests.exceptions import HTTPError

import ruvds


RUVDS_TOKEN: str = os.getenv("RUVDS_TOKEN")
SERVER_ID: str = os.getenv("SERVER_ID")
PAYMENT_URL: str = os.getenv("PAYMENT_URL")

logger = logging.getLogger("BOT")


async def info(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=constants.ChatAction.TYPING,
    )

    try:
        balance = ruvds.get_balance(RUVDS_TOKEN).get("amount")
        paid_till = ruvds.get_paid_untill(
            RUVDS_TOKEN,
            SERVER_ID,
        ).get("paid_till")
        cost = ruvds.get_server_cost(RUVDS_TOKEN, SERVER_ID).get("cost_rub")
    except HTTPError as e:
        logger.error(e)
        await update.message.reply_text(e)
        return
    except Exception as e:
        logger.error(e)
        await update.message.reply_text(e)
        return

    dt = datetime.fromisoformat(paid_till)
    paid_till_readable = dt.strftime("%d.%m.%Y")

    message = (
        f"сейчас: {balance}\n"
        f"оплачен до: {paid_till_readable}\n"
        f"стоимость: {cost}\n"
        f"ссылка для оплаты: {PAYMENT_URL}\n"
    )
    await update.message.reply_text(message)

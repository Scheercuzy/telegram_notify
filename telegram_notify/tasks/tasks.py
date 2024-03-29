import time

from telegram.bot import Bot
from telegram.error import NetworkError

from telegram_notify import celery
from telegram_notify import settings


@celery.task()
def send_message(chat_id, msg, retry=1):
    bot = Bot(settings.TOKEN)
    try:
        bot.send_message(
            chat_id=chat_id,
            text=msg)
    except NetworkError:
        if retry < 30:
            retry += 1
        time.sleep(retry)
        send_message.delay(chat_id, msg, retry=retry)
    return f"To: {chat_id}\n{msg}"

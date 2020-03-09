import time

from telegram.bot import Bot
from telegram.error import NetworkError

from telegram_notify.settings import Settings


def _send_message(chat_id, msg, retry=1):
    from telegram_notify.tasks import send_message
    bot = Bot(Settings.TOKEN)
    try:
        bot.send_message(
            chat_id=chat_id,
            text=msg)
    except NetworkError:
        if retry < 30:
            retry += 1
        time.sleep(retry)
        send_message.delay(chat_id, msg, retry=retry)

from flask import request

from telegram_notify.settings import Settings
from telegram_notify.tasks import send_message


def _index():
    if not request.is_json:
        return "Error, only accepts json"

    data = request.get_json()

    if "msg" not in data:
        return "Missing msg key"

    send_message.delay(Settings.CHAT_ID, data["msg"])
    return "Success"

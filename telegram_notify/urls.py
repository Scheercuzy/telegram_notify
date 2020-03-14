from flask import Blueprint
from flask import request

from telegram_notify import tasks
from telegram_notify.settings import Settings

blueprint = Blueprint("blueprint", __name__)


@blueprint.route('/', methods=['POST'])
def index():
    if not request.is_json:
        return "Error, only accepts json"

    data = request.get_json()

    if "msg" not in data:
        return "Missing msg key"

    tasks.send_message.delay(Settings.CHAT_ID, data["msg"])
    return "Success"

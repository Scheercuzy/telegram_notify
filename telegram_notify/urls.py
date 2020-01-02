from flask import Blueprint, request

from .settings import CHAT_ID
from .tasks import send_message

url = Blueprint("url", __name__)


@url.route('/', methods=['POST'])
def index():
    if not request.is_json:
        return "Error, only accepts json"

    data = request.get_json()

    if "msg" not in data:
        return "Missing msg key"

    send_message.delay(CHAT_ID, data["msg"])
    return "Success"

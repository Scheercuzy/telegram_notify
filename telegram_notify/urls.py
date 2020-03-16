from flask import Blueprint
from flask import request

from telegram_notify import tasks, Session
from telegram_notify.models import Person

blueprint = Blueprint("blueprint", __name__)


@blueprint.route('/', methods=['POST'])
def index():
    if not request.is_json:
        return "Error, only accepts json"

    data = request.get_json()

    if "msg" not in data:
        return "Missing msg key"

    session = Session()
    query = session.query(Person.chat_id).filter_by(access=True).all()
    if query:
        for chat_id in query:
            chat_id[0]
            tasks.send_message.delay(chat_id[0], data["msg"])
    return "Success"

from flask import Flask, request
from telegram_notify import CHAT_ID
from telegram_notify.bot import bot

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    if not request.is_json:
        return "Error, only accepts json"

    data = request.get_json()

    if "msg" not in data:
        return "Missing msg key"

    bot.send_message(
        chat_id=CHAT_ID,
        text=data["msg"])
    return "Success"

from flask import Flask, request
from telegram_notify import CHAT_ID
from telegram_notify.bot import bot

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    bot.send_message(
        chat_id=CHAT_ID,
        text=data["msg"])
    return "Success"

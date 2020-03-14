from telegram_notify import tasks


def start(update, context):
    tasks.send_message.delay(
        update.effective_chat.id,
        "I'm a bot, please talk to me!")

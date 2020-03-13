from telegram.ext import CommandHandler

from telegram_notify.bot import dispatcher


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, please talk to me!")


dispatcher.add_handler(
    CommandHandler('start', start))

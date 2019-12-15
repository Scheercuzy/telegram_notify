from telegram.ext import Updater, CommandHandler
from telegram_notify import TOKEN

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
bot = updater.bot


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, please talk to me!")


dispatcher.add_handler(
    CommandHandler('start', start))

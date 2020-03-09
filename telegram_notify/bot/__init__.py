from telegram.ext import Updater, CommandHandler

from telegram_notify.settings import Settings
from telegram_notify.bot import cmds


def make_updater():
    return Updater(token=Settings.TOKEN, use_context=True)


updater = make_updater()

dispatcher = updater.dispatcher

dispatcher.add_handler(
    CommandHandler('start', cmds.start))

from telegram.ext import CommandHandler

from telegram_notify import updater
from telegram_notify.bot import cmds


dispatcher = updater.dispatcher


dispatcher.add_handler(
    CommandHandler('start', cmds.start))
dispatcher.add_handler(
    CommandHandler('access', cmds.access))
dispatcher.add_handler(
    CommandHandler('revoke', cmds.revoke))

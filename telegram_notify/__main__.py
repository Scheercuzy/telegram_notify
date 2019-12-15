import logging
from telegram_notify import args
from telegram_notify.bot import updater
from telegram_notify.webserver import app


logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    updater.start_polling()
    if args.dev:
        app.run(host='localhost', port=8990)

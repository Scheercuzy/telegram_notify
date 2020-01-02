import logging
from telegram_notify import celery, updater
from telegram_notify.factory import create_app

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    app = create_app(celery=celery)
    updater.start_polling()
    app.run(port=8990)

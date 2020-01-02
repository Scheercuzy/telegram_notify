from telegram_notify.factory import create_app
from telegram_notify import celery  # noqa

webserver = create_app(celery=celery)

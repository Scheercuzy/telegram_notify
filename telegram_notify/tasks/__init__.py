from celery import Celery

from telegram_notify.settings import Settings
from telegram_notify.tasks import tasks


def make_celery():
    broker = f'redis://{Settings.REDIS_URL}:{Settings.REDIS_PORT}/0'
    backend = f'redis://{Settings.REDIS_URL}:{Settings.REDIS_PORT}/1'
    return Celery(backend=backend, broker=broker)


celery = make_celery()


@celery.task()
def send_message(chat_id, msg, retry=1):
    tasks._send_message(chat_id, msg, retry)

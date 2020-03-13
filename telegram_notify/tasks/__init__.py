from telegram_notify import celery

from telegram_notify.tasks import tasks


@celery.task()
def send_message(chat_id, msg, retry=1):
    tasks._send_message(chat_id, msg, retry)

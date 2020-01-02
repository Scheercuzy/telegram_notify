from celery import Celery
from telegram.ext import Updater

from .settings import TOKEN, REDIS_URL, REDIS_PORT


def make_celery():
    broker = f'redis://{REDIS_URL}:{REDIS_PORT}/0'
    backend = f'redis://{REDIS_URL}:{REDIS_PORT}/1'
    return Celery(backend=backend, broker=broker)


def make_updater():
    updater = Updater(token=TOKEN, use_context=True)
    return updater


celery = make_celery()
updater = make_updater()

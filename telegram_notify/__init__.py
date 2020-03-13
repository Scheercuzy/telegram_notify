import importlib
from flask import Flask
from celery import Celery
from telegram.ext import Updater

from telegram_notify.settings import Settings

# Setup app
app = Flask(__name__)

# Setup celery
celery = Celery(
    backend=f'redis://{Settings.REDIS_URL}:{Settings.REDIS_PORT}/0',
    broker=f'redis://{Settings.REDIS_URL}:{Settings.REDIS_PORT}/1'
)

# Setup celery in app
celery.conf.update(app.config)
TaskBase = celery.Task


class ContextTask(TaskBase):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return TaskBase.__call__(self, *args, **kwargs)


celery.Task = ContextTask

# Setup urls in app
app.register_blueprint(importlib.import_module('.urls', __name__).blueprint)


# Setup updater
updater = Updater(token=Settings.TOKEN, use_context=True)

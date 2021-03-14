import importlib
from flask import Flask
from celery import Celery
from telegram.ext import Updater
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from telegram_notify import settings
from telegram_notify.models import Base

# Setup app
app = Flask(__name__)


# Setup db
engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine
db_session_factory = sessionmaker(bind=engine)
Session = scoped_session(db_session_factory)


# Setup celery
celery = Celery(
    backend=f'redis://{settings.REDIS_URL}:{settings.REDIS_PORT}/0',
    broker=f'redis://{settings.REDIS_URL}:{settings.REDIS_PORT}/1'
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
updater = Updater(token=settings.TOKEN, use_context=True)

importlib.import_module('.bot', __name__)

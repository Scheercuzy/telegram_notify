from flask import Flask
from telegram_notify.tasks import celery
from telegram_notify.urls import blueprint

app = Flask(__name__)

# Setup celery
celery.conf.update(app.config)
TaskBase = celery.Task


class ContextTask(TaskBase):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return TaskBase.__call__(self, *args, **kwargs)


celery.Task = ContextTask

# Setup urls
app.register_blueprint(blueprint)

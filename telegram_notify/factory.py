from flask import Flask
import os

PKG_NAME = os.path.dirname(os.path.realpath(__file__)).split("/")[-1]


def create_app(**kwargs):
    app = Flask(__name__)
    if kwargs.get("celery"):
        init_celery_for_flask(kwargs.get("celery"), app)
    from .urls import url
    app.register_blueprint(url)
    return app


def init_celery_for_flask(celery, app):
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask

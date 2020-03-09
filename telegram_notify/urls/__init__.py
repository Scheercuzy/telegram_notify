from flask import Blueprint

from telegram_notify.urls import urls

blueprint = Blueprint("blueprint", __name__)


@blueprint.route('/', methods=['POST'])
def index():
    return urls._index()

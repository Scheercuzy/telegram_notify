from sqlalchemy.orm.exc import NoResultFound

from telegram_notify import tasks, Session

from telegram_notify.models import Person
from telegram_notify.settings import Settings


def start(update, context):
    session = Session()
    chat_id = update.effective_chat.id
    exists = session.query(Person.chat_id).filter_by(
        chat_id=chat_id).scalar() is not None
    if exists:
        tasks.send_message.delay(
            chat_id,
            "Welcome back")
    else:
        session.add(Person(chat_id=chat_id))
        session.commit()
        tasks.send_message.delay(
            chat_id,
            "Welcome newcomer"
        )
    Session.remove()


def access(update, context):
    args = context.args
    chat_id = update.effective_chat.id
    if args:
        if args[0] == Settings.ACCESS_TOKEN:
            session = Session()
            try:
                person = session.query(Person).filter_by(chat_id=chat_id).one()
            except NoResultFound:
                tasks.send_message.delay(
                    chat_id,
                    'You need to registry with /start first')
                Session.remove()
                return
            person.access = True
            session.commit()
            Session.remove()
            tasks.send_message.delay(
                chat_id,
                'Access granted')
        else:
            tasks.send_message.delay(
                chat_id,
                'Wrong access token')
        return

    tasks.send_message.delay(
        chat_id,
        'Access comands requires an argument')


def revoke(update, context):
    chat_id = update.effective_chat.id
    session = Session()
    try:
        person = session.query(Person).filter_by(chat_id=chat_id).one()
    except NoResultFound:
        tasks.send_message.delay(
            chat_id,
            'You need to registry with /start first')
        Session.remove()
        return
    if person.access:
        person.access = False
        session.commit()
        tasks.send_message.delay(
            chat_id,
            'Access revoked')
    else:
        tasks.send_message.delay(
            chat_id,
            "You didn't have access to begin with")
    Session.remove()

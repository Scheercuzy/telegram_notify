from telegram_notify import tasks, Session

from telegram_notify.models import Person


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

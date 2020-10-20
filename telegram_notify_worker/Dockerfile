FROM python:3.6

COPY . /app

RUN pip install /app

WORKDIR /config

ENV REDIS_PORT 6379

CMD [ "celery", "-A", "telegram_notify:celery", "worker", "-l", "INFO" ]
FROM python:3.6

COPY . /app

RUN pip install /app

WORKDIR /config

ENV REDIS_PORT 6379

CMD [ "telegram_notify", "--bot" ]
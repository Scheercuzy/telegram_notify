FROM python:3.6

COPY . /app

WORKDIR /app

RUN pip install .

ENV REDIS_PORT 6379

CMD [ "celery", "-A", "wsgi:celery", "worker", "-l", "INFO" ]
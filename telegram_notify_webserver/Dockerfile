FROM python:3.6

COPY . /app

RUN pip install /app

EXPOSE 8990

WORKDIR /config

ENV REDIS_PORT 6379

CMD [ "uwsgi", "--chdir", "/app", "--ini", "/app/webserver.ini" ]
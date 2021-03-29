FROM python:3.6

COPY . /app

COPY supervisord.conf /etc/supervisord.conf

RUN apt-get update -y && apt-get install redis -y

RUN pip install /app

EXPOSE 8990

WORKDIR /config

ENV REDIS_PORT 6379

ENV PYTHONPATH /app

CMD ["/usr/local/bin/supervisord"]
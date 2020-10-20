# telegram-notify

## Install

You must have pipenv and use systemd to follow these instructions

```bash
cd telegram_notify
pipenv install
```

Make sure Redis server is running on your server

Configure webserver.ini 

Configure the service files on systemd

- use the help of pipenv --venv to figure the location of the virtualenv of your project

Run the following commands to start the services

```bash
sudo systemctl start ${PWD}/systemd/telegram_notify_webserver.service
sudo systemctl start ${PWD}/systemd/telegram_notify_celery.service
sudo systemctl start ${PWD}/systemd/telegram_notify_bot.service
```

You can then enable them if you wish to do so by running 

```bash
sudo systemctl enable telegram_notify_webserver.service
sudo systemctl enable telegram_notify_celery.service
sudo systemctl enable telegram_notify_bot.service
```

## Curl

```bash
curl -H "Content-Type: application/json" -XPOST http://localhost:8990 -d '{"msg": "test"}'
```

## Docker

### Building Images 

webserver

```bash
docker build . -f telegram_notify_webserver/Dockerfile --tag telegram_notify_webserver:latest
```

worker

```bash
docker build . -f telegram_notify_worker/Dockerfile --tag telegram_notify_worker:latest
```

#### Running Images

You need a redis container running first

```bash
docker run --name redis -p 6379:6379 -d redis
```

webserver

```bash
docker run --name telegram_notify_webserver --env-file ./.env -p 8990:8990 --rm telegram_notify_webserver:latest
```

webserver

```bash
docker run --name telegram_notify_worker --env-file ./.env --rm telegram_notify_worker:latest
```

Required environment variables:

```text
TELEGRAM_TOKEN=
ACCESS_TOKEN=

REDIS_URL=redis
REDIS_PORT=6379
```

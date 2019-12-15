# telegram-notify



## Install

You must have pipenv and use systemd to follow these instructions

```
cd telegram_notify
pipenv install
```

Configure webserver.ini 

Configure the service files on systemd
- use the help of pipenv --venv to figure the location of the virtualenv of your project

Run the following commands to start the services

```
sudo systemctl start ${PWD}/systemd/telegram_notify_webserver.service
sudo systemctl start ${PWD}/systemd/telegram_notify_bot.service
```

You can then enable them if you wish to do so by running 

```
sudo systemctl enable telegram_notify_webserver.service
sudo systemctl enable telegram_notify_bot.service
```


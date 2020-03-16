import os


class Settings:
    TOKEN = os.environ['TELEGRAM_TOKEN']

    REDIS_URL = 'localhost'
    REDIS_PORT = 6379

    ACCESS_TOKEN = os.environ['ACCESS_TOKEN']

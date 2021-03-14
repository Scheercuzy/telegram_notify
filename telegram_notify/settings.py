import os
from dotenv import load_dotenv

if os.path.exists('.env'):
    load_dotenv('.env')

# Telegram
TOKEN = os.environ['TELEGRAM_TOKEN']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
# Redis
REDIS_URL = os.environ['REDIS_URL']
REDIS_PORT = os.environ['REDIS_PORT']

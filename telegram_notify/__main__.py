import logging
import argparse

from telegram_notify import app, updater

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--web', action='store_true')
group.add_argument('--bot', action='store_true')
args = parser.parse_args()

if args.web:
    print("Only webserver running")
    app.run(port=8990)

if args.bot:
    print("Only bot running")
    updater.start_polling()
    updater.idle()

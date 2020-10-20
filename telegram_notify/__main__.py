import logging
import argparse
import sys

from telegram_notify import app, updater, engine
from telegram_notify.models import Base

logging.basicConfig(level=logging.INFO)


def parse_args(args):
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('--web', action='store_true')
    group.add_argument('--bot', action='store_true')
    return parser.parse_args(args)


def main():
    args = parse_args(sys.argv[1:])

    Base.metadata.create_all(engine)

    if args.web:
        print("Running dev webserver")
        app.run(port=8990)

    if args.bot:
        print("Running Bot")
        updater.start_polling()
        updater.idle()


if __name__ == "__main__":
    main()

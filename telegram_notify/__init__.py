import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--dev', action='store_true')
args = parser.parse_args()

TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = os.environ['CHAT_ID']

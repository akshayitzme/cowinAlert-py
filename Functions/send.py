import requests
from time import time, sleep
from config import BOT_TOKEN

TelegramEndpoint = 'https://api.telegram.org/bot{}/sendMessage'.format(BOT_TOKEN)
def send(chatId, msg):
    params = {'chat_id': chatId, 'text': msg, 'parse_mode': 'html'}
    sleep(0.05)
    requests.get(url=TelegramEndpoint, params=params)
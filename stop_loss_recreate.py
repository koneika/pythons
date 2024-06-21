# -*- coding: utf-8 -*-
import telebot
from telebot import types
import json
import time

import requests
api = "7048609406:AAEhqRof2NAUVaiKgBH3xANwBjONKl2u3cg"
bot = telebot.TeleBot(api)

arr = ['EQBCoynGYslAMjv_gRl_2_B1KMOvh9ZW-ae0p7SaXZy6KFjY'] # да сюда нажо с джавы стырить чёто, надо автообновляющую базу данных сюда прикрепить

token = 'EQBCoynGYslAMjv_gRl_2_B1KMOvh9ZW-ae0p7SaXZy6KFjY'

myUsername = 1111655025
link = f'https://api.geckoterminal.com/api/v2/networks/ton/tokens/{token}'


r = requests.get(link, headers = {'accept': 'application/json'})
data = r.json()
save_price_usd = data['data']['attributes']['price_usd']



myUsername = 1111655025


    @bot.message_handler(commands=[data['data']['attributes']['symbol']])
    def start_message(message):

        r = requests.get(link, headers = {'accept': 'application/json'})

        data = r.json()
        # print(data)
        price_usd = data['data']['attributes']['price_usd']
        # print(data['data']['attributes']['symbol'])
        txt = f"Price in USD: {price_usd}, and {(float(price_usd)/float(save_price_usd))*100}%"
        # print(txt)
        bot.send_message(myUsername, txt)

if __name__ == '__main__':
    bot.infinity_polling()


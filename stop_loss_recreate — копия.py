import json
import time

import requests

myUsername = 1111655025
@bot.message_handler(commands=['goi2'])
def start_message(message):
# while True:
    # time.sleep(15)
    link = 'https://api.geckoterminal.com/api/v2/networks/ton/tokens/EQBCoynGYslAMjv_gRl_2_B1KMOvh9ZW-ae0p7SaXZy6KFjY'

    r = requests.get(link, headers = {'accept': 'application/json'})

        bot.send_message(myUsername, "bot started")
    data = r.json()

    price_usd = data['data']['attributes']['price_usd']

    print(f"Price in USD: {price_usd}")


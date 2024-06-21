import requests
from bs4 import BeautifulSoup
import time
import json
import subprocess
import telebot


token = "6462288711:AAEq4cLo9zDh8iNXdXS0w9SeocKxRbpKk_4"
bot = telebot.TeleBot(token)
stop_loss = 0.2445
# Замените EQDqz7LTwgj016kiTiSooM_ft8kveL2P4pj4fkJmsUV_an_X на адрес вашего токена
token_address = "EQDqz7LTwgj016kiTiSooM_ft8kveL2P4pj4fkJmsUV_an_X"

# Создайте команду curl
command = f"curl -X GET https://api.geckoterminal.com/api/v2/networks/ton/tokens/{token_address}/pools?page=1 -H 'accept: application/json'"

# Запустите команду и получите вывод

# def load():
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
output, error = process.communicate()

# load()

# Проверьте наличие ошибок
while True:
    if error:
        print(f"Ошибка: {error}")
    else:
        # Преобразуйте вывод в JSON
        data = json.loads(output.decode('utf-8'))

        # Обработайте данные
        for pool in data['data']:
                pool_id = pool['id']


                pool_name = pool['attributes']['name']
                price_usd = pool['attributes']['base_token_price_usd']
                volume_usd = pool['attributes']['volume_usd']['h24']
                # print(str(pool_id) + str(pool_id) + str(pool_id))
                if str(pool_id) in "ton_EQBb8kl4N3C0xr_U00Tc84Ipm0juApDUZlW0F0SbrqXJXdjY":
                    
                        # print(f"Pool ID: {pool_id}")
                        # print(f"Pool Name: {pool_name}")
                        # print(f"Price (USD): {price_usd}")
                        # print(f"Volume (USD): {volume_usd}")
                        # print("-------------------------")
                        time.sleep(15)
                        
                        if float(price_usd) < stop_loss:
                            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
                            output, error = process.communicate()

                            print(r"\U+2705 {price_usd} stop_loss less than - {stop_loss}")
                            bot.send_message(1111655025, r"\U+2705 {price_usd} stop_loss less than - {stop_loss}")

                        else:
                            
                            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
                            output, error = process.communicate()
                            
                            print(r"\U+26D4 {price_usd} stop_loss less than - {stop_loss}")
                            bot.send_message(1111655025, r"\U+26D4 {price_usd} stop_loss less than - {stop_loss}")
                            # print(float(price_usd), "ne ban")
                            # bot.send_message(message.from_user.id, fix_it)



                

# print("send a link of graph from geckoterminal",
# "\nfor example like: https://www.geckoterminal.com/ton/pools/EQBb8kl4N3C0xr_U00Tc84Ipm0juApDUZlW0F0SbrqXJXdjY",
# "\nor write just a contract")

# geckoTerminal = str(input())
# geckoTerminal = "https://api.geckoterminal.com/api/v2/networks/ton/tokens/EQDqz7LTwgj016kiTiSooM_ft8kveL2P4pj4fkJmsUV_an_X/pools?page=1"

# def logic(geckoTerminal):
#     response = requests.get(geckoTerminal)
    
#     html_content = response.content
#     soup = BeautifulSoup(html_content, 'html.parser')
#     print(response.text)

    

#     response_data = json.loads(response.content)

#     pools = response_data['data']
#     for pool in pools:
#         pool_id = pool['id']
#         pool_name = pool['attributes']['name']
#         price_usd = pool['attributes']['base_token_price_usd']
#         volume_usd = pool['attributes']['volume_usd']['h24']

#         print(f"Pool ID: {pool_id}")
#         print(f"Pool Name: {pool_name}")
#         print(f"Price (USD): {price_usd}")
#         print(f"Volume (USD): {volume_usd}")
#         print("-------------------------")

#         with open('geckoterminal_data.json', 'w') as f:
#             json.dump(response_data, f)

# if "https://www.geckoterminal.com/ton/pools/" in geckoTerminal:
#     """working code"""
    
#     logic(geckoTerminal)
    

# elif(len(geckoTerminal) == 48):
#     """working code"""
#     geckoTerminal = "https://www.geckoterminal.com/ton/pools/" + geckoTerminal

#     logic(geckoTerminal)
    
# else:
#     print("its not a contract or not contains a link of graph from geckoterminal",
#     "\nmake sure the first link contains https://www.geckoterminal.com/ton/pools/")
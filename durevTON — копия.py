import re
from selenium import webdriver
import time
import telebot

token = '7053594101:AAE2ZaCg_i6rt7dALqC6ixmkZKpIyQRpLDU'
bot = telebot.TeleBot(token)
myUsername = 1111655025

print("UBEDITELNAYA PROSBA, PROVER INTENET PREZDE CHEM TI BUDESH VKLUCHAT BOTA \n")
print("UBEDITELNAYA PROSBA, PROVER INTENET PREZDE CHEM TI BUDESH VKLUCHAT BOTA \n")
print("UBEDITELNAYA PROSBA, PROVER INTENET PREZDE CHEM TI BUDESH VKLUCHAT BOTA \n")

bot.send_message(myUsername, 'bot started')



url = "https://www.geckoterminal.com/ton/pools/EQCCsJOGdUdSGq0ambJFgSptdHfDPkaQlKlLIKTqtazhhcps"

# Запуск веб-драйвера (необходимо скачать драйвер для вашего браузера)
driver = webdriver.Chrome()  # Здесь используется Chrome, но можно использовать и другие браузеры

# Получение содержимого страницы
driver.get(url)

# Вывод содержимого страницы
# time.sleep(15)
while True:
    time.sleep(5)

    index_of_dollar = driver.page_source.find('$')
    if index_of_dollar != -1:  # Если доллар найден
        
        seven_chars_after_dollar = driver.page_source[index_of_dollar + 1:index_of_dollar + 8]
        print("$", seven_chars_after_dollar)
    else:
        print("чёто сдохло")

    # print(driver.page_source)

# Закрытие браузера
driver.quit()

# @bot.message_handler(commands=['start', 'help'])
#         def start_message(message):
#             bot.send_message(myUsername, 
#                             "/report или /admin - сообщить об нарушении\n"+
#                             "коммандой спамить - ЗАПРЕЩЕНО")
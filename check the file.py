#import telebot
from selenium import webdriver
import time

#print("UBEDITELNAYA PROSBA, PROVER INTENET PREZDE CHEM TI BUDESH VKLUCHAT BOTA \nUBEDITELNAYA PROSBA, PROVER INTENET PREZDE CHEM TI BUDESH VKLUCHAT BOTA \nUBEDITELNAYA PROSBA, PROVER INTENET PREZDE CHEM TI BUDESH VKLUCHAT BOTA \n")

print("write a link of graph")
url = str(input())

#myUsername = 1111655025
#token = '7053594101:AAE2ZaCg_i6rt7dALqC6ixmkZKpIyQRpLDU'
#bot = telebot.TeleBot(token)

# Запуск веб-драйвера (необходимо скачать драйвер для вашего браузера)
driver = webdriver.Firefox()

# Здесь используется Chrome, но можно использовать и другие браузеры

# Получение содержимого страницы
driver.get(url)


# print(driver.page_source)

# Поиск первого вхождения "$"

word = '><title>durev'

print(len(word), "\n", driver.page_source)

# index_of_dollar = driver.page_source.find(word)
time.sleep(999)
# Если доллар найден
# while True:
#     if index_of_dollar != -1:
        
#         # Вывод семи символов после первого доллара
#         seven_chars_after_dollar = driver.page_source[index_of_dollar + len(word):index_of_dollar + len(word) + 10]
#         if "$" in seven_chars_after_dollar:
#             # print(bot.send.message())
#             bot.send_message(myUsername, seven_chars_after_dollar)
#             time.sleep(60)
#     else:
#         print("Error, cant find a word")
# # Закрытие браузера
# driver.quit()
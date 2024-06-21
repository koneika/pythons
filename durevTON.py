import telebot
from selenium import webdriver
import time
import socket

print("UBEDITELNAYA PROSBA, PROVER INTENET PREZDE CHEM TI BUDESH VKLUCHAT BOTA \nUBEDITELNAYA PROSBA, PROVER INTENET PREZDE CHEM TI BUDESH VKLUCHAT BOTA \nUBEDITELNAYA PROSBA, PROVER INTENET PREZDE CHEM TI BUDESH VKLUCHAT BOTA \n")

url = "https://www.geckoterminal.com/ton/pools/EQCCsJOGdUdSGq0ambJFgSptdHfDPkaQlKlLIKTqtazhhcps"

myUsername = 1111655025
token = '6917856911:AAEeYChPuM-_NkRYRFtNtn_e_rtYqb1pNFA'
bot = telebot.TeleBot(token)

# Запуск веб-драйвера (необходимо скачать драйвер для вашего браузера)
driver = webdriver.Firefox()

# Здесь используется Chrome, но можно использовать и другие браузеры

# Получение содержимого страницы
driver.get(url)


# print(driver.page_source)

# Поиск первого вхождения "$"

word = 'leading-none\"><span>$'

print(len(word))



# Если доллар найден
while(True):
    def check_internet_connection(host="8.8.8.8", port=53, timeout=3):
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except socket.error:
            return False

    if check_internet_connection():
        index_of_dollar = driver.page_source.find(word)
        target = driver.page_source[index_of_dollar + len(word):index_of_dollar + len(word) + 8]
        if(index_of_dollar != -1):
            while not("<" in target or "/" in target or "s" in target or "p" in target or "a" in target or "n" in target or ">" in target):
            #if not("<" in target or ">" in target or "n" in target or "$>" in target or "</" in target):
            # Вывод семи символов после первого доллара
                seven_chars_after_dollar = driver.page_source[index_of_dollar + len(word):index_of_dollar + len(word) + 8]
                fix_it = str("$") + str(seven_chars_after_dollar)
                    #if "$" in seven_chars_after_dollar:
                        # print(bot.send.message())
                bot.send_message(myUsername, fix_it)
                time.sleep(45)

        else:
            print("Error, cant find a word")
# Закрытие браузера
driver.quit()

#######################################################почистить зубы
#######################################################почистить зубыы
#######################################################почистить зубы




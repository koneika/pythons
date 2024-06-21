# -*- coding: utf-8 -*-

import telebot
from telebot import types
import time

myUsername = 1111655025
token = '7006992799:AAH19FiYzQcuIDRi_MRiN92ZfT8Ol20HuE8'
bot = telebot.TeleBot(token)

print("vvedite kolichestvo")
choose = int(input())
print("bot started")

ttime = [0] * choose

for i in range(0, choose):
    print(f"vvedite time{i} in hour(s)")
    ttime[i] = int(input())

startedTime = time.time()
# timer = [1] * choose

hour = 3
breaktime = 3

bot.send_message(myUsername, 'bot started')

while True: 
    print((int(time.time()))-(int(time.time())), " == ", (int(startedTime))-(int(startedTime)) + int((hour * ttime[i])))
    print("startedTime = ", int(startedTime))
    time.sleep(1)
    for i in range (0, choose):
        if int(time.time()) == int(startedTime) + int((hour * ttime[i]))):
            bot.send_message(myUsername, '{i}zaidite za nagardoy @1111655025, u vas est 5 minut') #      
            time.sleep(breaktime)
            bot.send_message(myUsername, "vremya vishlo")

            startedTime += (hour * ttime[i]) + breaktime






























    # if(int(time.time()) == int(startedTime + hour*3))

# if __name__ == '__main__':
#     bot.infinity_polling() ## �� ��� ���� ����� �� while(True)
# if message.text == 'lol':
#     bot.send_message(myUsername, "bot is started")


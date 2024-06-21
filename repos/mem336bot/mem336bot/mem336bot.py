# -*- coding: utf-8 -*-
import subprocess

subprocess.run(["pip", "install", "pyTelegramBotAPI"])

import telebot
from telebot import types
import time

myUsername = 1111655025
token = '7006992799:AAH19FiYzQcuIDRi_MRiN92ZfT8Ol20HuE8'
bot = telebot.TeleBot(token)

choose = 2

startedTime = time.time()
timer = [1] * choose

hour = 3600
breaktime = 300
counter = 0

bot.send_message(myUsername, 'bot started')








while(True): 
    time.sleep(1)

    ttime = 2

    
    counter += 1
    print(int(time.time()), " ", int(startedTime) + int((hour*ttime))*int(timer[0]))
    if int(time.time()) == int(startedTime) + int((hour*ttime))*int(timer[0]):
        
        #send a message
        bot.send_message(myUsername, '1zaidite za nagardoy @1111655025, u vas est 5 minut') #      
        
        timer[0] += 1
        
        # stop program by breaktime
        time.sleep(breaktime)
        # send a message that your time is done
        bot.send_message(myUsername, "vremya vishlo")
    
        timer[0] += ttime
     # second one # second one # second one # second one # second one # second one # second one # second one # second one # second one 































    # if(int(time.time()) == int(startedTime + hour*3))

# if __name__ == '__main__':
#     bot.infinity_polling() ## �� ��� ���� ����� �� while(True)
# if message.text == 'lol':
#     bot.send_message(myUsername, "bot is started")


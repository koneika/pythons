# -*- coding: utf-8 -*-

import telebot
from telebot import types
import time

myUsername = 1111655025
token = '7006992799:AAH19FiYzQcuIDRi_MRiN92ZfT8Ol20HuE8'
bot = telebot.TeleBot(token)
print("UBEDITELNAYA PROSBA, PROVER INTENET PREZDE CHEM TI BUDESH VKLUCHAT BOTA \n")
print("UBEDITELNAYA PROSBA, PROVER INTENET PREZDE CHEM TI BUDESH VKLUCHAT BOTA \n")
print("UBEDITELNAYA PROSBA, PROVER INTENET PREZDE CHEM TI BUDESH VKLUCHAT BOTA \n")

print("vvedite kolichestvo")
choose = int(input())
print("bot started")

ttime = [0] * choose

save = [0] * choose

minusttime = [0] * choose

for i in range(0, choose):
    print(f"vvedite soobshenie №{i+1}")
    save[i] = str(input())

    print(f"vvedite time{i} by hour(s)")
    ttime[i] = int(input())

    print(f"calibrovka, naprimer vi postavili 24 chasa, a next nagrada bedet chere 12, topishite 12 by hour(s)")
    minusttime[i] = int(input())

for i in range(0, choose):
    print(save[i])
    print(ttime[i])

startedTime = [time.time()] * choose
# timer = [1] * choose

hour = 3600
breaktime = 300

bot.send_message(myUsername, 'bot started')


with open("save.txt", 'w') as f:
    for i in range(0, choose):
        f.write(f"{minusttime[i]} {choose} {ttime[i]} {save[i]}\n")


while True:
    time.sleep(1)
    
    # for i in range(0, choose):
    #     print(int(time.time()), " == ", int(startedTime[i]) + int((hour * ttime[i])))

    for i in range(0, choose):
        if int(time.time()) == (int(startedTime[i]) + int((hour * ttime[i])+i))-minusttime[i]:

            bot.send_message(myUsername, save[i])
            
            startedTime[i] += int((hour * ttime[i])-i)

            # then reset minus time
            minusttime[i] = 0






























    # if(int(time.time()) == int(startedTime + hour*3))

# if __name__ == '__main__':
#     bot.infinity_polling() ## �� ��� ���� ����� �� while(True)
# if message.text == 'lol':
#     bot.send_message(myUsername, "bot is started")


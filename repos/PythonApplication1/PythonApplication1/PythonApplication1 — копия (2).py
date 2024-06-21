# -*- coding: utf-8 -*-
import telebot
from telebot import types

token = '6790162522:AAFbanzvZFLUDfQrWsHmL_-LUMlvki1D7As'
bot = telebot.TeleBot(token)



@bot.message_handler(content_types=['text'])
def repeat_all_message(message):
    chatLogID = -1002088831304
    myUsername = 1111655025

    userID = message.from_user.id
    username = message.from_user.username
    txt = message.text

    name = message.from_user.first_name
    name2 = message.from_user.last_name
    # if name2 == "None":
    #     name2 = ""
    def toChat():
        bot.send_message(chatLogID, "[test]" +str(message.from_user.id) + " " + "@" +str(message.from_user.username)  
        + " " +str(message.from_user.first_name) + " " +str(message.from_user.last_name) + " " +txt)

    def toMe():
        bot.send_message(myUsername, str(message.from_user.id) + " " + "@" +str(message.from_user.username)  
        + " " +str(message.from_user.first_name) + " " +str(message.from_user.last_name) + " " +txt)

    count = 0
    ban = False
    #, 
    # banWord = ['хуй', 'пиз', 'хуя', 'ебе', 'ебё', 'ебя', 'ебу', 'еба', 'еби', 'пох', 'бля', 'нах', 'сук', 'лох']
    
    banWord = ['хуй', 'пон', 'ебе', 'ебё', 'сук', 'нах', 'лох', 'ебу', 'еби', 'еба', 'хуя', 'пиз', 'даун']
    stackoverflow = len(banWord)
    NoBanWord = ['теб', 'тебе', 'тебя'] + [' ']*stackoverflow # проблема маленькая
    stackoverflow = len(NoBanWord)
    banWord = ['хуй', 'пон', 'ебе', 'ебё', 'сук', 'нах', 'лох', 'ебу', 'еби', 'еба', 'хуя', 'пиз', 'даун'] + [' ']*stackoverflow # проблема маленькая

    txt2 = txt.split()

    # for k in range (0, len(k)):
    for j in range (0, len(banWord)):
         for i in range (0, len(txt2)):
             #or txt2[i] in banWord[j].upper() or txt2[i] in banWord[i].upper()
             if banWord[j].upper() in txt2[i].upper():
                 if NoBanWord[j].upper() in txt2[i].upper():
                    ban = False
                    print("false")
                 else:
                    ban = True
                    print("true")


                





        

    print(txt,'\n', ban)
    if ban == True:
        # toChat()
        toMe()
    # второй способ по жёще, он рабочий, но надо каким то боком придумать защиту, чтоб не банил за теб, поход и тд, это немного сложнее чем кажется\
    # можно попробовать через спли пробовать обнаружить банворд, и анбан ворд, таким методом мы сможем понять, а стоит ли банить
    # в общем это пока всё сложно, и требует умственной работы

if __name__ == '__main__':
    bot.infinity_polling()
    













































        # for j in range(0, len(txt2)):
    #     for i in range(0, len(banWord)):
    #         if banWord[i] in txt2[j]:
    #             if NoBanWord[i] in txt2[j]:
    #                 ban = False
    #             else:
    #                 ban = True


                    # print("banword")
                # ban = True
                # for i in range(0, len(NoBanWord)):
                #     if NoBanWord[i] in txt2[j] or txt2[j] in NoBanWord[i]:
                #                 print("banword")
                #                 ban = False
                # for j in range(0, len(txt2)):
                #     for i in range(0, len(NoBanWord)):
                        
    
    # if ban == True:
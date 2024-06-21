# -*- coding: utf-8 -*-
import telebot
from telebot import types
import time

token = '6790162522:AAFbanzvZFLUDfQrWsHmL_-LUMlvki1D7As'
bot = telebot.TeleBot(token)

chatLogID = -1002088831304
myUsername = 1111655025



# @bot.message_handler(commands=['stop'])
# def stop_bot(message):
#     if message == "/start":
#         print("запуск")
bot.send_message(chatLogID, "бот запущен")
bot.send_message(myUsername, "бот запущен")

@bot.message_handler(commands=['start', 'help'])
def start_message(message):
     bot.send_message(message.chat.id, 
                      "/report - сообщить об нарушении\n"+
                      "/language - поменять язык\n"+
                      "/add - добавить список запрещённых\nслов и не запрещённых\n"+
                      "/more - куда писать команды?")

newTime = time.time()
# print(str(int(newTime)) + "==" +str(int(newTime)))
@bot.message_handler(commands=['report'])
def report(message):
    global newTime
    if int(newTime) < int(time.time()):    
        bot.send_message(chatLogID, "[test]" +str(message.from_user.id) + " " + "@" +str(message.from_user.username)  
        + " " +str(message.from_user.first_name) + " " +str(message.from_user.last_name) + " " +message.text)
        bot.send_message(chatLogID, "@koneika336" + " @KGB1986g")
        bot.send_message(chatLogID, "Отправлено")
        newTime += 60
        # print(str(int(newTime)) + "==" +str(int(newTime)))

@bot.message_handler(commands=['add'])

#fstream

def add(message):
    bot.send_message(chatLogID, "будет по очерёдно, сначало запрещённые слова, потом исключения для них, пример:\n"+
                     "запрещённые слова:\n"
                     "  лох пон пох\n"+
                     "исключения для них:\n"+
                     "  плохо понял поход\n")
    # @bot.message_handler(content_types=['text'])
    # def answer(message):
    #     bot.send_message(chatLogID, "настроено")
    #     return True
    
    
@bot.message_handler(content_types=['text'])
def repeat_all_message(message):
    

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
    
    #fstream
    banWord = ['хуй', 'ебе', 'ебё', 'сук', 'нах', 'ебу', 'еби', 'еба', 'хуя', 'пиз', 'даун', 'бля', 'долбаёб', 'долбаеб']
    stackoverflow = len(banWord)
    NoBanWord = ['теб', 'тебе', 'тебя'] + [' ']*stackoverflow # проблема маленькая
    stackoverflow = len(NoBanWord)
    banWord = ['хуй', 'ебе', 'ебё', 'сук', 'нах', 'ебу', 'еби', 'еба', 'хуя', 'пиз', 'даун', 'бля', 'долбаёб', 'долбаеб'] + [' ']*stackoverflow # проблема маленькая

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


                





        
    # add(message)
    print(txt,'\n', ban)
    if ban == True:
        toChat()
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
import telebot
from telebot import types

token = '6790162522:AAFbanzvZFLUDfQrWsHmL_-LUMlvki1D7As'
bot = telebot.TeleBot(token)



@bot.message_handler(content_types=['text'])
def repeat_all_message(message):
    chatLogID = -1002088831304 # куда отправлять ему сообщения
    userID = message.from_user.id
    username = message.from_user.username
    txt = message.text

    name = message.from_user.first_name
    name2 = message.from_user.last_name

    def toChat():
        bot.send_message(chatLogID, "[test]" +str(message.from_user.id) +"" + " " + "@" +str(message.from_user.username)  
        + " " +str(message.from_user.first_name) + " " +str(message.from_user.last_name) + " " +txt)

    def toMe():
        bot.send_message(1111655025, str(message.from_user.id) +" @koneika336" + " " + "@" +str(message.from_user.username)  
                    + " " +str(message.from_user.first_name) + " " +str(message.from_user.last_name) + " " +txt)

    count = 0
    ban = False

    banWord = ["хуй", "пиз", "хуя", "ебе", "ебё", "ебя", "ебу", "еба", "еби", "пох", "бля", "нах", "сук", "лох"]
    NoBanWord = ["теб"]

    txt2 = txt.split()




    # # счёт всего банворда массива
    # for i in range(0, len(banWord)):
    #     # поиск в тексте банворд слово
    #     if banWord[i] in txt:
    #         # если есть, бан
    #         ban = True
    #         for i in range(0, len(NoBanWord)):
    #             for j in range(0, len(txt2)):
    #                 if NoBanWord[i] in txt2[j]:
    #                     ban = False
    #                     print("может тут конец света")
    #                     for j in range(0, len(txt2)):
    #                         for i in range(0, len(banWord)):
    #                             print("фалсе")
    #                             if ban == False:
    #                                 print("тру")
    #                                 if banWord[i] == txt2[j]:
    #                                     ban = Fasle
    #                                 else:
    #                                     ban = True
                                        
    #                     return False
    #                 else:
    #                     ban = True
        # else:
    










    for j in range(0, len(txt2)):
        for i in range(0, len(banWord)):
            print(txt2[j], " ", banWord[i])
            if txt2[j] in banWord[i] or banWord[i] in txt2[j]: #or txt2 in banWord[i]
                ban = True
                print("труеееееееее")
                for j in range(0, len(txt2)):
                    
                    for i in range(0, len(NoBanWord)):
                        print(txt2[j], " ", NoBanWord[i])
                        if txt2[j] in NoBanWord[i] and NoBanWord[i] in txt2[j]:
                            ban = False
                            print("фалсе?")
                        else:
                            ban = True
                            print("тру?")
            # else:
            #     for i in range(0, len(banWord)):
            #         print(i)
            #         if str(txt2) in banWord[i]:
            #             ban = True
            #             print("фалсе1")
            #         else:
            #             ban = False
            #             print("труе1")

















    print(txt2)
    print(ban)
    # for k in range(0, len(banWord)):
    #     for j in range(0, len(txt2)):
    #         for i in range(0, len(NoBanWord)):
    #             print("фалсе")
    #             if ban == True:
    #                 print("тру")
    #                 if NoBanWord[i] == txt2[j]:
    #                     print("а тут чё?")
    #                     if banWord[k] == txt2[j]:
    #                         print("я тут вообще?")
    #                         return True
        # # дальше проверка, есть ли там слово антиБанВорда
        # # for j in range(0, len(txt2)):
        # for i in range(0, len(NoBanWord)):
        #         # если в тексте есть антиБанВорд
        #     if NoBanWord[i] in txt:
        #             # отменить бан
        #         ban = False
        #             # верно ли?
        #         # следующая логика заключающая в том, что мы делаем из текста в текст массив с каждым словом
        #         # если каждое слово имеет хоть 1 банворд = бан
        #         # if BanWord[i] == txt2[j]:


            # если в каждом банворде есть 
    
    if ban == True:
        # toChat()
        toMe()
        
        

    # второй способ по жёще, он рабочий, но надо каким то боком придумать защиту, чтоб не банил за теб, поход и тд, это немного сложнее чем кажется\
    # можно попробовать через спли пробовать обнаружить банворд, и анбан ворд, таким методом мы сможем понять, а стоит ли банить
    # в общем это пока всё сложно, и требует умственной работы




if __name__ == '__main__':
    bot.infinity_polling()













































































# for i in range(0, len(NoBanWord)):
    #     if NoBanWord[i] in txt:
    #         print("интересно2")
    #         ban = False
    #         for i in range(0, len(banWord)):
    #             if banWord[i] in txt:
    #                 # if 
    #                 print("интересно5")
    #                 ban = True
    #             else:
    #                 print("интересно6")
    #                 ban = False
    #     else:
    #         print("интересно3")
    #         ban = True
    # counter = 0

    

    # txt2 = []
    # txt2 = txt
    # ban = False

    # txt2 = txt.split()
    # for l in range(0, len(banWord)):
    #     for k in range(0, len(NoBanWord)):
    #         for j in range(0, len(txt2)):
    #             for i in range(0, len(txt2)):
    #                 if txt2[j] == NoBanWord[k]:
    #                     if txt2[i] == banWord[l]:
    #                 #         bot.send_message(1111655025, str(message.from_user.id) +" @koneika336" + " " + "@" +str(message.from_user.username)  
    #                 # + " " +str(message.from_user.first_name) + " " +str(message.from_user.last_name) + " " +txt)
    #                         ban = True
    #                         print("интересно")
    # for j in range(0, len(NoBanWord)):
    #     for i in range(0, len(banWord)):

    #         if banWord[i] in txt:
    #             if NoBanWord[j] in txt:
    #                 # Ваш код или функция, которую вы хотите выполнить
    #                 None
    #                 # bot.send_message(1111655025, str(message.from_user.id) +" @koneika336" + " " + "@" +str(message.from_user.username)  
    #                 #     + " " +str(message.from_user.first_name) + " " +str(message.from_user.last_name) + " " +txt)
    #                 ban = True
    #                 print("интересно1")
    #             else:
    #                 # bot.send_message(1111655025, str(message.from_user.id) +" @koneika336" + " " + "@" +str(message.from_user.username)  
    #                 #     + " " +str(message.from_user.first_name) + " " +str(message.from_user.last_name) + " " +txt)
    #                 ban = True
    #                 print("интересно2")
    #         # print("а где я собственно должен быть?")




    # if ban == True:
    #     bot.send_message(1111655025, str(message.from_user.id) +" @koneika336" + " " + "@" +str(message.from_user.username) 
    #     + " " +str(message.from_user.first_name) + " " +str(message.from_user.last_name) + " " +txt)







































































            # for j in range(0, len(NoBanWord)):
                # if NoBanWord[j] == banWord[i]:
            # if NoBanWord[i] == txt:

    # space = " "
    # for i in txt2:
    #     for space in txt2:
    #         counter +=1
    # print(counter + 1)
    
    # for i in range(0, len(txt2)):
    #     if txt2[i] == ' ' or txt2[i] == '\n':
    #         counter +=1

    # print(counter+1)
    # for i in range(0, len(NoBanWord)):
    #     if NoBanWord[i] in txt:
    #         print("have")

    # # ну допустим тут нужно будет прочитать 3 буквы тока

    # banWordList = ["хуй"] * 
    # banWord = banWordList
    # txtArr = [""]
    # # из переменной в массив из букв
    # for i in range(0, len(txt)-1):
        
    #     txtArr[0] = txt
    
    # # тут мы сделали его массивом
    # # print(txtArr[0])

    # # ну почему фон 0,3 = 3 раза а не 4?
    # for i in range(0, 3):
    #     print(txtArr[0][i])
    #     if txtArr[0][i] == banWordList[0][i] and txtArr[0][i+1] == banWordList[0][i+1] and txtArr[0][i+2] == banWordList[0][i+2]:
    #         print("бан")
    #             # print()banWordList[0][i]






























    # какой то текст = 10
    # хуй равен = 3
    # индекс массива начинается от 0
    # print(0," ", len(banWord)-1)
    # for k in range(0, 1):
    #     # print("k= "+str(k))
    #     for i in range(0, len(banWord[k])-1):
    #         # print("i= "+str(i))
    #         for j in range(0, len(txt[k])-1):
    #             # print("j= "+str(j))
    #             if txt[i+j] == banWord[k][i+j]:

    #                 print(txt[i+j], "==" ,banWord[k][i+j])
    #                 print("k= "+str(k)+"i= "+str(i)+"j= "+str(j))
    

    
    # это для заглавной буквы
    # for i in range(len(txt)-len(banWord)-1)
    #     for j in range(0, len(banWord)-1)
    #         if txt[i+j] == banWord[i+j]:
    
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # bot.send_message(-1002088831304, a)
    # bot.send_message(-1002088831304, message.from_user.id)
    

    # N = 100

    # arr = [' '] * N
    # check = "хух"
    # len(check)
    # for i in range(0, N):
    #     # arr[i] = a[i]
    #     print(arr[i])
    #     if a[i-2] == 'х' and a[i-1] == 'у' and a[i-0] == 'й':
    #         print(message.from_user.id," ",a)















































# print(check[0], " ", check[1])
        # elif len(check[i]) == 6:
        #     for j in range (0, count-1):
        #         for i in range(0, len(check[i])-1):

        #             if a[i] == check[j][i] or a[i] == checkUp[j][i]:
        #                 if a[i+1] == check[j][i] or a[i+1] == checkUp[j][i]:
        #                     if a[i+2] == check[j][i] or a[i+2] == checkUp[j][i]:
        #                         if a[i+3] == check[j][i] or a[i+3] == checkUp[j][i]:
        #                             if a[i+4] == check[j][i] or a[i+4] == checkUp[j][i]:
        #                                 if a[i+5] == check[j][i] or a[i+5] == checkUp[j][i]:
        #                                     print("бан2")


                # print(a[i], " == ",check[1][i]," or ",a[i]," == ",checkUp[1][i])
    # print(check[0][0])
    # print(check[0][1])
    # print(check[0][2])
    # print(checkUp[0][0])
    # print(checkUp[0][1])
    # print(checkUp[0][2])
    # print(check[0])
                    # print("0", len(check[0])-1)

                    # print(a[i], " == ",check[0][0]," or ",a[i]," == ",checkUp[0][0])
                    # print(a[i+1], " == ",check[0][1]," or ",a[i+1]," == ",checkUp[0][1])
                    # print(a[i+2], " == ",check[0][2]," or ",a[i]," == ",checkUp[0][2])
                    # print("бан")
    #                 bot.send_message(1111655025, str(message.from_user.id) + " " + "@" +str(message.from_user.username)  
    # + " " +str(message.from_user.first_name) + " " +str(message.from_user.last_name) + " " + a)
    # for i in range(len(a)-len(check[1])-1):        
    #     if a[i] == 'п' or a[i] == 'П':
    #         if a[i+1] == 'и' or a[i+1] == 'И':
    #             if a[i+2] == 'з' or a[i+2] == 'З':
    #                 if a[i+3] == 'д' or a[i+3] == 'Д':
    #                     if a[i+4] == 'е' or a[i+4] == 'Е':
    #                         if a[i+5] == 'ц' or a[i+5] == 'Ц':
    #                 bot.send_message(1111655025, str(message.from_user.id) + " " + "@" +str(message.from_user.username)  
    # + " " +str(message.from_user.first_name) + " " +str(message.from_user.last_name) + " " + a)

                    

# # count = 2
    # checkUp = check.upper()
    # # for i in range(0, count-1):
    # #     checkUp[i] = check[i].upper()

    
    # # for i in range(0,count):
    # print(check)
    # if len(check) == 3:
    #     for i in range(0, len(check)-1):
    #         if a[i] == check[0] or a[i] == checkUp[0]:
    #             if a[i+1] == check[1] or a[i+1] == checkUp[1]:
    #                 if a[i+2] == check[2] or a[i+2] == checkUp[2]:
    #                     bot.send_message(1111655025, str(message.from_user.id) + " " + "@" +str(message.from_user.username)  
    #                     + " " +str(message.from_user.first_name) + " " +str(message.from_user.last_name) + " " + a)



















# print(len(a))
    # bot.reply_to(message, message.text)
    # bot.send_message(-1002088831304)
    # bot.send_photo(-1002088831304, message.photo)
    # bot.send_audio(-1002088831304, message.audio)
    # bot.send_voice(-1002088831304, message.voice)
    # bot.send_video(-1002088831304, message.video)
    # bot.send_document(-1002088831304, message.document)
    # bot.send_location(-1002088831304, message.location)
    # bot.send_contact(-1002088831304, message.contact)
    # bot.send_sticker(-1002088831304, message.sticker)

    
    # message.audio, message.photo, message.voice, message.video, message.document,
    #                                 message.text, message.location, message.contact, message.sticker

            # if a == "е":
        # print(a[i]+a[i+1]+a[i+2])
        # if a[i] == 'х' or a[i] == 'Х' and a[i+1] == 'у' or a[i+1] == 'У' and a[i+2] == 'й' or a[i+2] == 'Й':
        #     print("бан")











                            # bot.send_message(chatLogID, "[test]" +str(message.from_user.id) +"" + " " + "@" +str(message.from_user.username)  
                    # + " " +str(message.from_user.first_name) + " " +str(message.from_user.last_name) + " " +txt)
                    # bot.send_message(1111655025, "[test]" +str(message.from_user.id) +" @koneika336" + " " + "@" +str(message.from_user.username)  
                    # + " " +str(message.from_user.first_name) + " " +str(message.from_user.last_name) + " " +txt)











                        # первый способ
    
    # for k in range(0, len(NoBanWord)):
    #     for j in range(0, len(txt2)):
    #         if NoBanWord[k] == txt2[j]:
    #             # print("nobanword, detected")
    #             for l in range(0, len(banWord)):
    #                 for i in range(0, len(txt2)):
    #                     if banWord[l] == txt2[i]:
    #                         ban = True
    #                         # print("бан")

    #         else:
    #             # print("бан")
    #             ban = True













        # возможно добавить банворд, который тоже самое что и этот



    # for i in range(0, len(banWord)):
    #     if banWord[i] in txt:
    #         print("интересно")
    #         ban = True
    #         for i in range(0, len(banWord)):
    #             if banWord[i] in txt:
    #                 print("интересно")
    #                 ban = True
    #     else:
    #         print("интересно10")

    # for i in range(0, len(NoBanWord)):
    #     if NoBanWord[i] in txt:
    #         # если в слове есть тебя, перепроверка уже всех слов, те
    #         for l in range(0, len(banWord)):
    #             for k in range(0, len(NoBanWord)):
    #                 for j in range(0, len(txt)):
    #                     for i in range(0, len(txt)):
    #                         if txt[j] == NoBanWord[k]:
    #                             if txt[i] == banWord[l]:
    #                                 print("интересно1")
    #                                 ban = False
    #     else:
    #         print("интересно2")
    #         count += 1
    #         if count == 3:
    #             ban = True
    #         else:
    #             ban = False
    
            
    # if ban == True:
    #     bot.send_message(1111655025, str(message.from_user.id) +" @koneika336" + " " + "@" +str(message.from_user.username)  
    #         + " " +str(message.from_user.first_name) + " " +str(message.from_user.last_name) + " " +txt)











    
    # bot.send_message(chatLogID, str(userID) + " " + "@" +str(username) + " " +str(name) + " " +str(name2) + " " + txt)
    
    # print(str(txt))








        # Пример использования для строки
    # строка = "Всем привет с вами я"
    # N = 2






    

    # txt2 = txt.split()

    # for i in range(0, len(txt2)):
    #     print(txt2[i])





    # print(txt)
    # print(txt)
    # for j in range(0, len(txt2)+1):





                        # print(banWord[i])
                # print(txt2[i])
                # print("god")

                            # for i in range(0, len(banWord)):

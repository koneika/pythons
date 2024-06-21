from telethon import TelegramClient, events
import time

api_id = '25159718'
api_hash = '6f0e03276943eed01181365e246258d6'
channels = [
    'amaboyama',
    'halyvachek', 
    'topchekroc',
    'Pa4kaTon',
    'airdropstgnews',
    'xrocket12'
]

whitelist = [
    'https://t.me/xrocket?start=',
    'pass',
    'Пароль',
    'пароль',
    'Pass',
    'Мульти-чек'
]

blacklist = [
    'https://t.me/xrocket?start=sb_vNMn2321hEya67N',
    'https://t.me/xrocket?start=sb_VlNY26QvQ4qKOHx',
]

# # Открываем файл
# with open('save_data.txt', 'r') as file:
#     # Прочитываем строки из файла
#     lines = file.readlines()

if_it_was = [
    ""
] * 2000

# for line in lines:
#     # Добавляем каждую строку в массив
#     if_it_was.append(line.strip())

# for i in range(2000):
#     if_it_was[i] = f"Data {i+1}"

word_to_find = "https://t.me/xrocket?start="
how_much_words_in_whitelist = len(whitelist)
was_message = None
j = 0
dublicat = False

# # Открываем файл для записи
# with open('save_data.txt', 'r') as file:
#     # Записываем элементы массива в файл
#     for line in file:
#         if_it_was[j] = file.read()
#         j += 1

# # Открываем файл для записи
# with open("save_data.txt", 'w') as file:
#     # Записываем элементы массива в файл
#     for item in if_it_was:
#         file.write(str(item) + '\n')

# try:
    # Открываем файл для чтения
    # with open('save_data.txt', 'r') as file:
    #     # Читаем файл построчно и добавляем каждую строку в массив
    #     for line in file:
    #         # Преобразуем строку в число и добавляем в массив (убираем символ новой строки)
    #         if_it_was.append(str(line.strip()))

    # Выводим массив для проверки
    

async def new_message_listener(event):
    time.sleep(1) # protect listener from ban

    global was_message
    global j
    global dublicat
    dublicat = False # сбрасывает дублика с каждым сюда заходом

    message = event.message.text
    index = message.find(word_to_find)
    # print(event.message.text)
    for i in range(0, len(whitelist)):
        if whitelist[i] in message:
        
            for i in range(0, j):
                if if_it_was[i] == message[index : index+len(word_to_find)+19]:
                    dublicat = True # если дубликат обнаружен - тру
            #         print(j, if_it_was[i], "=", message[index : index+len(word_to_find)+19])

            
            # print(if_it_was)
            
            

            if j >= 2000:
                j = 0
            if_it_was[j] = message[index : index+len(word_to_find)+19]
            j += 1

            
            


            if message != was_message:
                
                if dublicat == False:

                    while index != -1:
                        if not 'https://t.me/xrocket?start=sb' in message[index : index+len(word_to_find)+19]:
                                # if_it_was[j] = message[index : index+len(word_to_find)+19]
                                # j += 1
                                # for i in range(0,100):
                                #     if if_it_was[j] in message[index : index+len(word_to_find)+19]:
                                #         print("тоже самое ", j)
                                
                            
                            await client.send_message(-1002087172853, message[index : index+len(word_to_find)+19])
                            index = message.find(word_to_find, index + len(word_to_find))
                            was_message = message
                        # elif not 'https://t.me/xrocket?start=cb' in message[index : index+len(word_to_find)+19]:
                        #         # if_it_was[j] = message[index : index+len(word_to_find)+19]
                        #         # j += 1
                        #         # for i in range(0,100):
                        #         #     if if_it_was[j] in message[index : index+len(word_to_find)+19]:
                        #         #         print("тоже самое ", j)
                                
                            
                        #     await client.send_message(-1002087172853, message[index : index+len(word_to_find)+19])
                        #     index = message.find(word_to_find, index + len(word_to_find))
                        #     was_message = message
                        else:
                            index = message.find(word_to_find, index + len(word_to_find))
                        # Открываем файл для записи
                        # with open("save_data.txt", 'w') as file:
                        #     # Записываем элементы массива в файл
                        #     for item in if_it_was:
                        #         file.write(str(item) + '\n')
        


client = TelegramClient('anon', api_id, api_hash)

for channel_name in channels:
    client.add_event_handler(new_message_listener, events.NewMessage(chats=channel_name))

with client:
    client.run_until_disconnected()

# except Exception as e:
#     print("Произошла ошибка при чтении файла:", e)

# finally:
#     # Открываем файл для записи
#     with open("save_data.txt", 'w') as file:
#         # Записываем элементы массива в файл
#         for item in if_it_was:
#             file.write(str(item) + '\n')





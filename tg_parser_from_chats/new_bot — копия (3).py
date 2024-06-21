from telethon import TelegramClient, events

api_id = '25159718'
api_hash = '6f0e03276943eed01181365e246258d6'
channels = [
    'amaboyama',
    'halyvachek', 
    'topchekroc'
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

if_it_was = [
    ""
] * 100

word_to_find = "https://t.me/xrocket?start="
how_much_words_in_whitelist = len(whitelist)
was_message = None
j = 0

async def new_message_listener(event):
    global was_message

    message = event.message.text
    index = message.find(word_to_find)
    # print(event.message.text)
    for i in range(0, how_much_words_in_whitelist):
        if whitelist[i] in message:
            if message != was_message:
                # print(message[index : index+len(word_to_find)+19])
                # if message[index : index+len(word_to_find)+19] != 'https://t.me/xrocket?start=sb_vNMn2321hEya67N':
                while index != -1:
                    if not 'https://t.me/xrocket?start=sb' in message[index : index+len(word_to_find)+19]:
                            # if_it_was[j] = message[index : index+len(word_to_find)+19]
                            # j += 1
                            # for i in range(0,100):
                            #     if if_it_was[j] in message[index : index+len(word_to_find)+19]:
                            #         print("тоже самое ", j)
                            
                        print('https://t.me/xrocket?start=sb_vNMn2321hEya67N', message[index : index+len(word_to_find)+19])
                        await client.send_message(-1002087172853, message[index : index+len(word_to_find)+19])
                        index = message.find(word_to_find, index + len(word_to_find))
                        was_message = message
                    else:
                        index = message.find(word_to_find, index + len(word_to_find))

client = TelegramClient('anon', api_id, api_hash)

for channel_name in channels:
    client.add_event_handler(new_message_listener, events.NewMessage(chats=channel_name))

with client:
    client.run_until_disconnected()
from telethon import TelegramClient, events

api_id = '25159718'
api_hash = '6f0e03276943eed01181365e246258d6'
channels = [
    'amaboyama',
    'halyvachek', 
    'topchekroc'
]  # Список идентификаторов или имен каналов #'topchekroc', #'tonchekov' # отписка бан 
# 'airdropstgnews',#    'CruptoVlast', # теневой канал     'vini_pyx_69',
# умерли     'xrocket_crazy', 'tonchekov'

whitelist = [
    'https://t.me/xrocket?start=',
    'pass',
    'Пароль',
    'пароль',
    'Pass',
    'Мульти-чек'
]
how_much_words_in_whitelist = 6
was_message = None
word_to_find = "https://t.me/xrocket?start="
index = None

async def new_message_listener(event):

    global was_message
    global word_to_find
    global index
    
    message = event.message.text
    index = message(word_to_find)

    for i in range(0, how_much_words_in_whitelist):

        if whitelist[i] in message:

            if not str(message) == str(was_message):
                if index != -1:
                    print(message[index : index+len(word_to_find)+19])
                    await client.send_message(-1002087172853, message[index : index+len(word_to_find)+19])
                    await client.send_message('me', message[index : index+len(word_to_find)+19])

                was_message = message

client = TelegramClient('anon', api_id, api_hash)

# Регистрируем обработчик событий для каждого канала
for channel_name in channels:
    client.add_event_handler(new_message_listener, events.NewMessage(chats=channel_name))

with client:
    client.run_until_disconnected()


# # Список идентификаторов групп и каналов
# group_ids = ['amaboyama']

# async def main():
#     async with TelegramClient('anon', api_id, api_hash) as client:
#         for group_id in group_ids:
#             async for message in client.iter_messages(group_id):
#                 print(f"Группа {group_id}: {message.text}")

# if __name__ == '__main__':
#     import asyncio
#     asyncio.run(main())
# import asyncio
# from telethon.sync import TelegramClient, events

# api_id = 25159718
# api_hash = '6f0e03276943eed01181365e246258d6'

# client = TelegramClient('anon', api_id, api_hash)
# client.start()

# async def main():
#     # Getting information about yourself
#     me = await client.get_me()

#     # "me" is a user object. You can pretty-print
#     # any Telegram object with the "stringify" method:
#     print(me.stringify())

#     # When you print something, you see a representation of it.
#     # You can access all attributes of Telegram objects with
#     # the dot operator. For example, to get the username:
#     username = me.username
#     print(username)
#     print(me.phone)

#     # You can print all the dialogs/conversations that you are part of:
#     async for dialog in client.iter_dialogs():
#         print(dialog.name, 'has ID', dialog.id)

#     # # You can send messages to yourself...
#     # await client.send_message('me', 'Hello, myself!')
#     # # ...to some chat ID
#     # await client.send_message(-100123456, 'Hello, group!')
#     # # ...to your contacts
#     # await client.send_message('+34600123123', 'Hello, friend!')
#     # # ...or even to any username
#     # await client.send_message('username', 'Testing Telethon!')

#     # You can, of course, use markdown in your messages:
#     message = await client.send_message(
#         'me',
#         'This message has **bold**, `code`, __italics__ and '
#         'a [nice website](https://example.com)!',
#         link_preview=False
#     )

#     # Sending a message returns the sent message object, which you can use
#     print(message.raw_text)

#     # # You can reply to messages directly if you have a message object
#     # await message.reply('Cool!')

#     # # Or send files, songs, documents, albums...
#     # await client.send_file('me', '/home/me/Pictures/holidays.jpg')

#     # You can print the message history of any chat:
#     async for message in client.iter_messages('me'):
#         print(message.id, message.text)

#         # You can download media from messages, too!
#         # The method will return the path where the file was saved.
#         if message.photo:
#             path = await message.download_media()
#             print('File saved to', path)  # printed after download is done



# with client:
#     client.loop.run_until_complete(main())
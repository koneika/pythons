# from telethon import TelegramClient

# api_id = 25159718  # Ваш идентификатор API
# api_hash = '6f0e03276943eed01181365e246258d6'  # Ваш хеш API

# with TelegramClient('anon', api_id, api_hash) as client:
#     client.loop.run_until_complete(client.send_message('me', 'xdxdxdxdxdxdxdxdxd'))



from telethon.sync import TelegramClient
import time

# from telethon import TelegramClient

# Remember to use your own values from my.telegram.org!
api_id = 25159718
api_hash = '6f0e03276943eed01181365e246258d6'
client = TelegramClient('anon', api_id, api_hash)



# with TelegramClient('anon', api_id, api_hash) as client:
#     channel_username = 'amaboyama'
#     channel = client.get_entity(channel_username)
#     while True:
#         time.sleep(5)
#         for message in client.iter_messages(channel):
#             print(f"Message from {message.sender.username}: {message.text}")

# async def main():
    # Most of your code should go here.
    # You can of course make and use your own async def (do_something).
    # They only need to be async if they need to await things.
    # me = await client.get_me()
    # await do_something(me)
    # phone = '+359 888 582 828'
    # sent = await client.send_code_request(phone)
    # print(sent)
    

# async def handler(event):
#     # Good
#     chat = await event.get_chat()
#     sender = await event.get_sender()
#     chat_id = event.chat_id
#     sender_id = event.sender_id

async def get_channel_messages(channel_username, limit=10):
    async for message in client.iter_messages(channel_username, limit=limit):
        print(message.text)

with client:
    client.loop.run_until_complete(get_channel_messages("ama"))

print("end")
input()


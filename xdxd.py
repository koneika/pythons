import asyncio 
import aiohttp 
import telebot 
import logging 
from telebot import types 
print("hello1")
logging.basicConfig(level=logging.INFO) 

logging.info("Это сообщение будет залогировано с уровнем INFO")

print("hello2")

bot = telebot.TeleBot("7048609406:AAEhqRof2NAUVaiKgBH3xANwBjONKl2u3cg") 
print("hello3")
@bot.inline_handler(lambda query: True)
def query_text(inline_query):
    print("hello4") 
    try: 
        network = 'ton'   
        coin_names = ['CES', 'GOI2', 'KAKAXA',]   
        token_addresses = ['EQCl0S4xvoeGeFGijTzicSA8j6GiiugmJW5zxQbZTUntre-1',  
                           'EQBCoynGYslAMjv_gRl_2_B1KMOvh9ZW-ae0p7SaXZy6KFjY',  
                           'EQDqz7LTwgj016kiTiSooM_ft8kveL2P4pj4fkJmsUV_an_X']   
        token_data = asyncio.run(fetch_multiple_token_prices(network, token_addresses)) 
         
        results = [] 
        for i, coin_name in enumerate(coin_names): 
            token_price = token_data[i].get('data', {}).get('attributes', {}).get('token_prices', {}).get(token_addresses[i], "N/A") 
            token_price = float(token_price)
            print(token_price)
            message = f"Цена токена",coin_name,": ",float(token_price),"USD" 
            results.append(types.InlineQueryResultArticle( 
                id=str(i),
                title=coin_name, 
                input_message_content=types.InputTextMessageContent(message), 
                description="Кто прочитал,тот гей" 
                 
            )) 
        print("hello5") 
        bot.answer_inline_query(inline_query.id, results) 
    except Exception as e: 
        print(e) 
 
async def fetch_token_price(network, token_address): 
    url = f"https://api.geckoterminal.com/api/v2/simple/networks/{network}/token_price/{token_address}" 
    async with aiohttp.ClientSession() as session: 
        async with session.get(url) as response: 
            if response.status == 200:
                print("ok")
                data = await response.json() 
                return data 
            else: 
                return None 
 
async def fetch_multiple_token_prices(network, token_addresses): 
    tasks = [fetch_token_price(network, address) for address in token_addresses] 
    return await asyncio.gather(*tasks) 
 
 
 
bot.polling()

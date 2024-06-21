# -*- coding: utf-8 -*-
import telebot
from telebot import types
import time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup



api = '7048609406:AAEhqRof2NAUVaiKgBH3xANwBjONKl2u3cg'

bot = telebot.TeleBot(api)

myUsername = 1111655025


bot.send_message(myUsername, "bot started")
with open('C:/Users/slava/Desktop/photo_2024-04-16_17-17-00.jpg', 'rb') as photo:
    bot.send_photo(myUsername, photo)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(myUsername, "bot started")


# Create an inline keyboard with two buttons
button1 = InlineKeyboardButton("Button 1", callback_data="button1")
button2 = InlineKeyboardButton("Button 2", url="https://example.com")

# Create a row with the buttons
row = [button1, button2]

# Create the inline keyboard markup
keyboard = InlineKeyboardMarkup([row])

# Now you can attach this keyboard to a message or an inline query result
# (e.g., when sending a message or responding to an inline query)

# @bot.message_handler(commands=['report', 'admin'])
# def report(message):
#     global newTime
#     if int(newTime) < int(time.time()):    
#         bot.send_message(myUsername, "[test]" +str(message.from_user.id) + " " + "@" +str(message.from_user.username)  
#         + " " +str(message.from_user.first_name) + " " +str(message.from_user.last_name) + " " +message.text)
#         newTime += 60

# bot.polling()

if __name__ == '__main__':
    bot.infinity_polling()
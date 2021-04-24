import telebot
import sqlite3
from telebot import types
from auth_token import token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Привет!")
    stick = open("Static/Pics/hi.webp", 'rb')
    bot.send_sticker(message.chat.id, stick)
    markup_path = types.ReplyKeyboardMarkup(resize_keyboard=True)
    url_button1 = types.InlineKeyboardButton(text="8924319512809491248128-4-08")
    url_button2 = types.InlineKeyboardButton(text="2")
    markup_path.row(url_button1)
    markup_path.row(url_button2)
    bot.send_message(message.chat.id, "Я бот-эксурсовод!", reply_markup=markup_path)
    # клавиатура у ввода


@bot.message_handler(func=lambda m: True)
def answer_all(message):
    pass


bot.polling()




# url_button1 = types.InlineKeyboardButton(text="Официальный сайт ФТ Сириус", url="https://sirius-ft.ru")
# url_button2 = types.InlineKeyboardButton(text="Сайт ОЦ 'Сириус'", url="https://sochisirius.ru")

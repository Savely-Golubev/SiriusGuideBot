import telebot
import sqlite3
from telebot import types
from auth_token import token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start_message(message):
    
    welcome_photo = open('Static/Pics/sirius_main.png', 'rb')
    bot.send_photo(message.chat.id, welcome_photo)
    bot.send_message(message.chat.id, "Привет, {0.first_name} 👋. Я бот-эксурсовод. Я могу провести небольшой экскурс по Федеральной Территории 'Сириус' вкратце рассказав об устройстве нашего наукограда🔬.".format(message.from_user, bot.get_me()), parse_mode='html')
    markup_path = types.ReplyKeyboardMarkup(resize_keyboard=True)
    url_button1 = types.InlineKeyboardButton(text="География и инфраструктура")
    url_button2 = types.InlineKeyboardButton(text="Сведения о федеральной территории")
    url_button3 = types.InlineKeyboardButton(text="Научные достижения")
    markup_path.row(url_button1) #разбиение на вертикальные кнопки
    markup_path.row(url_button2)
    markup_path.row(url_button3)
    bot.send_message(message.chat.id, "Для навигации используй кнопки ниже 👇",reply_markup=markup_path)
    # bot.send_message(message.chat.id, "1", )
    # bot.edit_message_text(message.chat.id, 'хихихи)')
    

@bot.message_handler(content_types=["text"])
def second_level(message):
    if message.text == 'Назад':  # кнопка назад
        markup_path = types.ReplyKeyboardMarkup(resize_keyboard=True)
        url_button1 = types.InlineKeyboardButton(text="География и инфраструктура")
        url_button2 = types.InlineKeyboardButton(text="Сведения об федеральной территории")
        url_button3 = types.InlineKeyboardButton(text="Научная работа")
        markup_path.row(url_button1) #разбиение на вертикальные кнопки
        markup_path.row(url_button2)
        markup_path.row(url_button3)
        bot.send_message(message.chat.id, text="Главное меню", reply_markup=markup_path)
    elif message.text == 'География и инфраструктура':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        second_button1 = types.InlineKeyboardButton(text="Местоположение на карте") #2 уровень, 1 ответ, 1 вариант     в карты переход ссылкой
        second_button2 = types.InlineKeyboardButton(text="Инфраструктура") #2 уровень, 1 ответ, 2 вариант             каждый объект отдельно
        backbutton = types.InlineKeyboardButton(text="Назад")
        keyboard.row(second_button1) 
        keyboard.row(second_button2)
        keyboard.row(backbutton)
        bot.send_message(message.chat.id, text="2 уровень 1 кнопка",reply_markup=keyboard)
        # bot.send_message(call.chat.id, 'ураа 2 ветка', reply_markup=keyboard)
    elif message.text == 'Сведения о федеральной территории':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        second_button1 = types.InlineKeyboardButton(text="История и миссия") #2 уровень, 2 ответ, 1 вариант
        second_button2 = types.InlineKeyboardButton(text="Руководство") #2 уровень, 2 ответ, 2 вариант
        backbutton = types.InlineKeyboardButton(text="Назад")
        keyboard.row(second_button1) 
        keyboard.row(second_button2)
        keyboard.row(backbutton)
        bot.send_message(message.chat.id, text="2 уровень 2 кнопка",reply_markup=keyboard)
        # bot.send_message(call.chat.id, 'ураа 2 ветка', reply_markup=keyboard)
    elif message.text == 'Научная работа':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        second_button1 = types.InlineKeyboardButton(text="Образовательные программы") #2 уровень, 2 ответ, 1 вариант
        second_button2 = types.InlineKeyboardButton(text="Достижения") #2 уровень, 2 ответ, 2 вариант
        backbutton = types.InlineKeyboardButton(text="Назад")
        keyboard.row(second_button1) #разбиение на вертикальные кнопки
        keyboard.row(second_button2)
        keyboard.row(backbutton)
        # keyboard.add(second_button1, second_button2, second_button3) callback_data = '2_3_3'
        bot.send_message(message.chat.id, text="2 уровень 3 кнопка",reply_markup=keyboard)
        # send_message   edit_message_text
    else:
        bot.send_message(message.chat.id, "Для навигации используй кнопки ниже 👇")
bot.polling()

bot.message_handler(content_types=["text"])
def third_level(message):
    if message.text == 'Назад':  # кнопка назад
        markup_path = types.ReplyKeyboardMarkup(resize_keyboard=True)
        url_button1 = types.InlineKeyboardButton(text="География и инфраструктура")
        url_button2 = types.InlineKeyboardButton(text="Сведения об федеральной территории")
        url_button3 = types.InlineKeyboardButton(text="Научная работа")
        markup_path.row(url_button1) #разбиение на вертикальные кнопки
        markup_path.row(url_button2)
        markup_path.row(url_button3)
        bot.send_message(message.chat.id, text="Главное меню", reply_markup=markup_path)
    elif message.text == 'Местоположение на карте':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        backbutton = types.InlineKeyboardButton(text="Назад")
        keyboard.row(backbutton)
        bot.send_message(message.chat.id, text="2 уровень 1 кнопка",reply_markup=keyboard)
        # bot.send_message(call.chat.id, 'ураа 2 ветка', reply_markup=keyboard)

    # bot.send_message(message.chat.id, "Привет, {0.first_name}!")


# url_button1 = types.InlineKeyboardButton(text="Официальный сайт ФТ Сириус", url="https://sirius-ft.ru")
# url_button2 = types.InlineKeyboardButton(text="Сайт ОЦ 'Сириус'", url="https://sochisirius.ru")
# Я бот-эксурсовод. Я могу провести небольшой экскурс по ФТ 'Сириус' вкратце рассказав об устройстве нашего наукограда


# sdi = sdi[0].split(";")
#         for i in sdi:
#             i = i.split(":")
#             msg, photo = i[0], open(i[1], 'rb')
#             bot.send_message(msgid, msg)
#             print(photo)
#             bot.send_photo(msgid, photo)

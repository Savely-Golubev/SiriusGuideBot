import telebot
from telebot import types
from auth_token import token
from telebot.types import InputMediaPhoto, InputMediaDocument

bot = telebot.TeleBot(token)

# читаем текста сразу же
text_iceberg = []
with open('Static/Text/Iceberg.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        text_iceberg.append(line.rstrip('\n'))

text_sirius_main = []
with open('Static/Text/Sirius_OC_main.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        text_sirius_main.append(line.rstrip('\n'))

text_sirius_add = []
with open('Static/Text/Sirius_OC_additional.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        text_sirius_add.append(line.rstrip('\n'))

sirius_university = []
with open('Static/Text/Sirius_University.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        sirius_university.append(line.rstrip('\n'))

history_text = []
with open('Static/Text/FT_Sirius.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        history_text.append(line.rstrip('\n'))

head_ft = []
with open('Static/Text/HeadOfFT.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        head_ft.append(line.rstrip('\n'))

achiev = []
with open('Static/Text/Achi.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        achiev.append(line.strip())


@bot.message_handler(commands=["start"])
def start_message(message):
    welcome_text = "Привет, {0.first_name} 👋. Я бот-эксурсовод. Я могу провести небольшую виртуальную экскурсию по Федеральной Территории 'Сириус' и расскажу об устройстве нашего наукограда🔬."
    welcome_photo = open('Static/Pics/sirius_main.png', 'rb')
    bot.send_photo(message.chat.id, welcome_photo, caption=welcome_text.format(
        message.from_user, bot.get_me()), parse_mode='html')
    markup_path = types.ReplyKeyboardMarkup(resize_keyboard=True)
    url_button1 = types.InlineKeyboardButton(text="География и инфраструктура")
    url_button2 = types.InlineKeyboardButton(
        text="Сведения о федеральной территории")
    url_button3 = types.InlineKeyboardButton(text="Научные достижения")
    markup_path.row(url_button1)  # разбиение на вертикальные кнопки
    markup_path.row(url_button2)
    markup_path.row(url_button3)
    bot.send_message(
        message.chat.id, "Для навигации используй кнопки ниже 👇", reply_markup=markup_path)
    # bot.send_message(message.chat.id, "1", )
    # bot.edit_message_text(message.chat.id, 'хихихи)')


@bot.message_handler(content_types=["text"])
def second_level(message):
    if message.text == 'Главное меню':  # кнопка назад
        markup_path = types.ReplyKeyboardMarkup(resize_keyboard=True)
        url_button1 = types.InlineKeyboardButton(
            text="География и инфраструктура", callback_data='start')
        url_button2 = types.InlineKeyboardButton(
            text="Сведения о федеральной территории", callback_data='start')
        url_button3 = types.InlineKeyboardButton(
            text="Научная работа", callback_data='start')
        markup_path.row(url_button1)  # разбиение на вертикальные кнопки
        markup_path.row(url_button2)
        markup_path.row(url_button3)
        bot.send_message(message.chat.id, text="Главное меню",
                         reply_markup=markup_path)
    elif message.text == 'География и инфраструктура':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # 2 уровень, 1 ответ, 1 вариант     в карты переход ссылкой
        second_button1 = types.InlineKeyboardButton(
            text="Местоположение на карте", callback_data='geo+inf')
        # 2 уровень, 1 ответ, 2 вариант             каждый объект отдельно
        second_button2 = types.InlineKeyboardButton(
            text="Инфраструктура", callback_data='geo+inf')
        backbutton = types.InlineKeyboardButton(text="Главное меню")
        keyboard.row(second_button1)
        keyboard.row(second_button2)
        keyboard.row(backbutton)
        bot.send_message(
            message.chat.id, text="О чём ты хочешь узнать? 👇", reply_markup=keyboard)
        # bot.send_message(call.chat.id, 'ураа 2 ветка', reply_markup=keyboard)
    elif message.text == 'Сведения о федеральной территории':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        second_button1 = types.InlineKeyboardButton(
            text="История и миссия")  # 2 уровень, 2 ответ, 1 вариант
        second_button2 = types.InlineKeyboardButton(
            text="Руководство")  # 2 уровень, 2 ответ, 2 вариант
        backbutton = types.InlineKeyboardButton(text="Главное меню")
        keyboard.row(second_button1)
        keyboard.row(second_button2)
        keyboard.row(backbutton)
        bot.send_message(
            message.chat.id, text="Выбери о чём ты хочешь узнать больше 👇", reply_markup=keyboard)
        # bot.send_message(call.chat.id, 'ураа 2 ветка', reply_markup=keyboard)
    elif message.text == 'Научная работа':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        second_button1 = types.InlineKeyboardButton(
            text="Образовательные программы")  # 2 уровень, 2 ответ, 1 вариант
        second_button2 = types.InlineKeyboardButton(
            text="Достижения")  # 2 уровень, 2 ответ, 2 вариант
        backbutton = types.InlineKeyboardButton(text="Главное меню")
        keyboard.row(second_button1)  # разбиение на вертикальные кнопки
        keyboard.row(second_button2)
        keyboard.row(backbutton)
        bot.send_message(
            message.chat.id, text="Выбери о чём ты хочешь узнать больше 👇", reply_markup=keyboard)
        # send_message   edit_message_text




    elif message.text == 'Местоположение на карте':
        sir_photo = open('Static/Pics/sirius.webp', 'rb')
        bot.send_photo(message.chat.id, sir_photo, caption='Территория расположена в Имеретинской низменности в междуречье Мзымты и Псоу, окружена Кавказскими горами и уникальным природным заповедником. Здесь проходила зимняя Олимпиада 2014 года, и на базе основного комплекса олимпийских объектов с 2015 года развивается образовательный центр «Сириус».')
        bot.send_message(message.chat.id, text="Лови геометку:")
        bot.send_location(
            message.chat.id, latitude=43.4015877965321, longitude=39.9646497769483)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        backbutton = types.InlineKeyboardButton(text="Главное меню")
        keyboard.row(backbutton)
        keyboard.row(backbutton)

    elif message.text == 'Инфраструктура':
        infr = open('Static/Pics/infrastruktura-part-marked.png', 'rb')
        bot.send_photo(message.chat.id, infr)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        third_button1 = types.InlineKeyboardButton(text="1 объект")
        third_button2 = types.InlineKeyboardButton(text="2 объект")
        third_button3 = types.InlineKeyboardButton(text="3 объект")
        third_button4 = types.InlineKeyboardButton(text="4 объект")
        backbutton = types.InlineKeyboardButton(text="Главное меню")
        keyboard.add(third_button1, third_button2,
                     third_button3, third_button4)
        keyboard.row(backbutton)
        bot.send_message(
            message.chat.id, text="Выбери номер объекта о котором хочешь узнать больше 👇", reply_markup=keyboard)

    elif message.text == '1 объект':
        text_shayba = []
        with open('Static/Text/Shayba.txt', 'r', encoding='utf-8') as file:
            for line in file.readlines():
                text_shayba.append(line.rstrip('\n'))
        shaiba_inf = open('Static/Pics/shayba_info.png', 'rb')
        shayba = open('Static/Pics/shayba.jpg', 'rb')
        media = [InputMediaPhoto(shaiba_inf, caption = ''.join(text_shayba)), InputMediaPhoto(shayba)]
        bot.send_media_group(message.chat.id, media)
        file.close()
    elif message.text == '2 объект':
        iceberg1 = open('Static/Pics/Iceberg1.jpg', 'rb')
        iceberg2 = open('Static/Pics/Iceberg2.jpg', 'rb')
        media = [InputMediaPhoto(iceberg1, caption = ''.join(text_iceberg)), InputMediaPhoto(iceberg2)]
        bot.send_media_group(message.chat.id, media)
    elif message.text == '3 объект':
        # file = open('Static/Text/Shayba.txt', 'w', encoding='utf-8')
        sirius1 = open('Static/Pics/Sirius1.jpg', 'rb')
        sirius2 = open('Static/Pics/Sirius2.jpg', 'rb')
        media = [InputMediaPhoto(sirius1, caption = ''.join(text_sirius_main)), InputMediaPhoto(sirius2)]
        bot.send_media_group(message.chat.id, media)
        bot.send_message(message.chat.id, text = ''.join(text_sirius_add))
        bot.send_message(message.chat.id, text = 'Официальный сайт: \n https://sochisirius.ru', disable_web_page_preview = True)
    elif message.text == '4 объект':
        # file = open('Static/Text/Shayba.txt', 'w', encoding='utf-8')
        uni1 = open('Static/Pics/Uni1.jpg', 'rb')
        uni2 = open('Static/Pics/Uni2.png', 'rb')
        media = [InputMediaPhoto(uni1, caption = '\n'.join(sirius_university)), InputMediaPhoto(uni2)]
        bot.send_media_group(message.chat.id, media)
        bot.send_message(message.chat.id, text = 'Официальный сайт: \n https://siriusuniversity.ru', disable_web_page_preview = True)



    elif message.text == "История и миссия":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        third_button1 = types.InlineKeyboardButton(text="История")
        third_button2 = types.InlineKeyboardButton(text="Цели и задачи")
        backbutton = types.InlineKeyboardButton(text="Главное меню")
        keyboard.add(third_button1, third_button2)
        keyboard.row(backbutton)
        bot.send_message(
            message.chat.id, text="О чём ты хочешь узнать? 👇", reply_markup=keyboard)
    elif message.text == "История":
        sir1 = open('Static/Pics/FT_Sir.jpg', 'rb')
        sir2 = open('Static/Pics/Sir_Loc.jpg', 'rb')
        media = [InputMediaPhoto(sir1), InputMediaPhoto(sir2)]
        bot.send_media_group(message.chat.id, media)
        bot.send_message(message.chat.id, text = ''.join(history_text))
        bot.send_message(message.chat.id, text = 'Официальный сайт: \n https://sirius-ft.ru', disable_web_page_preview = True)
    elif message.text == "Цели и задачи":
        sir1 = open('Static/Pics/targets.png', 'rb')
        media = [InputMediaPhoto(sir1)]
        bot.send_media_group(message.chat.id, media)
        bot.send_message(message.chat.id, text = 'Официальный сайт: \n https://sirius-ft.ru', disable_web_page_preview = True)

    elif message.text == 'Руководство':
        port1 = open('Static/Pics/AndrOlegovich.jpg', 'rb')
        media = [InputMediaPhoto(port1)]
        bot.send_media_group(message.chat.id, media)
        bot.send_message(message.chat.id, text = ''.join(head_ft))
        bot.send_message(message.chat.id, text = 'Официальный сайт: \n https://sirius-ft.ru', disable_web_page_preview = True)





    elif message.text == 'Образовательные программы':
        bot.send_message(message.chat.id, text = 'Наука: https://sochisirius.ru/obuchenie/nauka \nИскусство: https://sochisirius.ru/obuchenie/iskusctvo \nСпорт: https://sochisirius.ru/obuchenie/sport \nЛитературное творчество: https://sochisirius.ru/obuchenie/literature', disable_web_page_preview = True)
        # bot.send_message(message.chat.id, text = 'Искусство: https://sochisirius.ru/obuchenie/iskusctvo', disable_web_page_preview = True)
        # bot.send_message(message.chat.id, text = 'Спорт: https://sochisirius.ru/obuchenie/sport', disable_web_page_preview = True)
        # bot.send_message(message.chat.id, text = 'Литературное творчество: https://sochisirius.ru/obuchenie/literature', disable_web_page_preview = True)

    elif message.text == 'Достижения':
        bot.send_message(message.chat.id, text = '\n'. join(achiev))







# url_button1 = types.InlineKeyboardButton(text="Официальный сайт ФТ Сириус", url="https://sirius-ft.ru")
# url_button2 = types.InlineKeyboardButton(text="Сайт ОЦ 'Сириус'", url="https://sochisirius.ru")
# Я бот-эксурсовод. Я могу провести небольшой экскурс по ФТ 'Сириус' вкратце рассказав об устройстве нашего наукограда


bot.polling()

# -*- coding: utf-8 -*-
import telebot
from telebot import types

TOKEN = ""

bot = telebot.TeleBot(TOKEN)

MainMenu = types.InlineKeyboardMarkup(row_width=1)
item1 = types.InlineKeyboardButton("GSoft - это 📌", callback_data="gsoft")
item2 = types.InlineKeyboardButton("Как мы работаем? 🙋‍♂️", callback_data="works")
item3 = types.InlineKeyboardButton("Услуги 👨🏻‍💻", callback_data="jobs")
item4 = types.InlineKeyboardButton("Главное меню", callback_data="main")
item5 = types.InlineKeyboardButton("Местоположение 📍", url="https://go.2gis.com/s3tes")
item6 = types.InlineKeyboardButton("Контакты 📇", callback_data="cont")
item8 = types.InlineKeyboardButton("Оставить заявку 📃")
MainMenu.add(item1, item2, item3, item5, item6, item8)


@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(
        message.chat.id,
        "Здравствуйте 👋\nЯ - GSoft бот. Нужна моя помощь? !\nВыберите тему".format(
            message.from_user.id
        ),
        parse_mode="html",
        reply_markup=MainMenu,
    )


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == "gsoft":

                markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item_main = types.KeyboardButton("Главное меню")

                markup_reply.add(item_main)

                bot.send_message(
                    call.message.chat.id,
                    "Сделаем все и немного больше !\n\nНаши специалисты помогут с выбором Программных продуктов 1С и необходимого оборудования под Ваши конкретные задачи",
                    reply_markup=markup_reply,
                )

            if call.data == "works":

                markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item_main = types.KeyboardButton("Главное меню")

                markup_reply.add(item_main)

                bot.send_message(
                    call.message.chat.id,
                    "1️⃣Оставьте заявку на консультацию, и мы перезвоним Вам в течение 2 часов в рабочее время. Услуга предоставляется бесплатно.\n\n2️⃣Мы индивидуально рассматриваем вашу ситуацию и предоставляем качественное решение!\n\n3️⃣Согласовываем формальности и приступаем к внедрению качественного решения!",
                    reply_markup=markup_reply,
                )

            if call.data == "jobs":

                markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item_main = types.KeyboardButton(
                    "Главное меню",
                )

                markup_reply.add(item_main)

                bot.send_message(
                    call.message.chat.id,
                    "Установка программы 1С⚙️\n \nУ нас вы можете приобрести программы от компании 1С\n1С: Бухгалтерия для Казахстана\n1С: Зарплата и Управление персоналом для Казахстана\n1С: Зарплата и Управление персоналом КОРП для Казахстана\n1С: Управление торговым предприятием для Казахстана\n1С: Управление торговлей для Казахстана\n1С: Розница для Казахстана\n\nОбучение📝\n\nГрамотно обучим ваш персонал как правильно использовать программные продукты 1С и поможем с лёгкостью освоить работу с ними.\n\nСопровождение🛠\n\nСтав нашим клиентом вы получите:\n1. Своевременное обновление бухгалтерских программ.\n2. Полноценное сопровождение и консультации в рамках выбранного тарифа.\n3. Специальные цены на курсы обучения персонала.",
                    reply_markup=markup_reply,
                )

            if call.data == "cont":

                markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item_main = types.KeyboardButton("Главное меню")
                markup_reply.add(item_main)

                bot.send_message(
                    call.message.chat.id,
                    "Сотовый номер📱: +7 701 872 16 95\nemail📨: gsoft2018@mail.ru",
                    reply_markup=markup_reply,
                )

    except Exception as e:
        print(repr(e))


@bot.message_handler(content_types=["text"])
def send_text(message):
    if message.text == "Главное меню":
        bot.send_message(message.chat.id, "Меню:", reply_markup=MainMenu)


bot.polling(none_stop=True)

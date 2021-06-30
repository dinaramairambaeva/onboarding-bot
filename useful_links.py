import telebot
import text
from telebot import types
import config

bot = telebot.TeleBot(config.TOKEN)

# list of useful links
def links(message):
    links_markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton('Сайт', url='https://alser.kz/about-us')
    item2 = types.InlineKeyboardButton('Магазин', url='https://alser.kz')
    item3 = types.InlineKeyboardButton('HR портал', url='https://hrportal.alser.kz')

    links_markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, text.link_text, reply_markup = links_markup)
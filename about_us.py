import telebot
import text
from telebot import types
import config

bot = telebot.TeleBot(config.TOKEN)

#information about a company and link to the official website
def info(message):
    info_markup = types.InlineKeyboardMarkup()
    website = types.InlineKeyboardButton('Узнать больше', url='https://alser.kz/about-us')
    info_markup.add(website)

    bot.send_message(message.chat.id, text.about_us_text, reply_markup=info_markup)

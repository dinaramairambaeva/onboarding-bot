import telebot
from telebot import types
import config
import text

bot = telebot.TeleBot(config.TOKEN)

#list of questions
def questions(message):
    dep_markup = telebot.types.InlineKeyboardMarkup()
    item1 = telebot.types.InlineKeyboardButton(text.question1, callback_data='eda')
    dep_markup.add(item1)
    
    bot.send_message(message.chat.id, text.faq_text, reply_markup=dep_markup)

# reply to call (from faq)
def call_handler(call):
    try:
        if call.message:
            if call.data == 'eda':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text.answer1, reply_markup=None)

    except Exception as e:
        print(repr(e))


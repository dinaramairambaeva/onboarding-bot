import telebot 
import config
import departments
import useful_links
import faq
import text
import about_us
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

# start button
markupStart = types.ReplyKeyboardMarkup(resize_keyboard=True)
itemStart=types.KeyboardButton("start")
markupStart.add(itemStart)

# main keyboard
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Депортаменты")
item2 = types.KeyboardButton("Про компанию")
item3 = types.KeyboardButton("FAQ")
item4 = types.KeyboardButton("Полезные ссылки")
markup.add(item1, item2, item3, item4)

# reply to 'start' command
@bot.message_handler(commands=['start'])
def welcome(message):
    stick = open('privet.webp', 'rb')
    bot.send_sticker(message.chat.id, stick)
    bot.send_message(message.chat.id, text.welcoming.format(message.from_user, bot.get_me()), parse_mode="html")
    bot.send_message(message.chat.id, text.startingQuestion, reply_markup=markup)


# reply to text messages
@bot.message_handler(content_types=['text'])
def answerToButton(message):
    if message.text == 'Депортаменты':        
        departments.departments_f(message)
    elif message.text == 'Про компанию':
        about_us.info(message)
    elif message.text == 'FAQ':
        faq.questions(message)
    elif message.text == 'Полезные ссылки':
        useful_links.links(message)
    else:
        bot.send_message(message.chat.id, text.misunderstood, parse_mode="html")

#reply to call (from any inline keyboard)
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data.isdigit():
        departments.deparment_info(call)
    else:
        faq.call_handler(call)


#RUN
bot.polling(none_stop=True)

#run-daily


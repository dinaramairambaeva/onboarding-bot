import telebot
import config
import text
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("LB.CASE - это")
	markup.add(item1)

	bot.send_message(message.chat.id, (text.textstart)
	.format(message.from_user, bot.get_me()),parse_mode = 'html', reply_markup = markup)

@bot.message_handler(content_types = ['text'])
def keyboard(message):
	if message.chat.type == 'private':
		if message.text == 'LB.CASE - это':
			bot.send_message(message.chat.id, (text.lbthis))
		else:
			bot.send_message(message.chat.id, (text.writemess))



bot.polling(none_stop = True)
import telebot
import text

import config

bot = telebot.TeleBot(config.TOKEN)

#list of departments
def departments_f(message):
    dep_markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    item1 = telebot.types.InlineKeyboardButton('Департамент розницы и торговли', callback_data=1)
    item2 = telebot.types.InlineKeyboardButton('Департамент электронной коммерции', callback_data=2)
    item3 = telebot.types.InlineKeyboardButton('Департамент по работе с персоналом', callback_data=3)
    item4 = telebot.types.InlineKeyboardButton('Департамент планиорвания поставок', callback_data=4)
    item5 = telebot.types.InlineKeyboardButton('Департамент цифровых услуг и сервиса', callback_data=5)
    item6 = telebot.types.InlineKeyboardButton('Депортамент Безопасности', callback_data=6)
    item7 = telebot.types.InlineKeyboardButton('Департамент информационной безопасности', callback_data=7)
    item8 = telebot.types.InlineKeyboardButton('Департамент информационных технологий', callback_data=8)
    item9 = telebot.types.InlineKeyboardButton('Департамент логистики', callback_data=9)
    item10 = telebot.types.InlineKeyboardButton('Департамент маркетинга и рекламы', callback_data=10)
    item11 = telebot.types.InlineKeyboardButton('Коммерческий департамент', callback_data=11)
    item12 = telebot.types.InlineKeyboardButton('Отдел по развити Бизнеса', callback_data=12)
    item13 = telebot.types.InlineKeyboardButton('Отдел внутреннего контроля', callback_data=13)
    item14 = telebot.types.InlineKeyboardButton('Финансовый департамент', callback_data=14)
    item15 = telebot.types.InlineKeyboardButton('Депортамент продаж "Бизнес для Бизнеса"', callback_data=15)

    dep_markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15)

    bot.send_message(message.chat.id, "Департаменты", reply_markup=dep_markup)

#reply to call (from inline keyboard of departments)
def deparment_info(call):
    try:
        if call.message:
            if str(call.data) == '1':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text.department_drt, reply_markup=None)

            if str(call.data) == '2':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text.department_dek, reply_markup=None)

            if str(call.data) == '3':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= text.department_drp, reply_markup=None)

            if str(call.data) == '4':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text.department_dpp, reply_markup=None)
            
            if str(call.data) == '5':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text.department_dtus, reply_markup=None)

            if str(call.data) == '6':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text.department_db, reply_markup=None)

            if str(call.data) == '7':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text.department_dib, reply_markup=None)
            
            if str(call.data) == '8':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text.department_dit, reply_markup=None)
            
            if str(call.data) == '9':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text.department_dl, reply_markup=None)
            
            if str(call.data) == '10':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text.department_dmr, reply_markup=None)
            
            if str(call.data) == '11':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text.department_kd, reply_markup=None)
            
            if str(call.data) == '12':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text.department_orb, reply_markup=None)
            
            if str(call.data) == '13':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text.department_ovk, reply_markup=None)
            
            if str(call.data) == '14':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text.department_fd, reply_markup=None)
            
            if str(call.data) == '15':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text.department_b2b, reply_markup=None)


    except Exception as e:
        print(repr(e))
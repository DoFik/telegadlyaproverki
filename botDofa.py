import telebot
import config
import random

bot = telebot.Telebot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome (message):
	sti = open('sticker/AnimatedSticker.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

    
    #клавиша
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.ReplyKeyboardButton("Рандомное число")
    item2 = types.ReplyKeyboardButton("Как делишки?:)")

    markup.add(item1, item2)

	bot.send_message(message.chat.id, "Привет, {0.first_name}|\nЯ создан - {1.first_name}</b>, чтобы поболтать.".format(message.from_user, bot.get_me()),)
        parse_mode='html', reply_markup=markup

@bot.message_handler(content_types=['text'])
def lal(message):
	if message.chat.type == 'private':
	    if message.text == 'Рандомное число':
	    	bot.send_message(message.shat.id, str(random.randint(0,100)))
        elif message.text == 'Как делишки?:)':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)

        	bot send_message(message.chat.id, 'Отлично,сам как?', reply_markup=markup)
        else:
        	bot send_message(message.chat.id, 'Я не знаю что сказать;(')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call_data == 'good'
               bot.send_message(call.message.chat.id, 'Вот и отлично;)')
            elif call.data == 'bad'
                bot.send_message(call.message.chat.id, 'Ну не чего;(')

            # удаление инлайновой клавиши

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Как делишки?:)",(
            reply_markup=None)

# Запуск моего бота

bot.polling(none_stop=True)
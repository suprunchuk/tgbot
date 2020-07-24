import telebot
bot = telebot.TeleBot("1247617685:AAFbEONVHzsE1s9g-JqTIRfvxGrKmBw9W_0")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, как тебя ховут?')
 
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Алексей':
        bot.send_message(message.chat.id, 'Какое-то у тебя плохое имя!')
    elif message.text == 'Станислав':
        bot.send_message(message.chat.id, 'Хорошее имя')      
    else:
        bot.send_message(message.chat.id, 'Введите имя Станислав либо Алексей')

bot.polling(none_stop=True)
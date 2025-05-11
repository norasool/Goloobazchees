import telebot
bot = telebot.TeleBot("7993730901:AAHXLQgjMwCKf2Ai-xbZjwuBn03paEMyzcE")
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, " ")
bot.polling()

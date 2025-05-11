import telebot
from telebot.types import ReplyKeyboardMarkup

bot = telebot.TeleBot("7993730901:AAHXLQgjMwCKf2Ai-xbZjwuBn03paEMyzcE")

@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("استارت")
    bot.send_message(message.chat.id, " ", reply_markup=markup)

bot.polling()

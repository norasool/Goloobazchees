import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot("7993730901:AAHXLQgjMwCKf2Ai-xbZjwuBn03paEMyzcE")  # توکن ربات خودت را جایگزین کن

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("استارت بازی", callback_data="start_game"))
    bot.send_message(message.chat.id, " ", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "start_game")
def handle_start(call):
    bot.send_message(call.message.chat.id, "این یک دکمه تست است. بازی واقعی نیاز به کدنویسی بیشتر دارد!")

bot.polling()

import os
from dotenv import load_dotenv
import telebot
from telebot.types import ReplyKeyboardMarkup

# بارگذاری توکن از فایل .env
load_dotenv()
TOKEN = os.getenv("TOKEN")  # توکن از محیطی ایمن خوانده می‌شود
bot = telebot.TeleBot(TOKEN)

# دستور /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("♟️ شروع بازی")
    bot.send_message(message.chat.id, " ", reply_markup=markup)

# پردازش دکمه شروع بازی
@bot.message_handler(func=lambda m: m.text == "♟️ شروع بازی")
def handle_start(message):
    bot.send_message(message.chat.id, " ")  # پیام خالی

# اجرای ربات
if __name__ == "__main__":
    bot.polling()

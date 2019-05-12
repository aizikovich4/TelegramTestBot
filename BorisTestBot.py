import telebot;
from telebot import apihelper

apihelper.proxy = {'http':'http://142.93.158.26:3128'}

bot = telebot.TeleBot("API_TOKEN");

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print("get new message")
    bot.reply_to(message, message.text)

bot.polling(none_stop=True, interval=500)
#bot.polling()


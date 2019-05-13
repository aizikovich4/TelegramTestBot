import telebot;
from telebot import apihelper

#apihelper.proxy = {'http':'http://142.93.158.26:3128'}

bot = telebot.TeleBot("");

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print("get new message") 
    print(message.chat)
    bot.send_message(message.chat.id, message.text+" from "+ (message.chat.last_name if message.chat.last_name else "") +" " + (message.chat.first_name if message.chat.first_name else "")+ " as "+ (message.chat.username if message.chat.username else "") )

bot.polling(none_stop=True)

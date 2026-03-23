import telebot
from telebot import types
from flask import Flask
from threading import Thread

# Блок для работы 24/7
app = Flask('')
@app.route('/')
def home(): return "Бот работает!"
def run(): app.run(host='0.0.0.0', port=8080)
def keep_alive():
    t = Thread(target=run)
    t.start()

# --- ВСТАВЬ СВОИ ДАННЫЕ ТУТ ---
TOKEN = '8659728408:AAHinMNx_Kaep7wfOLNZVTQmWDmLIhmD9cs'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("☕ Меню", "🍕 Заказать")
    bot.send_message(message.chat.id, "Привет! Это бот Кафе.", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "☕ Меню":
        bot.send_message(message.chat.id, "Кофе: 120 сом\nЧай: 80 сом")
    elif message.text == "🍕 Заказать":
        bot.send_message(message.chat.id, "Напишите ваш заказ!")

if __name__ == "__main__":
    keep_alive()
    print("Бот запущен!")
    bot.polling(none_stop=True)

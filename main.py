import telebot
from flask import Flask
from threading import Thread
import os

# 1. ВСТАВЬ СВОЙ ТОКЕН НИЖЕ
TOKEN = "8659728408:AAHinMNx_Kaep7wfOLNZVTQmWDmLIhmD9cs"
bot = telebot.TeleBot(TOKEN)

# 2. НАСТРОЙКА ВЕБ-СЕРВЕРА (для Render 24/7)
app = Flask('')

@app.route('/')
def home():
    return "Бот кафе в Таласе работает 24/7!"

def run():
    # Render сам назначит порт, берем его из настроек системы
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- ТВОИ КОМАНДЫ БОТА (ПРИМЕР) ---
# Сюда вставь все свои @bot.message_handler, которые у тебя были

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Салам! Бот кафе в Таласе запущен и готов принимать заказы!")

# --- ЗАПУСК ---

if __name__ == "__main__":
    # Сначала запускаем веб-сервер в отдельном потоке
    keep_alive()
    print("Веб-сервер запущен, бот начинает работу...")
    
    # Затем запускаем самого бота
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Ошибка бота: {e}")

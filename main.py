import telebot # для работы с телеграм-ботом
import requests # для отправки запросов к веб-приложению
from telebot import types # для создания кнопок

# Создаем объект бота с помощью токена
bot = telebot.TeleBot("6521190956:AAHW9a3jRxJ9DE6V92TQsAm0hGPSdky_aYc")

# Функция для обработки команды /start
@bot.message_handler(commands=["start"])
def start(message):
    # Создаем объект клавиатуры
    keyboard = types.InlineKeyboardMarkup()
    # Создаем кнопку с текстом "Открыть веб-приложение" и url-адресом веб-приложения
    button = types.InlineKeyboardButton(text="Открыть веб-приложение", url= "https://hao124577.github.io/goter/")
    # Добавляем кнопку на клавиатуру
    keyboard.add(button)
    # Отправляем приветственное сообщение с фотографией и клавиатурой
    bot.send_photo(message.chat.id, photo=open("photo.jpg", "rb"), caption="Привет, я твой телеграм-бот!", reply_markup=keyboard)

# Запускаем бота
bot.polling()
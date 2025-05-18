import telebot
import requests
from test import API_TOKEN, BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands = ["start"])
def start(message):
    bot.send_message(message.chat.id, "Приветствую, человек. So far я знаю онли погоду в реальном времени, но wait for a while я тебя еще удивлю )")

@bot.message_handler(commands = ["weather"])
def weather(message):
    try:
        name = message.text.split(maxsplit = 1)[1]
    except IndexError:
        bot.send_message(message.chat.id, "! Укажи город после команды. Пример: /weather Афины")
        return

    params = {
            "q" : name,
            "appid" : API_TOKEN,
            "units" : "metric",
            "lang" : "ru"
        }

    response = requests.get("https://api.openweathermap.org/data/2.5/weather", params = params)

    if response.status_code == 200:
        data = response.json()
        name = data["name"]
        weather = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        w = data["wind"]["speed"]

        text = (
            f"📍Город: {name}\n"
            f"🌤️Погода: {weather}\n"
            f"🌡️Температура: {temp}ºC\n"
            f"💨Ветер: {w} м/с"
        )

        bot.send_message(message.chat.id, text)
    else:
        bot.send_message(message.chat.id, "Проверь название города )")

bot.polling(none_stop = True)
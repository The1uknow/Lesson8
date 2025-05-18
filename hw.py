# i = lambda q, w: q + w
# q = int(input("Enter a number: "))
# w = int(input("Enter one more number: "))
# print(i(q, w))


import requests
from test import API_TOKEN
params = {
    "q" : "Ташкент",
    "appid" : API_TOKEN,
    "units" : "metric",
    "lang" : "ru"
}
response = requests.get("https://api.openweathermap.org/data/2.5/weather", params = params)

if response.status_code == 200:
    data = response.json()

    name = data["name"]
    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    w = data["wind"]["speed"]

    print(f"📍Город: {name}")
    print(f"🌤️Погода: {weather}")
    print(f"🌡️Температура: {temp}")
    print(f"💨Ветер: {w}")
else:
    print(response.status_code)
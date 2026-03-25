import requests


def get_weather():
    city = input("Введите название города: ")
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'units': 'metric',
        'lang': 'ru',
        'appid': '79d1ca96933b0328e1c7e3e7a26cb347'
    }
    weather_data = requests.get(url, params=params).json()
    if weather_data.get('cod') != 200:
        print(f"Ошибка: {weather_data.get('message', 'Неизвестная ошибка')}")
        return

    temperature = round(weather_data['main']['temp'])
    temperature_feels_like = round(weather_data['main']['feels_like'])
    wind_speed = round(weather_data['wind']['speed'])
    pressure = round(weather_data['main']['pressure'])
    humidity = round(weather_data['main']['humidity'])
    description = weather_data['weather'][0]['description']
    print("\n" + "="*40)
    print(f"Погода в городе {city}".center(40))
    print("="*40)
    print(f"Температура:        {temperature}°C (ощущается как {temperature_feels_like}°C)")
    print(f"Ветер:              {wind_speed} м/с")
    print(f"Давление:           {pressure} гПа")
    print(f"Влажность:          {humidity}%")
    print(f"Погода:             {description.capitalize()}")
    print("="*40)


if __name__ == "__main__":
    get_weather()

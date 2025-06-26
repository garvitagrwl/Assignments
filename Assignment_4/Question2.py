import requests

def weather(city):
    url =  f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=74508250e2ed7f13e22fe34a8a1ae897"

    try:
        response = requests.get(url)
        data = response.json()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        feels_like = data["main"]["feels_like"]
        w = data["weather"][0]["description"]

        print(f"Weather in {city}:")
        print(f'''
        Temperature        : {temperature} Kelvin (Feels Like : {feels_like} Kelvin)
        Humidity           : {humidity}%
        Weather Description: {w.capitalize()}
        Sunrise            : {data["sys"]["sunrise"]} Unix Timestamp
        Sunset             : {data["sys"]["sunset"]} Unix Timestamp
        Sea Level          : {data["main"]["sea_level"]} Meters
        Wind Speed         : {data["wind"]["speed"]} Km/H
        ''')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

city = input("Enter the city name:")
weather(city)
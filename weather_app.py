#DAY-46

import requests

#api_key = [redacted]
url = 'http://api.openweathermap.org/data/2.5/weather'

def weather(city):
    comp_url = f'{url}?q={city}&appid={api_key}&units=metric'

    response = requests.get(comp_url)

    if response.status_code == 200:
        data = response.json()

        main_data = data['main']
        weather_data = data['weather'][0]
        wind_data = data['wind']

        city_name = data['name']
        temperature = main_data['temp']
        pressure = main_data['pressure']
        humidity = main_data['humidity']
        description = weather_data['description']
        wind_speed = wind_data['speed']

        print(f'Weather in {city_name}: ')
        print(f'Temperature: {temperature} degrees Celsius')
        print(f'Pressure: {pressure} hPa')
        print(f'Humidity: {humidity}%')
        print(f'Description: {description}')
        print(f'Wind Speed: {wind_speed} m/s')
    else:
        print("City not found or invalid API key")

city = input("Enter the city name: ")
weather(city)


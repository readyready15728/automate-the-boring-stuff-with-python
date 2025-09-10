import json
import os
import requests


def kelvins_to_celsius(temperature):
    return round(temperature - 273.15, 1)


def kelvins_to_fahrenheit(temperature):
    return round(temperature * 9 / 5 - 459.67, 1)


city_name = 'San Francisco'
state_code = 'CA'
country_code = 'US'
api_key = os.getenv('OPEN_WEATHER_API_KEY')

# Determine unprojected coordinates of city at first
response = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={api_key}')
response_data = json.loads(response.text)

lat = response_data[0]['lat']
lon = response_data[0]['lon']

# Now determine temperature at coordinates
response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}')
response_data = json.loads(response.text)

kelvins = response_data['main']['temp']
fahrenheit = kelvins_to_fahrenheit(kelvins)
celsius = kelvins_to_celsius(kelvins)

kelvins_fl = response_data['main']['feels_like']
fahrenheit_fl = kelvins_to_fahrenheit(kelvins_fl)
celsius_fl = kelvins_to_celsius(kelvins_fl)

print(f'Weather for {city_name}, {state_code}:')
print()
print(f"{response_data['weather'][0]['main']} ({response_data['weather'][0]['description'].title()})")
print(f'Temperature: {fahrenheit} °F / {celsius} °C')
print(f'Feels Like: {fahrenheit_fl} °F / {celsius_fl} °C')
print(f"Humidity: {response_data['main']['humidity']}%")

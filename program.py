import requests
from utils import get_city_woeid

city = input("Which city do you want to know the weather of?\n> ")

woeid = get_city_woeid(city)

url = f"https://www.metaweather.com/api/location/{woeid}/"
response = requests.get(url)
data = response.json()

for day in data['consolidated_weather']:
    weather = day['weather_state_name']
    date = day['applicable_date']
    temp = round(day['max_temp'], 1)
    print(f"- {date}: {weather} ({temp} C)")
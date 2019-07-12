import requests

city = input("Which city do you want to know the weather of?\n> ")
url = f"https://www.metaweather.com/api/location/search/?query={city}"

response = requests.get(url)
data = response.json()
woeid = data[0]['woeid']

url = f"https://www.metaweather.com/api/location/{woeid}/"
response = requests.get(url)
data = response.json()

for day in data['consolidated_weather']:
    weather = day['weather_state_name']
    date = day['applicable_date']
    temp = round(day['max_temp'], 1)
    print(f"- {date}: {weather} ({temp} C)")
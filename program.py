import requests

city = input("City?\n> ")
url = f"https://www.metaweather.com/api/location/search/?query={city}"

response = requests.get(url)
data = response.json()
woeid = data[0]['woeid']

print(woeid)
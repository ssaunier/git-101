import requests

def get_city_woeid(city):
    url = f"https://www.metaweather.com/api/location/search/?query={city}"

    response = requests.get(url)
    data = response.json()
    woeid = data[0]['woeid']
    
    return woeid
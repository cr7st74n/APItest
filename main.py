import requests
from pprint import pprint
import os

print("Hello, welcome to my weather API app")

apiKey = os.environ.get('WEATHER_KEY')


url = f"http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid={apiKey}"

dataLonLat = requests.get(url).json()
query = {"q":"azogues", "units":"metric", "appid":apiKey}



lat = dataLonLat[0]["lat"]
lon = dataLonLat[0]["lon"]

weatherURL = 'https://api.openweathermap.org/data/2.5/weather'

dataWeather = requests.get(weatherURL, params=query).json()

pprint(dataWeather)
print(dataWeather["weather"])

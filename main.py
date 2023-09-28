import requests
from pprint import pprint
import os
import time
from datetime import datetime

# User part 
print("Hello, welcome to my weather API app")

userCountry = input("Enter the country that you would like to know the 5-day forecast!\n")

# Get our Data from the API 
apiKey = os.environ.get('WEATHER_KEY')

query = {"q":userCountry, "units":"Imperial", "appid":apiKey}
queryForecast = {"q":userCountry, "units":"Imperial","appid":apiKey}

# 5 day Forecast
forecastURL = "https://api.openweathermap.org/data/2.5/forecast"
weatherURL = "https://api.openweathermap.org/data/2.5/weather"

dataWeather = requests.get(weatherURL, params=query).json()
forecastWeather = requests.get(forecastURL, params=queryForecast).json()


# pprint(dataWeather)
tempeture = dataWeather["main"]["temp"]
weatherDescription = dataWeather["weather"][0]["description"]
windSpeed = dataWeather["wind"]["speed"]

print(f"The Tempeture for: {userCountry} is: {tempeture}F \n")
print(f"The weather description is: {weatherDescription} \n")
print(f"The wind speed is: {windSpeed} \n")

forecastList = forecastWeather["list"]

for days in forecastList:

    print(f"At this time: {datetime.fromtimestamp( days['dt'])} \n")
    print("the Weather for this day is... \n")
    print(f"tempeture: {days['main']['temp']} \n")
    print(f"weather: {days['weather'][0]['description']} \n")
    print(f"wind: {days['wind']['speed']} \n")
    # print(f" date: {days['dt_txt']},tempeture: {['main']['temp']}, weather: {days['weather'][0]['description']}, {days['wind']['speed']}")

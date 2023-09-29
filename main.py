import requests
from pprint import pprint
import os
from datetime import datetime
import logging

# Key
apiKey = os.environ.get('WEATHER_KEY')
# User part 

def main():
    print("Hello, welcome to my weather API app")
    userCity = ""
    while len(userCity) == 0:
        userCity = input("Enter the city that you would like to know the 5-day forecast!\n").strip()
    weather,error = get_weather(userCity,apiKey)
    if error:
        print("Sorry, there is an error with your request.")
    else:
        print(f"\nThe weather in {userCity} is: \n")
        printData = ShowWeather(weather)
        printData


# Get our Data from the API 
def get_weather(city, key):
    try:
        queryForecast = {"q":city, "units":"Imperial","appid":key}

        # 5 day Forecast
        forecastURL = "https://api.openweathermap.org/data/2.5/forecast"

        forecastWeather = requests.get(forecastURL, params=queryForecast).json()
        # forecastWeather.raise_for_status() # raise exr for 400 or 500 err 

        forecastList = forecastWeather["list"]

        return forecastList, None

    except Exception as exc:
        print(exc)
        print("Error at getting the API")
        return None, exc

# Show to data will print the 5 day Forecast
def ShowWeather(data):
    try:
        for days in data:
            print(f"At this time: {datetime.fromtimestamp( days['dt'])} \n#the Weather for this day is...") # Unix time here ! Used to show the local time depending on the location.
            print(f"-tempeture: {days['main']['temp']}F \n-weather Descripton: {days['weather'][0]['description']} \n-wind speed: {days['wind']['speed']} \n")
    except KeyError:
        print("The data is not in the correct format")
        return "Unknown"
    
if __name__ == "__main__":
    main()

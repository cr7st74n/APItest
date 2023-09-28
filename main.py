import requests
print("Hello, welcome to my weather API app")

apiKey = "c59053e9cfd68c4fcf70f81e077a7583"

dataLonLat = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid={apiKey}").json()

lat = dataLonLat[0]["lat"]
lon = dataLonLat[0]["lon"]


dataWeather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apiKey}').json()

print(dataWeather["weather"])
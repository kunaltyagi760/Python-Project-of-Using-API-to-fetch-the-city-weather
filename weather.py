import requests

base_url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = "40ad1445a178b4e381d1267934f15a85"
city = input("Enter the city name : ")

url = base_url + "appid=" + api_key + "&q=" + city

response = requests.get(url).json()

temperature_in_celcius = response['main']['temp'] - 273.15

print("The temperature in", city, "is", temperature_in_celcius, "°C")
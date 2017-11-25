# -*- coding: utf-8 -*-

from geopy.geocoders import Nominatim

api_key = "f05f15a9dee99b552764a634f8d6407e"
address = "Oxford"

def Get_weather(address, api_key):
	geolocator = Nominatim()
	location = geolocator.geocode(address)
	latitude = location.latitude
	longitude = location.longitude
	forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
	summary = forecast.summary
	temperature = forecast.temperature
	return "Hello fello slackers! The wather is {} and {}° at {}".format(summary, temperature, address)

print(Get_weather(address, api_key))

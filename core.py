import urllib.request
import json
import ast

def Weather(API):
	lat   =  str(input("Latitude  : "))
	lon   =  str(input("Longitude : "))
	units = "metric"

	url	  = "https://api.openweathermap.org/data/2.5/weather?lat={}&units={}&lon={}&appid={}"
	call  = url.format(lat, units, lon, API)
	get   = urllib.request.Request(call,None)

	with urllib.request.urlopen(get) as response:
		read = response.read()
		read = read.decode("UTF-8")
		read = ast.literal_eval(read) # Tidying the messy response...

	# Filtering
	city = read.get("name")

	weather 	= read.get("weather") # general description
	weather 	= weather[0]
	description = weather["description"]

	main 		= read.get("main") # temp(in celcius), humidity, etc
	temperature = str(main["temp"])
	real_feel   = str(main["feels_like"])
	pressure    = str(main["pressure"])
	humidity    = str(main["humidity"])

	visibility = read.get("visibility") 
	visibility = str(float(visibility/1000)) # from meters to kilometers

	# Final Result
	print("City        : " + city)
	print("Weather     : " + description)
	print("Temperature : " + temperature + " Celcius")
	print("Feels Like  : " + real_feel + " Celcius")
	print("Pressure    : " + pressure + " hPa")
	print("Humidity    : " + humidity + " %")
	print("Visibility  : " + visibility + " Kilometers")
import core

def Get_API():
	with open("API.txt", "w") as wAPI:
		API = str(input("Type in your API : "))
		wAPI.write(API)

def Read_API():
	with open("API.txt", "r") as reader:
		API = reader.readline()
		core.Weather(API)

def Flush_API():
	with open("API.txt", "w") as clear:
		clear.write("")

# check Get_API already exist with a valid api or not
try: 
	with open("API.txt", "r") as check:
		if check.readline() != "": # API Exists
			preload.Read_API()
		else:
			preload.Get_API() # API has never been inputted
			preload.Read_API()
except:
	print("Either invalid API or API.txt is missing\nExiting...")
	preload.Flush_API()
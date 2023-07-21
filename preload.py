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
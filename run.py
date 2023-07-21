import preload
import core

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
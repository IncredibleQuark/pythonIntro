import simplejson as json
import os

new_file = open("newFile.txt", "w+")
string = "Content to be written in file."
new_file.write(string)


if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:  # Check if the file exists and has some data
	old_file = open("./ages.json", "r+")
	data = json.loads(old_file.read())
	print("Current age is", data["age"], "-- adding a year.")
	data["age"] = data["age"] + 1
	print("New age is", data["age"])
else:
	old_file = open("./ages.json", "w+")
	data = {"name": "Mark", "age": 24}
	print("No file found, set as default age to:", data["age"])

old_file.seek(0)
old_file.write(json.dumps(data))

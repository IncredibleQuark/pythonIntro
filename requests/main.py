import requests
from io import BytesIO
from PIL import Image

request = requests.get("https://google.com")
print("Status:", request.status_code)
print("URL:", request.url)
f = open("./page.html", "w+")
f.write(request.text)

params = {"q": 'house'}
request2 = requests.get("https://bing.com/search", params=params)
print(request2.url)

request3 = requests.get("https://linux.pictures/content/1-projects/163-picture-for-github-users-who-fork-open-source-projects/githubopen-demo.png")

print("Status code:", request3.status_code)

image = Image.open(BytesIO(request3.content))
print(image.size, image.format, image.mode)
path = "./image." + image.format

try:
	image.save(path, image.format)
except IOError:
	print("Can not save image")

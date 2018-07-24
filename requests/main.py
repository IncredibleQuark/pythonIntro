import requests

request = requests.get("https://google.com")
print("Status:", request.status_code)
print("URL:", request.url)
f = open("./page.html", "w+")
f.write(request.text)

params = {"q": 'house'}
request2 = requests.get("https://bing.com/search", params=params)
print(request2.url)

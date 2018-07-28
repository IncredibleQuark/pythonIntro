from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os


def start_search():

	search = input("Enter Search Word:")
	params = {"q": search}
	dir_name = search.replace(" ", "_").lower()

	if not os.path.isdir(dir_name):
		os.makedirs(dir_name)

	#  Search text results
	request = requests.get("https://www.bing.com/search", params=params)

	soup = BeautifulSoup(request.text, "html.parser")
	results = soup.find("ol", {"id": "b_results"})
	links = results.findAll("li", {"class": "b_algo"})

	for item in links:
		item_text = item.find("a").text
		item_href = item.find("a").attrs["href"]

		if item_text and item_href:
			print(item_text)
			print(item_href)
			print("Summary:", item.find("p").text)

	# Search for images
	request_images = requests.get("https://www.bing.com/images/search", params=params)
	soup_images = BeautifulSoup(request_images.text, "html.parser")
	images_links = soup_images.findAll("a", {"class": "thumb"})

	for item in images_links:
		try:
			img_obj = requests.get(item.attrs["href"])
			print("Getting", item.attrs["href"])
			title = item.attrs["href"].split("/")[-1]
			try:
				img = Image.open(BytesIO(img_obj.content))
				img.save("./" + dir_name + "/" + title, img.format)
			except:
				print("Could not save image", item.attrs["href"])
		except:
			print("Could not request image")

	start_search()


start_search()

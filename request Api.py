import requests
import json

page = requests.get(" https://itunes.apple.com/search?term=Ann+Arbor&entity=podcast")
print(type(page))
print(page.text[:150]) # print the first 150 characters
print(page.url) # print the url that was fetched
print("------")

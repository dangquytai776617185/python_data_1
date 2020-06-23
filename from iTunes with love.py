import requests
import json

baseurl = "https://itunes.apple.com/search"
params_dict = {}
params_dict["term"] = "james arthur"
params_dict["entity"] = "song"
req = requests.get(baseurl, params = params_dict) #requests data from url
data = json.loads(req.text) #work with data in json.format
for dit in data["results"]:
    print(dit["collectionName"] + "---" + dit["trackName"] + "---" + dit["previewUrl"])
#print(data)
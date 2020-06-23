import requests
import json

page = requests.get("https://api.datamuse.com/words?ml=ringing+in+the+ears&max=4")
#print(page.headers.keys())
x = page.json()
print(json.dumps(x, indent = 2))

#print(x["results"][0])
##print(dit["collectionName"] + "---" + dit["trackName"])
#print(page.status_code)
#print(page.headers)
for dit in x:
    print(dit["word"] + "--"+ str(dit["score"]))
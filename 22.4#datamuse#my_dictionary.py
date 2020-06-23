# import statements for necessary Python modules
import requests
import json

def get_mean(word):
    baseurl = "https://api.datamuse.com/words"
    params_diction = {} # Set up an empty dictionary for query parameters
    params_diction["ml"] = word
    params_diction["max"] = "3" # get at most 3 results
    params_diction["md"] = "d"
    resp = requests.get(baseurl, params=params_diction)
    # return the top three words
    word_ds = json.loads(resp.text)
    for d in word_ds:
        print(d["word"], d["defs"])
    return "--------"
    #return resp.json() # Return a python object (a list of dictionaries in this case)
word = input("Enter your word please: ")
print(get_mean(word))


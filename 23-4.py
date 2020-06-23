import requests

import requests
def requestsURL(baseurl, params = {}):
    # This function accepts a URL path and a params diction as inputs.
    # It calls requests.get() with those inputs,
    # and returns the full URL of the data you want to get.
    req = requests.Request(method = 'GET', url = baseurl, params = params)
    #prepped = req.prepare()
    return req.url
print(requestsURL("htpp://www.google.com/search", {"tbm":"isch", "q":"violins and guitars"}))

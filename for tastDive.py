import requests

tastedive_key = "367007-dangquyt-VSK39QKH"
def get_movies_from_tastedive(name):       #extracted from tastedive.com 
    baseurl = "https://tastedive.com/api/similar"
    params_diction = {}
    params_diction["k"] = tastedive_key
    params_diction["q"] = name
    params_diction["type"] = "movies"
    params_diction["limit"] = 5
    tastedive_req = requests.get(baseurl, params = params_diction)
    print(tastedive_req.url)
    return tastedive_req.json()
print(get_movies_from_tastedive("batman"))
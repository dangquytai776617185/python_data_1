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
#data = get_movies_from_tastedive("black panther")
def extract_movie_titles(dit_from_tastedive): # extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive
    movies_titles = []
    for movie in dit_from_tastedive["Similar"]["Results"]:
        movies_titles.append(movie["Name"])
    return movies_titles
#print(extract_movie_titles(data))

def get_related_movies(list_movies_title): #, called get_related_titles. It takes a list of movie titles as input. It gets five related movies for each from TasteDive, extracts the titles for all of them, and combines them all into a single list
    related_movies = []
    for movie in list_movies_title:
        if movie not in related_movies:
            related_movies.append(movie)
        data_2 = get_movies_from_tastedive(movie)
        movies_titles_2 = extract_movie_titles(data_2)
        for movie_2 in movies_titles_2:
            if movie_2 not in related_movies:
                related_movies.append(movie_2)
    return related_movies
#print(get_related_movies(extract_movie_titles(data)))


omdb_api_key = "fe23422a"
i = "tt3896198"
def get_movie_data(movie):   #The function should return a dictionary with information about that movie.
    baseurl = "https://www.omdbapi.com/"
    params_diction = {}
    params_diction["i"] = i
    params_diction["apikey"] = omdb_api_key
    params_diction["t"] = movie
    omdb_api_req = requests.get(baseurl, params = params_diction)
    #print(omdb_api_req.url)
    return omdb_api_req.json()
print(get_movie_data("batman"))


def get_movie_rating(data_from_omdb): #. It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer
    for dit in data_from_omdb["Ratings"]:
        if dit["Source"] == "Rotten Tomatoes":
            return dit["Value"]
    return "Dont have Rotteen's rating"
print(get_movie_rating(get_movie_data("batman")))

def get_sorted_recommendations(related_movies): #It takes a list of movie titles as an input. It returns a sorted list of related movie titles as output, up to five related movies for each input movie title.
    dict_movies = {}
    for movie in related_movies:
        dict_movies[movie] = get_movie_rating(get_movie_data(movie))
    final_list_movie = sorted(dict_movies.keys(), key= lambda x:(dict_movies[x], len(x)), reverse= True)
    for movie in dict_movies:
        print(movie + ":" + dict_movies[movie])
    return final_list_movie


#print(get_sorted_recommendations(get_related_movies(extract_movie_titles(get_movies_from_tastedive("batman")))))




    
    

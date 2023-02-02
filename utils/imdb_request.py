import requests

def get_movie_id(movie, key):
    url = f"https://imdb-api.com/en/API/Search/{key}/{movie}
    r = requests.get(url)
    result = r.json()["results"][0]
    print(result)

def get_cast_list():
    pass

def union_of_actors():
    pass
import requests


def get_movie_id(movie, key):
    url = f"https://imdb-api.com/en/API/Search/{key}/{movie}"
    r = requests.get(url)
    movie_id = r.json()["results"][0]['id']
    return movie_id


def get_cast_list(movie_id, key):
    url = f"https://imdb-api.com/en/API/FullCast/{key}/{movie_id}"
    r = requests.get(url)
    cast_list_dicts = r.json()["actors"]
    cast_list = [item["name"] for item in cast_list_dicts]
    return cast_list


def union_of_casts(movie_cast_1, movie_cast_2):
    return list(set(movie_cast_1) & set(movie_cast_2))

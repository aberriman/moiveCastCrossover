import requests


def get_movie_id(movie, key):
    url = f"https://imdb-api.com/en/API/Search/{key}/{movie}"
    r = requests.get(url)
    movie_id = r.json()["results"][0]['id']
    return movie_id


def get_cast_list(movie_id, key):
    url = f"https://imdb-api.com/en/API/FullCast/{key}/{movie_id}"
    r = requests.get(url)
    cast_list_dict = r.json()["actors"]
    cast_list = [item["name"] for item in cast_list_dict]
    return cast_list_dict, cast_list


def intersect_of_casts(movie_cast_1, movie_cast_2):
    return list(set(movie_cast_1) & set(movie_cast_2))


def make_actor_dict(intersection, movie_dict_1, movie_dict_2):
    actors = dict()
    for cast_member in movie_dict_1:
        if cast_member["name"] in intersection:
            actors[cast_member["name"]] = dict()
            actors[cast_member["name"]]["image"] = cast_member["image"]
            actors[cast_member["name"]]["Character_1"] = cast_member["asCharacter"]

    for cast_member in movie_dict_2:
        if cast_member["name"] in intersection:
            actors[cast_member["name"]]["Character_2"] = cast_member["asCharacter"]

    return actors


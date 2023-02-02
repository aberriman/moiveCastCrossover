import requests
import argparse
from utils.imdb_request import get_movie_id, get_cast_list, union_of_actors


def cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--movie1", type=str, help="The full name of the first movie")
    parser.add_argument("--movie2", type=str, help="The full name of the second movie")
    parser.add_argument("--key", type=str, help="Your API key for IMDB")
    return parser.parse_args()


def main(movie1, movie2, key):
    get_movie_id(movie1, key)

    result = r.json()["actors"]
    print(result)


if __name__ == '__main__':
    args = cli_args()
    main()

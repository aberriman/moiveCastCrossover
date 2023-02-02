import argparse
from utils.imdb_request import get_movie_id, get_cast_list, union_of_casts


def cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--movie1", type=str, help="The full name of the first movie")
    parser.add_argument("--movie2", type=str, help="The full name of the second movie")
    parser.add_argument("--key", type=str, help="Your API key for IMDB")
    return parser.parse_args()


def main(movie1, movie2, key):
    movie1_id = get_movie_id(movie1, key)
    movie2_id = get_movie_id(movie2, key)

    movie_cast_1 = get_cast_list(movie1_id, key)
    movie_cast_2 = get_cast_list(movie2_id, key)

    intersect = union_of_casts(movie_cast_1, movie_cast_2)
    print(intersect)


if __name__ == '__main__':
    args = cli_args()
    main(args.movie1, args.movie2, args.key)

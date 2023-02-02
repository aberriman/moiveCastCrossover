import requests
import argparse


def cli_args():
    pass


def main():
    r = requests.get("https://imdb-api.com/en/API/Search/k_azrb9zi7/inception 2010")
    result = r.json()["results"]
    print(result[0])
    print(result[1])

    r = requests.get("https://imdb-api.com/en/API/Fullcast/k_azrb9zi7/tt1375666")
    result = r.json()["actors"]
    print(result)


if __name__ == '__main__':
    main()

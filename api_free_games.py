from requests import get
from tabulate import tabulate

BASE_URL = "https://www.freetogame.com/api"


def call_url(url):
    response = get(url)
    if response.status_code == 200:
        return response.json()


def get_all_games():
    return f"{BASE_URL}/games"


def get_games_by_platform(platform):
    platform = platform.lower()

    return f"{BASE_URL}/games?platform={platform}"


def get_games_by_tag(tag):
    tag = tag.lower()

    return f"{BASE_URL}/games?category={tag}"


def get_games_by_platform_and_category(platform, category):
    if platform and category:

        category = category.lower()
        platform = platform.lower()

        filters = f"platform={platform}&category={category}"

        return f"{BASE_URL}/games?{filters}"


def make_game_list(json):

    headers = ["Id", "Title", "Genre", "Platform"]
    rows = []

    for game in json:
        row = [
            game["id"],
            game["title"],
            game["genre"],
            game["platform"],
        ]
        rows.append(row)

    return tabulate(rows, headers=headers)

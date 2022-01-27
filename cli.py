from argparse import ArgumentParser
from tabulate import tabulate
from api_free_games import (
    get_all_games,
    get_games_by_platform,
    get_games_by_tag,
    get_games_by_platform_and_category,
    call_url,
    make_game_list,
)


def show_platforms_and_tags():
    platforms = [("Platform",), ("pc",), ("browser",), ("all",), ]

    print(tabulate(platforms, headers="firstrow"))
    print("\n")

    tags = [
        ("Tag",),
        ("mmorpg",),
        ("shooter",),
        ("strategy",),
        ("moba",),
        ("racing",),
        ("sports",),
        ("social",),
        ("sandbox",),
        ("open-world",),
        ("survival",),
        ("pvp",),
        ("pve",),
        ("pixel",),
        ("voxel",),
        ("zombie",),
        ("turn-based",),
        ("first-person",),
        ("third-Person",),
        ("top-down",),
        ("tank",),
        ("space",),
        ("sailing",),
        ("side-scroller",),
        ("superhero",),
        ("permadeath",),
        ("card",),
        ("battle-royale",),
        ("mmo",),
        ("mmofps",),
        ("mmotps",),
        ("3d",),
        ("2d",),
        ("anime",),
        ("fantasy",),
        ("sci-fi",),
        ("fighting",),
        ("action-rpg",),
        ("action",),
        ("military",),
        ("martial-arts",),
        ("flight",),
        ("low-spec",),
        ("tower-defense",),
        ("horror",),
        ("mmorts",),
    ]

    print(tabulate(tags, headers="firstrow"))


ACTIONS = {
    "all":
    get_all_games,

    "by_platform":
    get_games_by_platform,

    "by_tag":
    get_games_by_tag,

    "by_platform_and_category":
    get_games_by_platform_and_category,

    "show_platforms_and_tags":
    show_platforms_and_tags,
}


def main():
    parser = ArgumentParser(description="")

    parser.add_argument(
        "-f",
        "--function",
        required=True,
        help="all | by_platform | by_tag | "
        "by_platform_and_category | show_platforms_and_tags"
    )

    parser.add_argument(
        "-a",
        "--args",
        nargs="*",
        type=str,
        required=False,
        help="List of params"
    )

    args = parser.parse_args()

    action = ACTIONS[args.function]

    url = None

    if action is show_platforms_and_tags:
        show_platforms_and_tags()

    elif action is get_all_games:
        url = action()

    else:
        url = action(*args.args)

    if url:
        json = call_url(url)
        print(make_game_list(json))


main()

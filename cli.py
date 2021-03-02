import click
import requests


def get_played_hands(url: str):
    """
    Gets played hands from specified url
    :param url
    """

    try:
        response = requests.get(url).json()
        return response
    except AttributeError as ae:
        print(f"Failed to load JSON file with err: ${ae}")


@click.command()
@click.argument("url")
def main(url):
    """
    :param url
    """
    played_hands = get_played_hands(url)

    print(played_hands)


if __name__ == "__main__":
    main()

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

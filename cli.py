import click
from app.utils import parse_played_hands
from app.game.jack import evaluate_games


@click.command()
@click.argument("url")
def main(url):
    """
    :param url
    """
    played_hands = parse_played_hands.get_played_hands(url)
    results = evaluate_games(played_hands)

    print(results)


if __name__ == "__main__":
    main()

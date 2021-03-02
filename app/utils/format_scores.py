from tabulate import tabulate


def format_scores(hand: int, player_a_score: int, player_b_score: int, winner: str) -> list:
    """
    Format play scores
    :param hand The hand that has been played. The index value of the game, starting from 1
    :type hand int
    :param player_a_score
    :type player_a_score int
    :param player_b_score
    :type player_b_score int
    :param winner
    :returns: string representation of player scores
    :rtype: str
    """
    return [hand, player_a_score, player_b_score, winner]


def format_results(results):
    return tabulate(results, headers=["Hand", "Player A Score", "Player B Score", "Winner"])

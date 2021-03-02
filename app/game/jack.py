from app.utils.scores import score_matrix
from app.utils.format_scores import format_scores, format_results


def evaluate_games(games: list):
    """
    Evaluates winners in a list of games
    :param games
    :type games str
    """
    results = []

    for game_count, game in enumerate(games, start=1):
        result_of_game = winner_of_hand(game_count, game)
        if result_of_game is not None:
            results.append(result_of_game)

    return format_results(results)


def winner_of_hand(game_count: int, game: dict) -> list:
    """
    Evaluates the winner in a game
    :param game_count Index of the game
    :type game_count int
    :param game The game
    :type game dict
    """
    player_a_cards = game["playerA"]
    player_b_cards = game["playerB"]

    player_a_score = get_player_score(player_a_cards)
    player_b_score = get_player_score(player_b_cards)

    if player_a_score > 21:
        return format_scores(game_count, player_a_score, player_b_score, "Player B")

    if player_b_score > 21:
        return format_scores(game_count, player_a_score, player_b_score, "Player A")

    if player_b_score > player_a_score:
        return format_scores(game_count, player_a_score, player_b_score, "Player B")

    if player_a_score > player_b_score:
        return format_scores(game_count, player_a_score, player_b_score, "Player A")

    if player_a_score == player_b_score:
        return tie_breaker(game_count, player_a_cards, player_b_cards)


def get_player_score(cards: list) -> int:
    """
    Evaluates player's current score based on the cards they have. Cards will be a list of strings
    :param cards
    :type cards list
    """
    total_score = 0

    for card in cards:
        score = score_matrix[card[:-1]]
        total_score += score

    return total_score


def tie_breaker(game_count: int, player_a_cards: list, player_b_cards: list) -> list:
    # return format_scores(player_a_score, player_b_score, "Player A Wins")
    pass
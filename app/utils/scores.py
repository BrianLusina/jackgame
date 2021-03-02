score_matrix = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}

ranks = {
    "K": 3,
    "Q": 2,
    "J": 1,
    "10": 0
}

# arbitrary value numbers to denote ranking of suits. Highest is 4, lowest is 1
suits = {
    "S": 4,
    "H": 3,
    "C": 2,
    "D": 1
}


def sorter(card: str):
    """
    Custom sorting function to sort cards based on the highest single value provided the score matrix
    :param card
    :type card str
    """
    return score_matrix[card[:-1]]


def compare_suits(suit_a: str, suit_b: str) -> bool:
    """
    Compares 2 suits from 2 cards & returns true if suit_a is greater than suit_b
    :param suit_a Suit A from Card A
    :type suit_a str
    :param suit_b Suit B from Card B
    :type suit_b str
    """
    return suits[suit_a] > suits[suit_b]

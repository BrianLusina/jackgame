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

suits = {
    "S",
    "H",
    "C",
    "D"
}


def sorter(card: str):
    """
    Custom sorting function to sort cards based on the highest single value provided the score matrix
    :param card
    :type card str
    """
    return score_matrix[card[:-1]]

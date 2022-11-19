SUITS = ('♥', '♦', '♠', '♣')

RANKS = ('2', '3', '4', '5', '6', '7', '8',
         '9', '10', 'J', 'Q', 'K', 'A')

CARD_VALUES = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 11   # Can be adjusted.
}


class Card:
    def __init__(self, rank, suit):
        self.__rank = rank
        self.__suit = suit
        self.__value = CARD_VALUES[self.__rank]

    @property
    def get_card(self):
        return Card(self.__rank, self.__suit)

    @property
    def get_rank(self):
        return self.__rank

    @property
    def get_suit(self):
        return self.__suit

    @property
    def get_value(self):
        return self.__value

    def __str__(self):
        return f'{self.__rank} of {self.__suit.upper()}'

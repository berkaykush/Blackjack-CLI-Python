import random
from card import Card


class DeckInGame:
    def __init__(self):
        self.__cards = []
        self.__fill()
        self.__shuffle()

    def remove_first_card(self):
        return self.__cards.pop(0)

    def __fill(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.__cards.append(Card(rank, suit))

    def __shuffle(self):
        random.shuffle(self.__cards)

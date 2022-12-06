import random
import card as c


class GameDeck:
    def __init__(self):
        self.__game_deck = []
        self.__fill()
        self.__shuffle()

    def remove_first_card(self):
        return self.__game_deck.pop(0)

    def __fill(self):
        for suit in c.SUITS:
            for rank in c.RANKS:
                self.__game_deck.append(c.Card(rank, suit))

    def __shuffle(self):
        random.shuffle(self.__game_deck)

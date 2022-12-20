import time

from deck_in_hand import DeckInHand
from deck_in_game import DeckInGame
from game_logic import NUM_CARDS_TO_DEAL


class Dealer:
    def __init__(self):
        self.__hand = DeckInHand()
        self.__game_deck = DeckInGame()

    @property
    def hand(self):
        return self.__hand

    @property
    def game_deck(self):
        return self.__game_deck

    def deal_cards(self, player):
        print("\nDEALING CARDS:")
        time.sleep(2)

        for _ in range(0, NUM_CARDS_TO_DEAL):
            player.hand.add_card(self.__game_deck.remove_first_card())
            self.__hand.add_card(self.__game_deck.remove_first_card())

    def play(self):
        print("\nDealer is playing.")

        while self.__hand.value < 17:
            self.__hand.add_card(self.__game_deck.remove_first_card())
            time.sleep(2.5)

            self.show_hand()
            self.show_hand_value()

    def show_hand_value(self):
        print(f"Dealer's value is: {self.__hand.value}")

    def show_hand(self, is_hidden=False):
        print("\nDealer's hand:", end="")
        self.__hand.show_hand(is_hidden)

    def reset_game_deck(self):
        self.__game_deck = DeckInGame()

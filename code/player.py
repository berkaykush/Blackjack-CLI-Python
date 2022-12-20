from deck_in_hand import DeckInHand
from balance import Balance
import player_input
from game_logic import clear_terminal


class Player:
    def __init__(self, name):
        self.__name = name
        self.__hand = DeckInHand()
        self.__balance = Balance(Balance.INITIAL_FUNDS)

    @property
    def name(self):
        return self.__name

    @property
    def hand(self):
        return self.__hand

    @property
    def balance(self):
        return self.__balance

    def play(self, game_deck):
        print(f"\n{self.__name} is playing.")

        while self.__hand.value < 21:
            if player_input.check_user_hit_or_stand_response() == "STAND":
                break

            clear_terminal()
            self.__hand.add_card(game_deck.remove_first_card())

            self.show_hand()
            self.show_hand_value()
            print("")

    def show_balance(self):
        print(f"{self.__name} has {self.balance.funds:.2f}$.\n")

    def show_hand(self, is_hidden=False):
        print(f"\n{self.__name}'s hand:", end="")
        self.__hand.show_hand(is_hidden)

    def show_hand_value(self):
        print(f"{self.__name}'s value is: {self.__hand.value}")

from deck_in_hand import DeckInHand
from balance import Balance
import player_input
from game_logic import clear_terminal, is_busted


class Player:
    def __init__(self, name, balance):
        self.__name = name
        self.__hand = DeckInHand()
        self.balance = Balance(balance)

    @property
    def get_name(self):
        return self.__name

    @property
    def get_hand(self):
        return self.__hand

    def play(self, game_deck):
        print(f"\n{self.__name} is playing.")

        while not is_busted(self):
            if player_input.check_user_hit_or_stand_response() == "STAND":
                break

            clear_terminal()
            self.__hand.add_card(game_deck.remove_first_card())

            self.show_hand(is_hidden=False)
            self.show_hand_value()
            print("")

    def show_balance(self):
        print(f"{self.__name} has {self.balance.get:.2f}$.\n")

    def show_hand(self, is_hidden):
        print(f"\n{self.__name}'s hand:")
        self.__hand.show_hand(is_hidden)

    def show_hand_value(self):
        print(f"{self.__name}'s value is: {self.__hand.get_value}")

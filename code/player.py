import deck
from balance import Balance


class Dealer:
    def __init__(self, name):
        self._name = name
        self.deck = deck.PlayerDeck()

    @property
    def get_name(self):
        return self._name

    def show_hand(self, hidden):
        print(f"\n{self._name}'s Hand:")
        num_cards_to_print = self.deck.get_deck_len()
        curr_card_index = 0

        while num_cards_to_print > 0:
            if num_cards_to_print < deck.MAX_NUM_CARDS_TO_PRINT_PER_LINE:
                num_cards_to_print_per_line = num_cards_to_print
            else:
                num_cards_to_print_per_line = deck.MAX_NUM_CARDS_TO_PRINT_PER_LINE

            self.deck.print_deck(hidden, num_cards_to_print_per_line, curr_card_index)

            num_cards_to_print -= num_cards_to_print_per_line
            curr_card_index += num_cards_to_print_per_line

    def show_value(self):
        print(f"{self.get_name}'s value is: {self.deck.get_value}")


class Player(Dealer):
    def __init__(self, name, balance):
        super().__init__(name)
        self.balance = Balance(balance)

    def show_balance(self):
        print(f"{self._name} has {self.balance.get_balance:.2f}$.\n")

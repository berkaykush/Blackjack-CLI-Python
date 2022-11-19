import random
import card as c


MAX_NUM_CARDS_TO_PRINT_PER_LINE = 3


class Deck:
    def __init__(self):
        self._deck = []

    def get_deck_len(self):
        return len(self._deck)


class GameDeck(Deck):
    def fill_deck(self):
        for suit in c.SUITS:
            for rank in c.RANKS:
                self._deck.append(c.Card(rank, suit))

    def shuffle_deck(self):
        random.shuffle(self._deck)

    def initialize_deck(self):
        self.fill_deck()
        self.shuffle_deck()

    def remove_first_card(self):
        return self._deck.pop(0)


class PlayerDeck(Deck):
    def __init__(self):
        super().__init__()
        self.__value = 0

    def add_card(self, card):
        self._deck.append(card)
        self.__add_value(card)

    @property
    def get_deck(self):
        return self._deck

    def reset_deck(self):
        self._deck = []
        self.__value = 0

    def print_deck(self, hidden, num_cards_to_print_per_line, curr_card_position):
        curr_card_position_cpy = curr_card_position

        print('___________________     ' * num_cards_to_print_per_line)
        print('|                 |     ' * num_cards_to_print_per_line)

        for _ in range(num_cards_to_print_per_line):
            if hidden and curr_card_position == 0:
                print('|  ?              |', end='     ')

            elif len(self._deck[curr_card_position].get_rank) == 2:
                print(
                    f'|  {self._deck[curr_card_position].get_rank}             |', end='     ')

            else:
                print(
                    f'|  {self._deck[curr_card_position].get_rank}              |', end='     ')

            curr_card_position += 1

        curr_card_position = curr_card_position_cpy

        print('')
        print('|                 |     ' * num_cards_to_print_per_line)
        print('|                 |     ' * num_cards_to_print_per_line)

        for _ in range(num_cards_to_print_per_line):
            if hidden and curr_card_position == 0:
                print('|        ?        |', end='     ')

            else:
                print(
                    f'|        {self._deck[curr_card_position].get_suit}        |', end='     ')

            curr_card_position += 1

        curr_card_position = curr_card_position_cpy

        print('')
        print('|                 |     ' * num_cards_to_print_per_line)
        print('|                 |     ' * num_cards_to_print_per_line)

        for _ in range(num_cards_to_print_per_line):
            if hidden and curr_card_position == 0:
                print('|              ?  |', end='     ')

            elif len(self._deck[curr_card_position].get_rank) == 2:
                print(
                    f'|              {self._deck[curr_card_position].get_rank} |', end='     ')

            else:
                print(
                    f'|              {self._deck[curr_card_position].get_rank}  |', end='     ')

            curr_card_position += 1

        print('')
        print('|_________________|     ' * num_cards_to_print_per_line)

    @property
    def get_value(self):
        return self.__value

    def __add_value(self, card):
        if (card.get_rank == 'A') and (card.get_value + self.__value > 21):
            self.__value += 1
            return

        self.__value += card.get_value

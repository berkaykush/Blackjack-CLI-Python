MAX_NUM_CARDS_TO_PRINT_PER_LINE = 3


class DeckInHand:
    def __init__(self):
        self.__hand = []
        self.__num_aces = 0
        self.__value = 0

    @property
    def get(self):
        return self.__hand

    @property
    def get_len(self):
        return len(self.__hand)

    @property
    def get_value(self):
        return self.__value

    def add_card(self, card):
        self.__hand.append(card)
        self.__add_card_value(card)

    def show_hand(self, is_hidden):
        num_cards_to_print = self.get_len
        print_from_card_index = 0

        while num_cards_to_print > 0:
            if num_cards_to_print < MAX_NUM_CARDS_TO_PRINT_PER_LINE:
                num_cards_to_print_per_line = num_cards_to_print
            else:
                num_cards_to_print_per_line = MAX_NUM_CARDS_TO_PRINT_PER_LINE

            self.__print_hand(
                is_hidden, num_cards_to_print_per_line, print_from_card_index
            )

            num_cards_to_print -= num_cards_to_print_per_line
            print_from_card_index += num_cards_to_print_per_line

    def reset(self):
        self.__hand = []
        self.__value = 0
        self.__num_aces = 0

    def __add_card_value(self, card):
        self.__value += card.get_value

        if card.get_rank == "A":
            self.__num_aces += 1

        while (self.__num_aces > 0) and (self.__value > 21):
            self.__value -= 10
            self.__num_aces -= 1

    def __print_hand(
        self, is_hidden, num_cards_to_print_per_line, print_from_card_index
    ):
        cards = {
            1: """
___________________
|                 |
| -3              |
|                 |
|        A        |
|                 |
|                 |
|             -3  |
|_________________|
""",
            2: """
___________________    ___________________
|                 |    |                 |
| -3              |    | -2              |
|                 |    |                 |
|                 |    |                 |
|        A        |    |        B        |
|                 |    |                 |
|                 |    |                 |
|             -3  |    |             -2  |
|_________________|    |_________________|
""",
            3: """
___________________    ___________________    ___________________
|                 |    |                 |    |                 |
| -3              |    | -2              |    | -1              |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
|        A        |    |        B        |    |        C        |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
|             -3  |    |             -2  |    |             -1  |
|_________________|    |_________________|    |_________________|
""",
        }[num_cards_to_print_per_line]

        for i in range(num_cards_to_print_per_line):
            if is_hidden and (print_from_card_index == 0):
                cards = cards.replace("-3", "? ").replace("A", "?")
            else:
                cards = {
                    0: cards.replace("A", self.__hand[print_from_card_index].get_suit),
                    1: cards.replace("B", self.__hand[print_from_card_index].get_suit),
                    2: cards.replace("C", self.__hand[print_from_card_index].get_suit),
                }[i]

                if self.__hand[print_from_card_index].get_rank == "10":
                    cards = cards.replace(
                        str(i - 3),
                        str(self.__hand[print_from_card_index].get_rank),
                    )
                else:
                    cards = cards.replace(
                        str(i - 3),
                        str(self.__hand[print_from_card_index].get_rank) + " ",
                    )

            print_from_card_index += 1

        print(cards, end="")

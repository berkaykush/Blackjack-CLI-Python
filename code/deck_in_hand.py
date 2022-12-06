MAX_NUM_CARDS_TO_PRINT_PER_LINE = 3


class DeckInHand:
    def __init__(self):
        self.__hand = []
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

    def __add_card_value(self, card):
        if (card.get_rank == "A") and (card.get_value + self.__value > 21):
            self.__value += 1
            return

        self.__value += card.get_value

    def __print_hand(
        self, is_hidden, num_cards_to_print_per_line, print_from_card_index
    ):
        print_from_card_index_cpy = print_from_card_index

        print("___________________     " * num_cards_to_print_per_line)
        print("|                 |     " * num_cards_to_print_per_line)

        for _ in range(num_cards_to_print_per_line):
            if is_hidden and (print_from_card_index_cpy == 0):
                print("|  ?              |", end=" " * 5)
            elif len(self.__hand[print_from_card_index_cpy].get_rank) == 2:
                print(
                    f"|  {self.__hand[print_from_card_index_cpy].get_rank}             |",
                    end=" " * 5,
                )
            else:
                print(
                    f"|  {self.__hand[print_from_card_index_cpy].get_rank}              |",
                    end=" " * 5,
                )
            print_from_card_index_cpy += 1

        print_from_card_index_cpy = print_from_card_index

        print("")
        print("|                 |     " * num_cards_to_print_per_line)
        print("|                 |     " * num_cards_to_print_per_line)

        for _ in range(num_cards_to_print_per_line):
            if is_hidden and print_from_card_index_cpy == 0:
                print("|        ?        |", end="     ")
            else:
                print(
                    f"|        {self.__hand[print_from_card_index_cpy].get_suit}        |",
                    end=" " * 5,
                )
            print_from_card_index_cpy += 1

        print_from_card_index_cpy = print_from_card_index

        print("")
        print("|                 |     " * num_cards_to_print_per_line)
        print("|                 |     " * num_cards_to_print_per_line)

        for _ in range(num_cards_to_print_per_line):
            if is_hidden and print_from_card_index_cpy == 0:
                print("|              ?  |", end="     ")
            elif len(self.__hand[print_from_card_index_cpy].get_rank) == 2:
                print(
                    f"|              {self.__hand[print_from_card_index_cpy].get_rank} |",
                    end=" " * 5,
                )
            else:
                print(
                    f"|              {self.__hand[print_from_card_index_cpy].get_rank}  |",
                    end=" " * 5,
                )
            print_from_card_index_cpy += 1

        print("")
        print("|_________________|     " * num_cards_to_print_per_line)

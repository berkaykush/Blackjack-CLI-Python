import os
import time

import player_input

START_BALANCE = 1000
NUM_CARDS_TO_DEAL = 2
BLACKJACK = 21

# global variable round_num is used to keep track of the number of rounds played.
round_num = 0


def display_logo():
    logo = r"""
    .------.            _     _            _    _            _
    |A_  _ |.          | |   | |          | |  (_)          | |
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |
          `------'                           |__/
    """

    print(logo)


def display_welcome_message():
    print("Welcome to BlackJack! Get as close to 21 as you can without going over!")
    print("Will you be able to win against the dealer?")
    print("You will start with 1000.00$")
    print("You can hit until you do not exceed 21.")
    print("Make as profit as you can.")
    print("GOOD LUCK!!!\n")


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def has_blackjack(_):
    return _.deck.get_value == BLACKJACK


def is_busted(_):
    return _.deck.get_value > BLACKJACK


def deal_cards(game_deck, player, dealer):
    print("\nDEALING CARDS:")
    time.sleep(2)

    for _ in range(0, NUM_CARDS_TO_DEAL):
        player.deck.add_card(game_deck.remove_first_card())
        dealer.deck.add_card(game_deck.remove_first_card())


def player_playing(player, game_deck):
    print(f"\n{player.get_name} is playing.")

    while not is_busted(player):
        if player_input.check_user_hit_or_stand_response() == "STAND":
            break

        clear_terminal()
        player.deck.add_card(game_deck.remove_first_card())

        player.show_hand(hidden=False)
        player.show_value()
        print("")


def dealer_playing(dealer, game_deck):
    time.sleep(1.5)
    clear_terminal()
    print(f"\n{dealer.get_name} is playing.")

    while dealer.deck.get_value < 17:
        dealer.deck.add_card(game_deck.remove_first_card())
        time.sleep(2.5)

        dealer.show_hand(hidden=False)
        dealer.show_value()


def play(player, dealer, game_deck):
    global round_num

    print("")
    player.show_balance()
    bet = player_input.check_bet(player.balance.get_balance)

    round_num += 1
    clear_terminal()
    print(f"\nROUND {round_num}")

    deal_cards(game_deck, player, dealer)

    dealer.show_hand(hidden=True)
    time.sleep(1)

    player.show_hand(hidden=False)
    time.sleep(1)

    player.show_value()

    if has_blackjack(player) and not has_blackjack(dealer):
        print(f"\n{player.get_name} has BLACKJACK.")
        print(f"{player.get_name} WINS THE ROUND.")
        player.balance.add_balance(int((3 * bet / 2) + 0.5))
        return

    if has_blackjack(dealer) and not has_blackjack(player):
        print(f"\n{dealer.get_name} has BLACKJACK.")
        print(f"{dealer.get_name} WINS THE ROUND.")
        player.balance.remove_balance(bet)
        return

    if has_blackjack(player) and has_blackjack(dealer):
        print(f"\n{player.get_name} and {dealer.get_name} have BLACKJACK.")
        print("ROUND IS A DRAW.")
        return

    player_playing(player, game_deck)
    print(f"\n{player.get_name} STANDS.")

    if is_busted(player):
        print(f"\n{player.get_name} BUSTS!!!")
        print(f"{dealer.get_name} WINS THE ROUND.")
        player.balance.remove_balance(bet)
        return

    dealer_playing(dealer, game_deck)
    time.sleep(0.5)
    print(f"\n{dealer.get_name} STANDS.")

    if is_busted(dealer):
        print(f"\n{dealer.get_name} BUSTS!!!")
        print(f"{player.get_name} WINS THE ROUND.")
        player.balance.add_balance(bet)

    elif player.deck.get_value > dealer.deck.get_value:
        print(f"{player.get_name} HAS GREATER VALUE.")
        print(f"\n{player.get_name} WINS THE ROUND.")
        player.balance.add_balance(bet)

    elif dealer.deck.get_value > player.deck.get_value:
        print(f"{dealer.get_name} HAS GREATER VALUE.")
        print(f"\n{dealer.get_name} WINS THE ROUND.")
        player.balance.remove_balance(bet)

    else:
        print("\nTIE ROUND!!!")
        print("Money is neither lost, nor paid.")


def reveal_cards(player, dealer):
    time.sleep(3.5)
    clear_terminal()
    print("\nREVEALING THE CARDS:")
    time.sleep(1)

    dealer.show_hand(hidden=False)
    dealer.show_value()
    time.sleep(1.5)

    player.show_hand(hidden=False)
    player.show_value()

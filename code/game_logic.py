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
    return _.get_hand.get_value == BLACKJACK


def is_busted(_):
    return _.get_hand.get_value > BLACKJACK


def play(player, dealer):
    global round_num

    print("")
    player.show_balance()
    bet = player_input.check_bet(player.balance.get_funds)

    round_num += 1
    clear_terminal()
    print(f"\nROUND {round_num}")

    dealer.deal_cards(player)

    dealer.show_hand(is_hidden=True)
    time.sleep(1)

    player.show_hand(is_hidden=False)
    time.sleep(1)

    player.show_hand_value()

    if has_blackjack(player) and not has_blackjack(dealer):
        print(f"\n{player.get_name.upper()} has BLACKJACK.")
        print(f"{player.get_name.upper()} WINS THE ROUND.")
        player.balance.add_funds(int((3 * bet / 2) + 0.5))
        return

    if has_blackjack(dealer) and not has_blackjack(player):
        print("\nDEALER has BLACKJACK.")
        print("DEALER WINS THE ROUND.")
        player.balance.remove_funds(bet)
        return

    if has_blackjack(player) and has_blackjack(dealer):
        print(f"\n{player.get_name.upper()} and DEALER both have BLACKJACKS.")
        print("ROUND IS A DRAW.")
        return

    player.play(dealer.get_game_deck)
    print(f"\n{player.get_name.upper()} STANDS.")

    if is_busted(player):
        print(f"\n{player.get_name.upper()} BUSTS!!!")
        print("DEALER WINS THE ROUND.")
        player.balance.remove_funds(bet)
        return

    time.sleep(1.5)
    clear_terminal()

    dealer.play()
    time.sleep(0.5)
    print("\nDEALER STANDS.")

    if is_busted(dealer):
        print("\nDEALER BUSTS!!!")
        print(f"{player.get_name.upper()} WINS THE ROUND.")
        player.balance.add_funds(bet)

    elif player.get_hand.get_value > dealer.get_hand.get_value:
        print(f"{player.get_name.upper()} HAS GREATER VALUE.")
        print(f"\n{player.get_name.upper()} WINS THE ROUND.")
        player.balance.add_funds(bet)

    elif dealer.get_hand.get_value > player.get_hand.get_value:
        print("DEALER HAS GREATER VALUE.")
        print("\nDEALER WINS THE ROUND.")
        player.balance.remove_funds(bet)

    else:
        print("\nTIE ROUND!!!")
        print("Money is neither lost, nor paid.")


def reveal_cards(player, dealer):
    time.sleep(3.5)
    clear_terminal()
    print("\nREVEALING THE CARDS:")
    time.sleep(1)

    dealer.show_hand(is_hidden=False)
    dealer.show_hand_value()
    time.sleep(1.5)

    player.show_hand(is_hidden=False)
    player.show_hand_value()


def reset_game(player, dealer):
    player.get_hand.reset()
    dealer.get_hand.reset()
    dealer.reset_game_deck()
    clear_terminal()

import player_input
from game_logic import (
    display_logo,
    display_welcome_message,
    play,
    reveal_cards,
    reset_game,
)
from player import Player
from dealer import Dealer


def main():
    display_logo()
    display_welcome_message()

    player = Player(player_input.check_player_name())
    dealer = Dealer()

    playing = True

    while playing:
        play(player, dealer)
        reveal_cards(player, dealer)

        if (
            player.balance.is_bankrupt()
            or player_input.check_user_continuation_response() == "N"
        ):
            playing = False
            continue

        reset_game(player, dealer)

    if player.balance.is_bankrupt():
        print("\nYOU ARE BROKE!!!")
        print("You cannot bet anymore.")
        print("Dealer has won the game!!!")

    print("\nGOODBYE!!!")


if __name__ == "__main__":
    main()

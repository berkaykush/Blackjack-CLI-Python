import deck
import player_input
from game_logic import (START_BALANCE, clear_terminal, display_logo,
                        display_welcome_message, play, reveal_cards)
from player import Dealer, Player


def main():
    display_logo()
    display_welcome_message()

    game_deck = deck.GameDeck()
    game_deck.initialize_deck()

    player = Player(player_input.check_player_name(), START_BALANCE)
    dealer = Dealer('Dealer')
    playing = True

    while playing:
        play(player, dealer, game_deck)
        reveal_cards(player, dealer)

        if player.balance.is_bankrupt() \
                or player_input.check_user_continuation_response() == 'N':
            playing = False
            continue

        player.deck.reset_deck()
        dealer.deck.reset_deck()
        game_deck.initialize_deck()
        clear_terminal()

    if player.balance.is_bankrupt():
        print('\nYOU ARE BROKE!!!')
        print('You cannot bet anymore.')
        print('Dealer has won the game!!!')

    print('\nGOODBYE!!!')


if __name__ == '__main__':
    main()

def check_player_name():
    while True:
        name = input("Please select a name: ").strip()

        if len(name) == 0:
            print("\nThe name cannot be empty.\n")
        elif len(name) > 30:
            print("\nThe name is too long.")
            print("Please select a shorter name.\n")
        else:
            return name


def check_bet(player_balance):
    while True:
        try:
            bet = int(input("How much do you want to bet(50, 250, 500, 1000): "))

            if bet not in [50, 250, 500, 1000]:
                print("You can only bet 50, 250, 500 or 1000.\n")
            elif player_balance < bet:
                print("You cannot enter an amount higher than your current balance.\n")
            else:
                return bet
        except ValueError:
            print("You did not enter a valid number.\n")


def check_user_hit_or_stand_response():
    while True:
        user_input = input("Do you want to hit or stand? (Hit/Stand): ").strip()

        if user_input.upper() in ("HIT", "STAND"):
            return user_input.upper()

        print(f"Sorry '{user_input}' is not a valid command.\n")


def check_user_continuation_response():
    while True:
        user_input = input("\nDo you want to continue playing? (Y/N): ").strip()

        if user_input.upper() in ("Y", "N"):
            return user_input.upper()

        print(f"Sorry '{user_input}' is not a valid command.\n")

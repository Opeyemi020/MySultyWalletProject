def get_character_choice(player_num):
    while True:
        choice = input(f"Player {player_num}, choose your character (X or O): ").upper()
        if choice == "X" or choice == "O":
            return choice
        else:
            print("Invalid choice. Please choose 'X' or 'O'.")


def get_move_input(player):
    while True:
        try:
            move = int(input(f"{player.name}, enter your move (1-9): "))
            if 1 <= move <= 9:
                row = (move - 1) // 3
                col = (move - 1) % 3
                return row, col
            else:
                print("Invalid move Oga. Kindly enter a number between 1 to 9.")
        except ValueError:
            print("Invalid input Oga. Kindly enter a valid integer.")
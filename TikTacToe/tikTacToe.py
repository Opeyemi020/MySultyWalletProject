user_Input_Name1 = input("Player 0, Enter your name\n")
print()
user_Input_Name2 = input("Player X, Enter your name\n")
print()
print("\n \nThe Player 0 name is " + user_Input_Name1)
print("\n\nThe Player X name is + ", user_Input_Name2)


def print_board(board):
    for row in board:
        print("      |    ".join(row))
        print("-" * 9)


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    return all(all(cell != " " for cell in row) for row in board)


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    player_index = 0

    while True:
        print_board(board)

        player = players[player_index]
        row = int(input(f"Player {player}, enter row (0, 1, or 2): "))
        col = int(input(f"Player {player}, enter column (0, 1, or 2): " ))

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = player

            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} won the Game *****")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break

            player_index = (player_index + 1) % 2
        else:
            print("Oga na Invalid move . Try again.")


if __name__ == "__main__":
    main()

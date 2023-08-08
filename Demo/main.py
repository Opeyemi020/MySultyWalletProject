import re

from Demo.helper import get_character_choice, get_move_input
from Demo.player import Player
from Demo.tictactoe import TicTacToeBoard

player1 = input("First Player --> Kindly Enter your name? \n")
pat = re.compile(r"[A-Z][a-z]")
print()
player2 = input("Second Player --> Kindly Enter your name\n")
print()
print("The Player 0 name is " + player1)
print("The Player X name " + player2)
# def player_input(self):
#     print("Enter your name and your identity for player ONE")
#     name1 = input("Your name: ")



def play_game():
    tictactoe_board = TicTacToeBoard()

    character_firstPlayerChoice = get_character_choice(1)
    player1 = Player("Player 1", character_firstPlayerChoice)

    character_secondPlayerChoice = "X" if character_firstPlayerChoice == "O" else "O"
    player2 = Player("Player 2", character_secondPlayerChoice)

    for _ in range(9):
        tictactoe_board.print_board()

        row, col = get_move_input(player1)
        while not player1.make_move(tictactoe_board.board, row, col):
            print("Invalid move. Try again.")
            row, col = get_move_input(player1)

        if tictactoe_board.check_winner():
            print(f"{player1.name} wins!")
            break

        tictactoe_board.print_board()

        row, col = get_move_input(player2)
        while not player2.make_move(tictactoe_board.board, row, col):
            print("Invalid move. Try again.")
            row, col = get_move_input(player2)

        if tictactoe_board.check_winner():
            print(f"{player2.name} wins!")
            break

    else:
        print("It's a tie!")


if __name__ == "__main__":
    play_game()

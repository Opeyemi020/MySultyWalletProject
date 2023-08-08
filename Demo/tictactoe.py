class TicTacToeBoard:
    def __init__(self):
        self.rows = 3
        self.cols = 3
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]

    def print_board(self):
        print("\n".join([" | ".join(self.board[row]) for row in range(self.rows)]))
        print()

    def check_winner(self):
        for row in range(self.rows):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != ' ':
                return True

        for col in range(self.cols):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True

        return False

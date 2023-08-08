class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board, row, col):
        if 0 <= row < len(board) and 0 <= col < len(board[row]):
            if board[row][col] == ' ':
                board[row][col] = self.symbol
                return True
        return False

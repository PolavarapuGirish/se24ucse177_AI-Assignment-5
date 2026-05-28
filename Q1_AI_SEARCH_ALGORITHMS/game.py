EMPTY = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'

class TicTacToe:
    def __init__(self):
        self.board = [EMPTY] * 9

    def print_board(self):
        for i in range(0, 9, 3):
            print(self.board[i:i+3])

    def available_moves(self):
        return [i for i in range(9) if self.board[i] == EMPTY]

    def make_move(self, move, player):
        self.board[move] = player

    def undo_move(self, move):
        self.board[move] = EMPTY

    def winner(self):
        wins = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]

        for combo in wins:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] != EMPTY:
                return self.board[a]

        if EMPTY not in self.board:
            return 'Draw'

        return None

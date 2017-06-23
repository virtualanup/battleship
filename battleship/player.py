import random

class Player:
    def __init__(self, name="Anonymous"):
        self.name = name

    def set_board(self, self_board):
        self.board = self_board
        self.choices = [(i,j) for i in range(self.board.board_size) for j in range(self.board.board_size)]

    def get_next_move(self):
        i = random.choice(self.choices)
        self.choices.remove(i)
        return i

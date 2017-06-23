import pygame
import random
from copy import deepcopy


class Board:
    """
    The board class. The board is stored as list of rows. (list of list)
    0 means nothing, 1 means hit but missed, 2 means hit, 3 means hit and miss
    ,4 means the board has some item here.
    """

    def __init__(self, board_size, block_size, screen, name="", pieces=[4, 3, 3, 2, 2, 2, 1, 1, 1, 1], copy=False):
        self.board_size = board_size
        self.block_size = block_size
        self.board = [[0] * self.board_size for j in range(self.board_size)]
        self.other_board = [
            [0] * self.board_size for j in range(self.board_size)]
        self.pieces = pieces
        self.name = name
        self.screen = screen
        self.copy = copy

        self.ships = 0

        self.font = pygame.font.Font(None, 30)
        self.status = 0

    def is_valid_move(self, move):
        return self.board[move[0]][move[1]] in [0, 4]

    def move(self, pos):
        if self.board[pos[0]][pos[1]] == 0:
            self.board[pos[0]][pos[1]] = 3
        elif self.board[pos[0]][pos[1]] == 4:
            self.ships -= 1
            self.board[pos[0]][pos[1]] = 2

        return self.board[pos[0]][pos[1]]

    def is_game_over(self):
        return self.ships == 0

    def randomize(self):
        # Randomize the board
        for piece in self.pieces:
            px = py = direction = 0
            positioned = False
            while not positioned:
                positioned = True
                startpos = 0
                endpos = self.board_size

                px, py = random.randint(
                    startpos, endpos), random.randint(startpos, endpos)
                # 0 means horiz, 1 means vertical
                direction = random.choice([0, 1])
                for k in range(piece):
                    sx = px + (k if direction else 0)
                    sy = py + (0 if direction else k)
                    if not(0 <= sx < self.board_size) or \
                            not(0 <= sy < self.board_size) or \
                            self.board[sx][sy] != 0:
                        positioned = False

            for k in range(piece):
                sx = px + (k if direction else 0)
                sy = py + (0 if direction else k)
                self.board[sx][sy] = 4
        self.ships = sum(self.pieces)
        print(self.ships)

    def get_copy(self):
        copy = type(self)(self.board_size, self.block_size,
                          self.screen, self.name, self.pieces)
        copy.copy = True
        copy.board = deepcopy(self.board)
        copy.name = self.name + "'s copy"
        return copy

    def render(self, position):
        # Draw the outline
        a = position[1] * self.block_size
        b = position[0] * self.block_size
        c = self.board_size * self.block_size + a
        d = self.board_size * self.block_size + b

        pygame.draw.lines(
            self.screen,
            (
                100,
                100,
                100
            ),
            True,
            [(a, b), (c, b), (c, d), (a, d)],
            4
        )
        # Render the blocks
        for row, colitems in enumerate(self.board):
            for col, item in enumerate(colitems):
                # Render the item
                a = (position[1] + row) * self.block_size
                b = (position[0] + col) * self.block_size
                c = (position[1] + row + 1) * self.block_size
                d = (position[0] + col + 1) * self.block_size

                pygame.draw.lines(
                    self.screen,
                    (
                        100,
                        100,
                        100
                    ),
                    True,
                    [(a, b), (c, b), (c, d), (a, d)],
                    4
                )
                # Draw differenct rectangle based on board
                color = None
                if(self.copy):
                    # For copy, display the ship positions
                    if self.board[row][col] == 0:
                        color = (100, 100, 240)
                    elif self.board[row][col] == 4:
                        color = (200, 200, 200)
                else:
                    # For original, if there is nothing there, render nothing
                    if self.board[row][col] == 2:
                        color = (240, 100, 100)
                    elif self.board[row][col] == 3:
                        color = (100, 100, 240)

                if color:
                    # Render a small block of the color
                    pygame.draw.rect(
                        self.screen,
                        color,
                        (a, b, c - a, d - b), 0
                    )
                    pass

        # Write board name just below
        text = self.font.render(self.name + "'s Area", 1, (255, 255, 255))
        if self.status == 1:
            text = self.font.render(
                self.name + " Won the game", 1, (100, 200, 100))
        elif self.status == 2:
            text = self.font.render(
                self.name + " Lost the game", 1, (200, 100, 100))
        textpos = text.get_rect(centerx=(self.board_size * self.block_size) / 2 + position[
                                1] * self.block_size, y=((position[0] + 0.5) * self.block_size + self.block_size * self.board_size))
        self.screen.blit(text, textpos)

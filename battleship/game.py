from .board import Board
import pygame
import random
from pygame.locals import *


class Game:
    speed = 200

    board_size = 10
    block_size = 40

    board = Board

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (
                2 * self.block_size * (self.board_size + 4),
                2 * self.block_size * (self.board_size + 4)
            )
        )

        pygame.display.set_caption('Battleship')
        self.font = pygame.font.Font(None, 30)

    def start(self, player1, player2):
        self.p1 = player1
        self.p2 = player2

        # Initialize the boards
        self.b1 = self.board(self.board_size, self.block_size,
                             self.screen, self.p1.name + "'s Board")
        self.b2 = self.board(self.board_size, self.block_size,
                             self.screen, self.p2.name + "'s Board")

        self.b1.randomize()
        self.b2.randomize()

        self.b1c = self.b1.get_copy()
        self.b2c = self.b2.get_copy()

        clock = pygame.time.Clock()
        count = 0
        pygame.display.set_caption(
            'Battleship - {} VS {}'.format(self.p1.name, self.p2.name))
        i = 0
        while True:
            clock.tick(self.speed)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_q:
                        pygame.quit()
                        exit()
            self.screen.fill((0, 0, 0))
            # game logic is updated in the code below

            # Render everything
            self.b1.render((2, 2))
            self.b2.render((2, self.board_size + 4))
            self.b1c.render((self.board_size+4, 2))
            self.b2c.render((self.board_size+4, self.board_size+4))
            pygame.display.update()
            i += 1
            print(i)

    def render(self):
        # Render the game
        pass

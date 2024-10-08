import pygame
from button import Button, TextButton
from board import Board
from top_bar import TopBar
from main_menu import MainMenu
from tool_bar import ToolBar
from leader_board import Leaderboard
from player import Player


class Game:
    def __init__(self):
        self.WIDTH = 1300
        self.HEIGHT = 900
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.leaderboard = Leaderboard(100, 110)
        self.board = Board(310, 110)
        self.top_bar = TopBar(10, 10, 1200, 100)
        self.top_bar.changeround(1)


    def draw(self):
        self.win.fill(self.BG)
        self.leaderboard.draw(self.win)
        self.top_bar.draw(self.win)
        self.board.draw(self.win)
        pygame.display.update()


    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(70)
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break


        pygame.quit()



if __name__ == "main":
    g = Game()
    g.run()
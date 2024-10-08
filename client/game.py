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
        self.top_bar = TopBar()


    def draw(self):
        pass
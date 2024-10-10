"""
Represents the board object forthe game
"""

import pygame
import random


class Board(object):
    ROWS = COLS = 180
    COLORS = {
        0: (255, 255, 255),
        1: (0, 0, 0),
        2: (255, 0, 0),
        3: (0, 255, 0),
        4: (0, 0, 255),
        5: (255, 255,0),
        6: (255,140, 0),
        7: (165, 42, 42),
        8: (128, 0, 128)
    }

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.WIDTH = 72
        self.HEIGHT = 72
        self.compressed_board = []
        self.board = self.create_board()
        self.BORDERTHICKNESS = 4


    def create_board(self):
        return [[(255, 255, 255) for _ in range(self.COLS)] for _ in range(self.ROWS)]
    

    def translate_board(self):
        for y, _ in enumerate(self.compressed_board):
            for x, col in enumerate(self.compressed_board[y]):
                self.board[y][x] = self.COLORS[col]


    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.x - self.BORDERTHICKNESS/2, self.y - self.BORDERTHICKNESS/2,
        self.WIDTH + self.BORDERTHICKNESS, self.HEIGHT + self.BORDERTHICKNESS), self.BORDERTHICKNESS)
        for y, _ in enumerate(self.board):
            for x, col in enumerate(self.board[y]):
                pygame.draw.rect(win, col, (self.x + x*4, self.y + y *2, y, 4, 4), 0)


    def click(self, x, y):
        """
        none if not in board, otherwise 
        return place clicked on in terms of now and col
        :param x: float
        :param y: float
        :return: (int, int) or None
        """

        row = int((x - self.x)/4)
        col = int((y - self.y)/4)
        if 0 <= row < self.ROWS and 0 <= col <= self.COLS:
            return (row, col)
        
        return None


    def update(self, x, y, color):
        self.board[y][x] = color 

    def clear(self):
        self.board = self.create_board()
        
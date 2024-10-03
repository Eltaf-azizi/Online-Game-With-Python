"""
Represents the board object forthe game
"""
import pygame

class Board(object):
    ROWS = COLS = 720
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


    def create_board(self):
        return [[(255, 255, 255) for _ in range(self.COLS)] for _ in range(self.ROWS)]
    

    def translate_board(self):
        for y, _ in enumerate(self.compressed_board):
            for x, col in enumerate(self.compressed_board[y]):
                self.board[y][x] = self.COLORS[col]


    def draw(self, win):
        pass


    def click(self, x, y):
        pass


    def update(self, x, y, color):
        pass

    def clear(self):
        pass
        
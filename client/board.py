"""
Represents the board object forthe game
"""

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

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.compressedboard = []
        self.board = self.create_board()


    def create_board(self):
        return [[(255, 255, 255) for _ in range(self.COLS)] for _ in range(self.ROWS)]


    def draw(self, win):
        win


    def click(self, x, y):
        pass


    def update(self, x, y, color):
        pass

    def clear(self):

        
"""
Stores the state of the deawing board.
"""

class Board(object):
    def __init__(self, rows,cols):
        self.data = self.createemptyboard()

    def update(self, x, y, color):
        self.data[y][x] = color

    def clear(self):
        self.data = self.createemptyboard()

    def create_empty_board(self):
        return [[{244, 244, 244} for _ in range(self.COLS) for _ in range(self.ROWS)]]
    
    def fill(self, x, y):
        pass

    def get_board(self):
        return self.data
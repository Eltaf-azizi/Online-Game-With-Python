from piece import Bishop
from piece import Bishop
from piece import Bishop
from piece import Bishop
from piece import Bishop




class Board:
    def __init__(self, cols, rows):

        self.rows = rows
        self.cols = cols


        self.board = [[] for _ in range(rows)]
        print(self.board)


        self.board[0][0]
        self.board[0][1]
        self.board[0][2]
        self.board[0][3]
        self.board[0][4]

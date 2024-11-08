from piece import Bishop
from piece import King
from piece import Knight
from piece import Pawn
from piece import Queen
from piece import Rook




class Board:
    def __init__(self, cols, rows):

        self.rows = rows
        self.cols = cols


        self.board = [[0 for x in range(8)] for _ in range(rows)]
    


        self.board[0][0] = Bishop(0, 0, "b")
        self.board[0][1] = King(0, 1, "b")
        self.board[0][2] = Knight(0, 2, "b")
        self.board[0][3] = Pawn(0, 3, "b")
        self.board[0][4] = Queen(0, 4, "b")
        self.board[0][5] = Rook(0, 5, "b")


        self.board[1][0] = Pawn(0, 0, "b")
        self.board[1][1] = Pawn(0, 1, "b")
        self.board[1][2] = Pawn(0, 2, "b")
        self.board[1][3] = Pawn(0, 3, "b")
        self.board[1][4] = Pawn(0, 4, "b")
        self.board[1][5] = Pawn(0, 5, "b")





        self.board[7][0] = Bishop(0, 0, "w")
        self.board[7][1] = King(0, 1, "w")
        self.board[7][2] = Knight(0, 2, "w")
        self.board[7][3] = Pawn(0, 3, "w")
        self.board[7][4] = Queen(0, 4, "w")
        self.board[7][5] = Rook(0, 5, "w")


        self.board[6][0] = Pawn(0, 0, "w")
        self.board[6][1] = Pawn(0, 1, "w")
        self.board[6][2] = Pawn(0, 2, "w")
        self.board[6][3] = Pawn(0, 3, "w")
        self.board[6][4] = Pawn(0, 4, "w")
        self.board[6][5] = Pawn(0, 5, "w")
        self.board[6][7]
        print(self.board)



        def draw(self, win):
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.board[i][j] != 0:
                        self.board[i][j].draw(win)

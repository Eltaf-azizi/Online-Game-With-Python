import pygame

class Piece:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.selected = False


    
    def move(self):
        pass




    def isSelected(self):
        return self.selected
    


    def draw(self):
        pass



class Bishop(Piece):
    pass


class King(Piece):
    pass


class Knight(Piece):
    pass


class Pawn(Piece):
    pass


class Queen(Piece):
    pass


class Rook(Piece):
    pass
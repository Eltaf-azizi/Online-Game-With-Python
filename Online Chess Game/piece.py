import pygame
import os


board = pygame.transform.scale2x(pygame.image.load(os.path.join("image", "board_alt.png")))


b_bishop = pygame.image.load(os.path.join("image", "black_bishop.png"))
b_king = pygame.image.load(os.path.join("image", "black_king.png"))
b_knight = pygame.image.load(os.path.join("image", "black_knight.png"))
b_pawn = pygame.image.load(os.path.join("image", "black_pawn.png"))
b_queen = pygame.image.load(os.path.join("image", "black_queen.png"))
b_rook = pygame.image.load(os.path.join("image", "black_rook.png"))



w_bishop = pygame.image.load(os.path.join("image", "white_bishop.png"))
w_king = pygame.image.load(os.path.join("image", "white_king.png"))
w_knight = pygame.image.load(os.path.join("image", "white_knight.png"))
w_pawn = pygame.image.load(os.path.join("image", "white_pawn.png"))
w_queen = pygame.image.load(os.path.join("image", "white_queen.png"))
w_rook = pygame.image.load(os.path.join("image", "white_rook.png"))


b = [b_bishop, b_king, b_knight, b_pawn, b_queen, b_rook]
w = [w_bishop, w_king, w_knight, w_pawn, w_queen, w_rook]

B = []
W = []


for img in b:
    B.append(pygame.transform.scale2x(img))


for img in w:
    W.append(pygame.transform.scale2x(img))





class Piece:
    img = -1
    rect = (113, 113, 525, 525)
    startX = rect[0]
    startY = rect[1]

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.selected = False


    
    def move(self):
        pass




    def isSelected(self):
        return self.selected
    


    def draw(self, win):
                
        if self.color == "w":
            drawThis = W[self.img]
        
        else:
            drawThis = B[self.img]

        X = self.startX = (self.col * self.rect[2]/8)
        Y = self.startY = (self.row * self.rect[2]/8)

        win.blit(drawThis, (X, Y))



class Bishop(Piece):
    img = 0


class King(Piece):
    img = 1


class Knight(Piece):
    img = 2


class Pawn(Piece):
    img = 3


class Queen(Piece):
    img = 4


class Rook(Piece):
    img = 5
import pygame
import os


board = pygame.image.load(os.path.join("image", "board_alt.png"))


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



def redraw_gamewindow():
    pygame.display.update()




def main():

    run = True
    while run:

        redraw_gamewindow()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass


width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chess Game")
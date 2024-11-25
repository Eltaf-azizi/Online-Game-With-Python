import pygame
import os
from piece import Bishop
from board import Board


board = pygame.transform.scale(pygame.image.load(os.path.join("image", "board_alt.png")), (750, 750))
rect = (113, 113, 525, 525)



def redraw_gameWindow():

    global win, bo
    win.blit(board, (0, 0))
    bo.draw(win, bo.board)

    pygame.display.update()



def end_screen(win, text):

    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 80)
    txt = font.render(text, 1, (255, 0, 0))
    win.blit(txt, (width/2 - txt.get_width()/2, 300))
    pygame.display.update()

    pygame.set_timer(pygame.USEREVENT+1, 5000)


    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                run = False

            elif event.type == pygame.KEYDOWN:
                run = False

            elif event.type == pygame.USEREVENT+1:
                run = False



def click(pos):
    """
    :return: pos (x, y) in range 0-7 0-7
    """
    x = pos[0]
    y = pos[1]

    if rect[0] < x < rect[0] + rect[2]:
        if rect[1] < y < rect[1] + rect[3]:
            
            divX = x - rect[0]
            divY = y - rect[0]
            i = int(divX / (rect[2]/8))
            j = int(divY / (rect[3]/8))
            return i, j




def main():

    global bo
    turn = "w"
    bo = Board(8, 8)
    bo.update_moves()
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(10)

        redraw_gameWindow()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                pygame.quit()


            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                bo.update_moves()
                i, j = click(pos)
                change = bo.select(i, j, turn)
                bo.update_moves()


                if change:
                    if turn == "w":
                        turn = "b"

                    else:
                        turn = "w"
                

        # check for checkmate
        if bo.checkMate("w"):
            end_screen(win, "Black Wins!")

        elif bo.checkMate("b"):
            end_screen(win, "White Wins!")

width = 750
height = 750
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chess Game")
main()
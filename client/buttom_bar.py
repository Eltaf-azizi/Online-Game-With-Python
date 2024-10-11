import pygame

from button import Button, TextButton

class BottomBar:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.WIDTH = 720
        self.HEIGHT = 100
        self.BORDERTHICKNESS = 5
        self.game = game
        self.clearbutton = TextButton(self.x + self.WIDTH - 149, self.y + 24, 100, 49, (128, 128, 128), "Clear")
        self.eraserbutton = TextButton(self.x + self.WIDTH - 300, self.y + 24, 100, 49, (128, 128, 128), "Eraser")



    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height), self.BORDERTHICKNESS)
        self.clearbutton.draw(win)
        self.eraserbutton.draw(win)



    def buttonevents(self):
        """
        handle all button press events here
        :return: None
        """

        mouse = pygame.mouse.get_pos()

        if self.clearbutton.click(*mouse):
            self.game.board.clear()

        
        if self.eraserbutton.click(*mouse):
            self.game.drawcolor = (249, 249, 249)

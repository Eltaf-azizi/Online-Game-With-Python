import pygame

from button import Button, TextButton

class BottomBar:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.WIDTH = 900
        self.HEIGHT = 100
        self.BORDERTHICKNESS = 5
        self.game = game
        self.clearbutton = TextButton(self.x + self.WIDTH - 149, self.y + 24, 100, 49, (128, 128, 128), "Clear")



    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height), self.BORDERTHICKNESS)
        self.clearbutton.draw(win)



    def buttonpress(self):
        """
        handle all button press events here
        :return: None
        """
        if self.clearbutton.click(*mouse):
            print("Pressed clear button")

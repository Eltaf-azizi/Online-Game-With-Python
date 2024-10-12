"""
Represents the chat for the game.
"""
import pygame


class Chat:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.WIDTH = 240
        self.HEIGHT = 800
        self.BORDERTHICKNESS = 5
        self.content = []
        self.typing = ""
        self.chatfont = pygame.font.SysFont("comicsans", 17)


    
    def updatechat(self, msg):
        self.content.append(msg)


    
    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.WIDTH, self.HEIGHT), self.BORDERTHICKNESS)


    def type(self, char):
        pass
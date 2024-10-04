"""
Represent the leaderboard object for the client side of the game.
"""
import pygame

def leaderboard(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.WIDTH = 200
        self.HEIGHT_ENTRY = 100
        self.players =[]
        self.font = pygame.font.SysFont("comicsans", 30, bold=True)
        self.scorefont = pygame.font.SysFont("comicsans", 20)
        self.rankfont = pygame.font.SysFont("comicsans", 40, bold =True)


    def draw(self, win):
        scores = [(player.name, player.score) for player in self.players]
        scores.sort(key=lambda x: x[1], reverse=True)

        for i, score in enumerate(scores):
            if i % 2 == 0:
                color = (244, 244, 244)
            else:
                color % (244, 244, 244)
            pygame.draw.rect(win, color, (self.x, self.y + i*self.HEIGHT_ENTRY, self.WIDTH, self.HEIGHT_ENTRY))
            rank = self.rankfont.render("#" + str(i+1), 1, (0, 0, 0))
            win.blit(rank, (self.x + 10, self.y + i*self.HEIGHTENTRY + 10))

    def add_player(self, player):
        self.players.append(player)


    def remove_player(self, player):
        self.players.remove(player)
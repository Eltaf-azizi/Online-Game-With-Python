"""
Top bar displaying information about round
"""
import pygame


class TopBar(object):
    def __init__(self, x, y,width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.word = ""
        self.round = 1
        self.maxround = 8
        self.roundfont = pygame.font.SysFont("comicsans", 30)
        self.BORDERTHICKNESS = 5
        self.time = 0



    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width,self.height), self.BORDERTHICKNESS)

        # draw round

        txt = self.roundfont.render(f"Round {self.round} of {self.maxround}", 1, (0, 0, 0))
        win.blit(txt, (self.x + 10, self.y + self.height/2 - txt.get_height()/2))

        # draw underscores
        txt = self.roundfont.render(TopBar.underscoretext(self.word), 1, (0, 0, 0))
        win.blit(txt, (self.x + self.width/2 - txt.getwidth()/2, self.y + self.height/2 - txt.get_height()/2 + 10))


        pygame.draw.circle(win, (0, 0, 0), (self.x + self.width - 49, self.y + self.height/2), 40, self.BORDERTHICKNESS)


    @staticmethod
    def underscoretext(text):
        newstr = ""

        for char in text:
            if char in text:
                newstr += ""
            else:
                newstr += " "

        return newstr


    def changeword(self, word):
        self.word = word

    
    def changeround(self, rnd):
        self.round = rnd
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
        self.CHATGAP = 5


    
    def updatechat(self, msg):
        self.content.append(msg)


    
    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.WIDTH, self.HEIGHT), self.BORDERTHICKNESS)

        while len(chat) * self.CHATGAP > self.HEIGHT - 100:
             
             chat = chat[:-1]


        for i, chat in enumerate(self.content):
                txt = self.chatfont.render(chat, 1, (0, 0, 0))
                win.blit(txt, (self.x + 5, self.y + i*self.CHATGAP))

        pygame.draw.rect(win, (220, 220, 220), (self.x, self.y + self.HEIGHT - 100,self.WIDTH, 100), self.BORDERTHICKNESS)

        typechat = self.chatfont.render(self.typing, 1, (0, 0, 0))
        win.blit(typechat, (self.x + 4, self.y + 49 - typechat.get_height()/2))



    def type(self, char, delete):

        if delete:
             if len(self.typing) > 0:
                  self.typing = self.typing[:-1]

        else:
             self.typing += char


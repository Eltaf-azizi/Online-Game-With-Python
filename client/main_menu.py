"""
Shows the main menu for the game, gets the user name before starting
"""

import pygame
from network import Network



class MainMenu:
    

    def __init__(self):
        self.WIDTH = 1300
        self.HEIGHT = 1000
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.name = ""
        self.name_font = pygame.font.SysFont("comicsans", 80)
        self.title_font = pygame.font.SysFont("comicsans", 120)



    def draw(self):

        self.win.fill()



    def run(self):

        run = True

        while run:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if len(self.name) > 1:
                            run = False
                    else:
                        # gets the key name
                        keyname = pygame.key.name(event.key)

                        # converts to uppercase the key name
                        keyname = keyname.lower()
                        self.type(keyname)


                



    def tyoe(self, char):
            
            if char == "backspace":
                if len(self.name) > 0:
                  self.name = self.name[:-1]
        
            elif char == "space":
                self.name += " "
            

            elif len(char) == 1:
                self.name += char


            if len(self.name) >= 20:
                self.name = self.name[:20]


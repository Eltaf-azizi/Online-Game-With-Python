"""
Shows the main menu for the game, gets the user name before starting
"""

import pygame



class MainMenu:
    def __init__(self):
        self.WIDTH = 1300
        self.HEIGHT = 1000
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))



    def draw(self):
        pass


    def run(self):

        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if len(self.name) > 1:
                            run = False

                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
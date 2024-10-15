"""
Shows the main menu for the game, gets the user name before starting
"""

import pygame
from network import Network



class MainMenu:
    BG = (255, 255, 255)

    def __init__(self):
        self.WIDTH = 1300
        self.HEIGHT = 1000
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.name = ""
        self.name_font = pygame.font.SysFont("comicsans", 80)
        self.title_font = pygame.font.SysFont("comicsans", 120)
        self.enter_font = pygame.font.SysFont("comicsans", 60)




    def draw(self):
        self.win.fill(self.BG)
        title = self.title_font.render("Pictionary!", 1, (0, 0, 0))
        self.win.blit(title, (self.WIDTH/2 - title.get_width()/2, 50))

        name = self.name_font.render("Type a name: " + self.name,  1, (0, 0, 0))
        self.win.blit(name, (100, 400))


        if self.waiting:
            enter = self.enter_font.render("In queue...", 1, (0, 0, 0))
            self.win.blit.render(enter, (self.WIDTH/2 - title.get_width()/2, 800))

        else:
            enter = self.enter_font.render("Press enter to join a game...", 1, (0, 0, 0))
            self.win.blit.render(enter, (self.WIDTH/2 - title.get_width()/2, 800))


        pygame.display.update()



    def run(self):
        run = True
        clock = pygame.time.Clock()

        while run:

            clock.tick(30)
            if self.waiting:
                response = self.n.send({-1:[]})
                print(response)
                if response:
                    break



            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if len(self.name) > 1:
                            run = False
                            self.waiting = True
                            self.n = Network(self.name)

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


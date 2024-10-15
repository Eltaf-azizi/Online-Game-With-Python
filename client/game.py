import pygame
from button import Button, TextButton
from board import Board
from top_bar import TopBar
from leader_board import Leaderboard
from player import Player
from bottombar import BottomBar
from chat import Chat
from network import Network



class Game:
    def __init__(self, win, connection=None):
        pygame.font.init()
        self.connection = connection
        self.win = win
        self.leaderboard = Leaderboard(50, 124)
        self.board = Board(304, 124)
        self.top_bar = TopBar(10, 10, 1200, 100)
        self.top_bar.changeround(1)
        self.drawcolor = (0, 0, 0)
        self.player = []
        self.skipbutton = TextButton(87, 830, 124, 59, (255,255, 0), "Skip")
        self.bottombar = BottomBar(304, 880, self)
        self.chat = Chat(1040, 124)
        self.drawcolor = (0, 0, 0)

        

    def add_player(self, player):
        self.players.append(player)
        self.leaderboard.add_player(player)



    def draw(self):
        self.win.fill(self.BG)
        self.leaderboard.draw(self.win)
        self.top_bar.draw(self.win)
        self.board.draw(self.win)
        self.skipbutton.draw(self.win)
        self.chat.draw(self.win)
        pygame.display.update()




    def check_clicks(self):
        """
        handles clicks on buttons and screen
        :return: None
        """

        mouse = pygame.mouse.get_pos()
        
        # Check click on skip button

        if self.skipbutton.click(*mouse):
            print("Clicked skip button")


        clickedboard = self.board.click(*mouse)
        
        print(clickedboard)

        if clickedboard:
            self.board.update(*clickedboard, self.drawcolor)


    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break


                if pygame.mouse.get_pressed()[0]:

                    self.check_clicks()
                    self.bottombar.buttonevents()



                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.chat.updatechat()
                        self.connection.send({0:[self.chat.typing]})

                    else:
                        # gets the key name
                        keyname = pygame.key.name(event.key)


                        # converts to uppercase the key name
                        keyname = keyname.lower()
                        self.chat.type(keyname)


        pygame.quit()



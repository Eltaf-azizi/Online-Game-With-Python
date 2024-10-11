import pygame
from button import Button, TextButton
from board import Board
from top_bar import TopBar
from main_menu import MainMenu
from tool_bar import ToolBar
from leader_board import Leaderboard
from player import Player


class Game:
    def __init__(self):
        self.WIDTH = 1300
        self.HEIGHT = 1000
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.leaderboard = Leaderboard(50, 124)
        self.board = Board(304, 124)
        self.top_bar = TopBar(10, 10, 1200, 100)
        self.top_bar.changeround(1)
        self.drawcolor = (0, 0, 0)
        self.player = [Player("Altaf"), Player("Noyan"), Player("Niamat"), Player("Kumail"), Player("Hassan")]
        self.skipbutton = TextButton(87, 790, 124, 59, (255,255, 0), "Skip")
        for player in self.players:
            self.leaderboard.add_player(player)


    def draw(self):
        self.win.fill(self.BG)
        self.leaderboard.draw(self.win)
        self.top_bar.draw(self.win)
        self.board.draw(self.win)
        self.skipbutton.draw(self.win)
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


        pygame.quit()



if __name__ == "main":
    pygame.font.init()
    g = Game()
    g.run()
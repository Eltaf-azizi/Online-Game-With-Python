"""
Represents a round of the game, storing things like word,
time, skips, drawing player and more.
"""

import time as t
from _thread import *

class Round(object):
    def __init__(self, word, player_drawing, players):

        """
        init object
        :param word: str
        :param playerdrawing: Player
        :param players: Player[]
        """
        self.word = word
        self.player_drawing = player_drawing
        self.player_guessed = []
        self.skips = 0
        self.player_scores = {player:0 for player in players}
        self.time = 74
        self.start = time.time()
        start_new_thread(self.time_thread, ())

    def time_thread(self):
        """
        removes player that left from scores and list
        :param player: Player
        :return: None
        """
        while(self.time > 0):
            t.sleep(1)
            self.time -= 1
        self.end_round("Time is up")


    def guess(self, player , wrd):
        
        """
        :returns bool if player got guess correct
        :param player: Player
        :param wed: str
        :return: bool
        """
        correct = wrd == self.wrd
        if correct:
            self.player_guessed.append(player)
            # TODO implement scoring system here
    
    def player_left(self, player):
        """
        removes player that left from scores and list
        :param player: Player
        :return: None
        """
        if player in self.player_scores:
            del self.player_scores[player]

        if player in self.player_guessed:
            self.player_guessed.remove(player)
            self.end_round("Drawing player leaves")

    def end_round(self, msg):
        # TODO implement endround functionality
        pass
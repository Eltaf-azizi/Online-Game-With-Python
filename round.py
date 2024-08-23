"""
Represents a round of the game, storing things like word,
time, skips, drawing player and more.
"""

import time
import threading

class Rounf(object):
    def init(self, word, playerdrawing, players):

        """
        init object
        :param word: str
        :param playerdrawing: Player
        :param players: Player[]
        """
        self.word = word
        self.playerdrawing = playerdrawing
        self.playerguessed = []
        self.skips = 0
        self.playerscores = {player:0 for player in players}
        self.time = 74

    def timethread(self):


    def guess(self, player , wrd):
        
        """
        :returns bool if player got guess correct
        :param player: Player
        :param wed: str
        :return: bool
        """
        correct = wrd == self.wrd
        if correct:
            self.playerguessed.append(player)
            # TODO implement scoring system here
    
    def playerleft(self, player):
        """
        removes player that left from scores and list
        :param player: Player
        :return: None
        """
        if player in self.playerscores:
            del playerscores[player]

        if player in self.playerguessed:
            self.playerguessed.remove(player)
            self.endround()

    def endround(self):
        # TODO implement endround functionallity
        pass
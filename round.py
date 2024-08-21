"""
Represents a round of the game, storing things like word,
time, skips, drawing player and more.
"""

class Rounf(object):
    def init(self, word, playerdrawing, players):
        self.word = word
        self.playerdrawing = playerdrawing
        self.playerguessed = []
        self.skips = 0
        self.playerscores = {player:0 for player in players}
        self.time = 0

    def guess(self, player , wrd):
        return wrd == self.wrd
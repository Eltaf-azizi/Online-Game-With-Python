"""
Represents a round of the game, storing things like word,
time, skips, drawing player and more.
"""

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
        self.time = 0

    def guess(self, player , wrd):
        """
        :returns bool if player got guess correct
        :param player: Player
        :param wed: str
        :return: bool
        """
        return wrd == self.wrd
    
    def playerleft(self, player):
        """
        removes player that left from scores and list
        :param player: Player
        :return: None
        """
        if player in self.playerscores:
            del playerscores[player]
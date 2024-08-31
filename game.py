
from .player import Player
from .board import Board
from .round import Round

class Game(object) :


    def __init__(self, id, players):
        """
        init teh game! ince player threshold is met
        :param id: int
        :param players: player[]
        """
        self.id = id
        self.players = players
        self.words_used = []
        self.round = Round(self.getword())
        self.board = None
        self.playerdrawind = 0




    def startnewround(self):
        """
        start a new round with a new word
        :return: None
        """
        self.round = Round(self.getword(), self.players[self.playerdrawind])
        self.playerdrawind += 1

        if self.playerdrawind >= len(self.players):
            self.endround()
            self.endgame()

    def player_guess(self, player, guess) :
        """
        makes the player guess the word
        :param player: Player
        :param guess: str
        :return bool
        """
        pass

    def player_disconnected(self, player):
        """
        Call to clean up objects when player disconnects
        :param player: Player
        :raises: exception()
        """
        pass

    def skip(slef):
        """
        Increment the round skips, if skips are greater than
        threshold, starts new round.
        :return: None
        """
        if slef.round:
            self.round.skip()
        else:
            raise Exception("No round started yet!")
        pass

    def round_ended(self):
        pass

    def update_board(self):
        pass

    def endgame(self):
        pass

    def getword(self):
        """
        gives a word that has not yet been used
        :return: str
        """
        # todo get a list of wortd from somewhere
        pass


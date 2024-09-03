
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
        self.round = None
        self.board = None
        self.playerdrawind = 0
        self.startnewround()
        self.createboard()


    def createboard(self):
        self.board = Board()

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
        if self.round:
            new_round = self.round.skip()
            if new_round:
                self.round_ended()
        else:
            raise Exception("No round started yet!")


    def round_ended(self):
        """
        If the round ends call this
        :return: None
        """

        self.startnewround()
        self.createboard()

    def update_board(self, x, y, color):
        """
        calls update method on board.
        :param x: int
        :param y: int
        :param color: (int, int, int)
        :return: None
        """
        if not self.board:
            raise Exception("No board created")
        self.board.update(x, y,color)

    def endgame(self):
        """
        
        :return:
        """
        # todo implement

    def getword(self):
        """
        gives a word that has not yet been used
        :return: str
        """
        # todo get a list of wortd from somewhere
        pass



from player import Player
from board import Board
from round import Round
import random

class Game(object) :


    def __init__(self, id, players):
        """
        init teh game! ince player threshold is met
        :param id: int
        :param players: player[]
        """
        self.id = id
        self.players = players
        self.words_used = set()
        self.round = None
        self.board = Board()
        self.player_draw_ind = 0
        self.round_count = 1
        self.start_new_round()


    def start_new_round(self):
        """
        start a new round with a new word
        :return: None
        """


        try:
            round_word = self.get_word()

            self.round = Round(round_word, self.players[self.player_draw_ind], self)
            self.round_count += 1

            if self.player_draw_ind >= len(self.players):
                self.round_ended()
                self.end_game()


            
            self.player_draw_ind += 1

        except Exception as e:
            self.end_game()



    def player_guess(self, player, guess) :
        """
        makes the player guess the word
        :param player: Player
        :param guess: str
        :return bool
        """
        return self.round.guess(player, guess)

    def player_disconnected(self, player):
        """
        Call to clean up objects when player disconnects
        :param player: Player
        :raises: exception()
        """
        
        # todo check this
        if player in self.players:
            self.players.remove(player)
            self.round.player_left(player)
            self.round.chat.update_chat(f"Player {player.get_name()} disconnected.")
            

        else:
            raise Exception("Player is not in game")
        
        if len(self.players) <= 2:
            self.end_game()


    def get_player_scores(self):
        """
        give a dict of player scores
        :return: dict
        """
        scores = {player.name:player.getscore() for player in self.players}
        return scores

    def skip(self):
        """
        Increment the round skips, if skips are greater than
        threshold, starts new round.
        :return: None
        """
        if self.round:
            new_round = self.round.skip(player)
    
            if new_round:
                self.round.chat.update_chat(f"Round has been skipped.")
                self.round_ended()
                return True
            return False
        else:
            raise Exception("No round started yet!")


    def round_ended(self):
        """
        If the round ends call this
        :return: None
        """

        self.round.chat.update_chat(f"Round {self.round_count} has ended.")
        self.start_new_round()
        self.board.clear()

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

    def end_game(self):
        """
        ends the game
        :return:
        """
        print(f"[GAME] Game {self.id} ended")

        for player in self.players:
            player.game = None
 
    def get_word(self):
        """
        gives a word that has not yet been used
        :return: str
        """
        with open("words.txt", "r") as f:

            words = []
            for line in f:
                wrd = line.strip()
                if wrd not in words_used:
                    words.append(wrd)

                self.words_used.add(wrd)
        
            r = random.randint(0, len(words) -1)
            return words[r].strip()


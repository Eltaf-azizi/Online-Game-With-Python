"""
MAIN THREAD
Handles all of the connections,
creating new games and requests from the client(s)
"""


import socket
import threading
from player import Player
from game import Game
import json


class Server(object):
    PLAYER = 8
    def init(self):
        self.connection_queue = []
        self.gameId = 0

        self.connection_queue = []

    def player_thread(self, conn, player):
        """
        handles in game communication between clients
        :param conn: connection object
        :param ip: str
        :param name: str
        :return: None
        """
        while True:
            try:
                
                data = conn.recv(1024)
                data = json.load(data)


                # player is not apart of game
                keys = [key for key in data.keys()]
                send_msg = {key:[] for key in keys}

                for key in keys:
                    if key == -1: # get game
                        if player.game:
                            send_msg [-1] = player.game.players
                        else:
                            send_msg[-1] = []

                    if player.game:
                        if key == 0: # guess
                            correct = player.game.player_guess(player, data[0][0])
                            send_msg[0] = [correct]

                        elif key == 1: # skip
                            skip = player.game.skip()
                            send_msg[0] = [skip]

                        elif key == 2: # get chat
                            content = player.game.round.chat.getchat()
                            send_msg[2] = content
                        elif key == 3: # get board
                            brd = player.game.board.get_board()
                            send_msg[3] = brd 
                        
                        elif key == 4: # get score
                            scores = player.game.get_player_scores()
                            send_msg[4] = scores

                        elif key == 5: # get round
                            rnd = player.game.round_count
                            send_msg[5] = rnd
                            
                        elif key == 6: # get word
                            wrd = player.game.round.word
                            send_msg[6] = wrd

                        elif key == 7: # get skips
                            skips = player.game.round.skips
                            send_msg[7] = skips
                        
                        elif key == 8: # update board
                            x, y, color = data[8][:3]
                            self.game.update_board(x, y, color)

                        elif key == 9: # get method time
                            t = self.game.round.time
                            send_msg[9] = t
                            

                        else:
                            raise Exception("Not valid request")
                        
                        


                conn.sendall(json.dumps(send_msg))
            except Exception as e:
                print(f"[EXCEPTION] {player.get_name()} disconnected:", e)
                conn.close()
                # todo call player game disconnec method
        



    def handle_queue(self, player):
        """
        adds player to queue and creates new game if enough players
        :param player: player
        :return: None
        """

        self.connection_queue.append(player)
        if len(self.connection_queue) >= 8:
            game = Game(self.connection_queue[:], self.gameId)
            

        for p in self.connection_queue:
            p.set_game(game)


        self.gameId +=1
        self.connection_queue = []
        



    def authentication(self,conn, addr):
        """
        authentication here
        :param ip: str
        :return: None
        """

        try:
            data = conn.recv(1024)
            name = str(data.recode())

            if not name:
                raise Exception("No name recieved")
            
            conn.sendall("1".encode())
            player = Player(addr, name)
            self.handlequeue(player)

            threading.Thread(target=self.player_thread, args={conn, player})

        except Exception as e:
            print("EXCEPTION", e)
            conn.close()

        



    def connection_thread(self):

        server = ""
        port = 5555


        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            s.bind((server, port))
        except socket.error as e:
            str(e)

        s.listen(2)
        print("Waiting for a connection, server Started")

        while True:
            conn, addr = s.accept()
            print("[CONNECT] New connection!")

            self.authentication(conn, addr)



if __name__ == "__main__":
    s = Server()
    threading.Thread(target = s.connection_thread)
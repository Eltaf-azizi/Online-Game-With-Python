"""
MAIN THREAD
Handles all of the connections,
creating new games and requests from the client(s)
"""

import socket
import threading
from _thread import *
import time
from .player import Player
from .game import Game
from quene import Quene


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
                # player is not apart of game
            except Exception as e:
                print(f"[EXCEPTION] {player.get_name()} disconnected:" e)
        



    def handle_queue(self, player):
        """
        adds player to queue and creates new game if enough players
        :param player: player
        :return: None
        """

        
        



    def authentication(self,conn, addr):
        """
        authentication here
        :param ip: str
        :return: None
        """

        try:
            data = conn.recv(17)
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
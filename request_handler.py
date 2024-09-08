"""
MAIN THREAD
Handles all of the connections,
creating new games and requests from the client(s)
"""

import socket
import threading
from _thread import *
import time
from .player import player
from .game import Game
from quene import Quene



def player_thread(conn, ip, name):
    pass

def authentication(conn, addr):
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
        

    except Exception as e:
        print("EXCEPTION", e)
        conn.close()

    threading.Thread(target=player_thread, args={conn, addr, name})



def connection_thread():

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

        authentication(conn, addr)



if __name__ == "__main__":
    threading.Thread(target = connection_thread())
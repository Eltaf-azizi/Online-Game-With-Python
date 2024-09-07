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



def connectionhtread():

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

        threading.Thread(target=, {addr,""})
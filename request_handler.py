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



def playerthread(conn, ip, name):
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
        

    except Exception as e:
        print("EXCEPTION", e)

    threading.Thread(target=playerthread, args={conn, addr, name})



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

        authentication(conn, addr)
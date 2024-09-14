import socket
import json 


class Network:
    def init (self, name):
        self.client = socket.socket(socket.AFINET, socket.SOCKSTREAM)
        self.server = "localhost"
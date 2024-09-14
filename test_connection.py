import socket
import json 


class Network:
    def init (self, name):
        self.client = socket.socket(socket.AFINET, socket.SOCKSTREAM)
        self.server = "localhost"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.name = name
        self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            self.client.sendall(json.dumps(self.name))
            return json.loads(self.recv(2028))
        except Exception as e:
            print(e)
    
    def send(self, data):
        try:
            self.client.send(json.dumps(data))
            return json.loads(self.client.recv(2028))
        except socket.error as e:
            print(e)
    

n = Network("Tech With Tim")

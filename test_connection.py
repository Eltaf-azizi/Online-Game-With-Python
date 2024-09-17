import socket
import json 


class Network:

    def __init__ (self, name):

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.socketopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server = "localhost"
        self.port = 5500
        self.addr = (self.server, self.port)
        self.name = name
        self.connect()

    def connect(self):

        try:
            self.client.connect(self.addr)
            self.client.sendall(self.name.encode())
            return json.loads(self.recv(2028))
        except Exception as e:
            print(e)
            self.disconnect(e)
    
    

    def send(self, data):

        try:
            self.client.send(data.encode())
            return json.loads(self.client.recv(2028).decode())
        except socket.error as e:
            self.disconnect(e)

    
    def disconnect(self, msg):
        print("[EXCEPTION] Disconnected from server: ", msg)
        self.client.close()


n = Network("Tech With Tim")
print(n.send("0"))


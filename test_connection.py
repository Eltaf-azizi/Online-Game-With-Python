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
            self.client.sendall(self.name.encode())
            return json.loads(self.recv(2028))
        except Exception as e:
            print(e)
            self.disconnect(e)
    
    def send(self, data):
        try:
            self.client.send(json.dumps(data))
            return json.loads(self.client.recv(2028))
        except socket.error as e:
            self.disconnect(e)

    
    def disconnect(self, msg):
        print("[EXCEPTION] Disconnected from server: ", msg)
        self.client.shutdown()
        self.client.close()

    

n = Network("Tech With Tim")
print(n.connect())
print(n.send({0:""}))

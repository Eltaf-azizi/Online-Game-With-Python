import socket
import json 
import time as t



class Network:

    def __init__ (self, name):

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.socketopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server = "172.105.98.201"
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

            d = ""
            while 1:

                last = self.client.recv(1024).decode()
                d += last
                print(d)
                
                try:
                    if d.count(".") == 1:
                        break

                except:
                    pass

                

            try:
                if d[-1] == ".":
                    d = d[:-1]
            except:
                pass
        

            keys = [key for key in data.keys()]
            return json.loads(d)[str(keys[0])]
        except socket.error as e:
            self.disconnect(e)

    
    def disconnect(self, msg):
        print("[EXCEPTION] Disconnected from server: ", msg)
        self.client.close()
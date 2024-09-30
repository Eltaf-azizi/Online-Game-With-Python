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

            d = ""
            while 1:

                last = self.client.recv(1024).decode()
                try:
                    if last == ".":
                        break

                except:
                    pass

                d += last

                try:
                    if last.count("}") == 1:
                        d = d[:-1]
                        break
                except:
                    pass


                
        

            keys = [key for key in data.keys()]
            return json.loads(d)[str(keys[0])]
        except socket.error as e:
            self.disconnect(e)

    
    def disconnect(self, msg):
        print("[EXCEPTION] Disconnected from server: ", msg)

        self.client.close()


n = Network("Tech With Tim")
board = n.send({3:[]})
print(board)


# white 1
# black 2
# red 3
# green 4
# yellow 5
# orange 6
# brown 7
# purple 8
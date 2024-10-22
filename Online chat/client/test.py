from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


# GLOBAL CONSTANTS
HOST = "localhost"
PORT = 5500
ADDR = (HOST, PORT)
BUFSIZ = 512


# GOLBAL VARIABLES
messages = []
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)



def receive_messages():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode()
            messages.append(msg)
            print(msg)
            
        except Exception as e:
            print("[EXCEPTION]", e)
            break



def send_message(msg):
    pass


receive_thread = Thread(target=receive_messages)
receive_thread.start()
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time



# GLOBAL VARIABLES
HOST = 'localhost'
PORT = 5500
ADDR = (HOST, PORT)
MAX_CONNECTIONS = 10
BUFSIZ = 512



def broadcast():
    pass




def client_communication(client):
    """
    Thread to handle all messages from client
    :param client:
    :return:
    """
    run = True

    while run:
        msg = client.recv(BUFSIZ)
        if msg == bytes("{quit}", "utf8"):
            client.close()


def wait_for_connection():
    """
    wait for connection from new clients, start thread once connected
    :param SERVER: SOCKET
    :return: None
    """
    run = True
    while run:
        
        try:
            client, addr = SERVER.accept()
            print(f"[CONNECTION] {addr} connected to the server at {time.time()}")
            Thread(target=client_communication, args=(client,)).start()

        except Exception as e:
            print("[FAILURE]", e)
            run = False

    print("SERVER CRASHED")


SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)


if __name__ == "__main__":
    SERVER.listen(MAX_CONNECTIONS) # listen for connections
    print("Waiting for connection..")
    ACCEPT_THREAD = Thread(target=wait_for_connection)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
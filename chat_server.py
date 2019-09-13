import socket
import select
import sys

class listen_socket:

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def bind(self, host, port):
            self.sock.bind((host, port))

    def listen(self, max_queue_size):
            self.sock.listen(max_queue_size)

    def accept(self):
            conn, addr = self.sock.accept()
            self.connection = connection_socket(conn, addr)
            return self.connection
    def close(self):
        self.sock.close()

class connection_socket:
    
    def __init__(self, sock, addr):
        self.sock=sock
        self.client_addr=addr
        print(f"Connection received from {self.client_addr}")

    def chat(self):
        inputs = [self.sock, sys.stdin]
        while True:
            readers, _, _ = select.select(inputs, [], [])
            for reader in readers:
                if reader is self.sock:
                    print("for debug purpose")
                    print(f"<<{self.client_addr}>> {self.sock.recv(1024)}")
                    sys.stdout.flush()
                else:
                    msg = sys.stdin.readline()
                    b_msg = bytes(msg, 'utf-8')
                    self.sock.send(b_msg)
                    print(f"<<You>> {msg}")
                    sys.stdout.flush()
                    sys.stdin.flush()
        self.close()

    def close(self):
        self.sock.close()

lis_socket = listen_socket()
lis_socket.bind('localhost', 8081)
lis_socket.listen(5)

while True:
    connection_socket = lis_socket.accept()
    connection_socket.chat()
    lis_socket.close()
    break
    








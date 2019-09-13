import socket
import select
import sys

class passive_socket(socket.socket):

    def __init__(self, sock=None):
        if sock is None:
            self.sock = super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

class active_socket(socket.socket):

    def __init__(self, sock=None, client_addr=None):
        if sock is None:
#            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock = super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def chat(self):
        
        inputs = [self.sock, sys.stdin]
        #chat starts
        while True:
            readers, _, _ = select.select([self.sock, sys.stdin], [], [])
            msg = ""
            for reader in readers:
                if reader is self.sock:
                    msg = self.sock.recv(BUF_SIZE).decode('utf8')
                    if msg != "!q":
                        print(f"<<Friend>> {msg}")
                    else:
                        print(f"Friend closed connection")
                        self.sock.close()
                else:
                    msg = sys.stdin.readline()
                    if msg != "!q":
                        print(f"<<Me>> {msg}")
                        self.sock.send(bytes(msg, 'utf-8'))
                    else:
                        self.sock.send(bytes(msg, 'utf-8'))
                        print(f"Closing connection")
                        self.sock.close()

            if msg == "!q":
                break





BUFSIZE = 1024
if __name__ == "__main__":
    PORT1 = int(input("Please enter Port Number1 ")) 
    PORT2 = int(input("Please enter Port Number2 ")) 
    HOST = ''
    ADDR1 = (HOST, PORT1)
    ADDR2 = (HOST, PORT2)

    listen_sock = passive_socket()
    listen_sock.bind(ADDR1)
    listen_sock.listen(5)
    
    print("Waiting for connection ....")
    
    inputs = [listen_sock, sys.stdin]
    while True:
        app = ""
        readers, _, _ = select.select(inputs, [], [])
        for reader in readers:
            if reader is listen_sock:
                conn_sock, client_addr = listen_sock.accept()
                chat_sock_serv = active_socket(conn_sock, client_addr)
                app = "server"
                break
            else:
                chat_sock_client = active_socket()
                chat_sock_client.connect(ADDR2)
                app = "client"
                break

        if app == "server":
            chat_sock_serv.chat()
            del chat_sock_serv
        elif app == "client":
            chat_sock_client.chat()
            del chat_sock_client
    

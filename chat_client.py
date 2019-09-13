import socket
import select
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8081))

while True:
    inputs = [sys.stdin, client_socket]
    readers, _, _ = select.select(inputs, [], [])
    for reader in readers:
        if reader is client_socket:
            print(f"<<localhost>> {client_socket.recv(1024)}")
            sys.stdout.flush()
        else:
            msg = sys.stdin.readline();
            b_msg = bytes(msg, 'utf-8')
            client_socket.send(b_msg)
            print(f"<<You>> {msg}")
            sys.stdout.flush()
            sys.stdin.flush()

client_socket.close()

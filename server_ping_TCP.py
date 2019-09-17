import socket
import random
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 11100))

while True: 
    sock.listen()
    conn, addr = sock.accept()
    start = time.time()
    random.randint(1, 1000) 
    end = time.time()
    elapsed = end-start
    print(f"Connected to {addr}     DELAY: {elapsed*1000}ms")





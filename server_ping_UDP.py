import socket
import random
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 16000))

while True:
    rand = random.randint(1, 10)
    msg, addr = sock.recvfrom(1024)
    start = time.time()
    message = msg.upper()
    if rand >= 2:
        sock.sendto(message, addr)
    end = time.time()
    elapsed = end-start
    print(f"Connected to {addr}     DELAY: {elapsed*1000}ms")
sock.close()

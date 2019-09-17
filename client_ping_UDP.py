import time 
import socket

for ping in range(10):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1.0)
    msg = b'test'
    addr = ("127.0.0.1", 16000)

    start = time.time()
    sock.sendto(msg, addr)
    try:
        msg_recvd = sock.recv(1024)
        end = time.time()
        elapsed = end-start
        print(f"PINGNo. {ping}   Time elapsed: {elapsed*1000}ms   msg: {msg_recvd}")
    except:
        print(f"PINGNo. {ping}   Request Timed out")
        



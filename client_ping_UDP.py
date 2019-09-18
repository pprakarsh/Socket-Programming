import time 
import socket

count = 0
sum = 0
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
        count += 1
        sum += elapsed
        print(f"PINGNo. {ping}   Time elapsed: {elapsed*1000} ms   msg: {msg_recvd}")
    except:
        print(f"PINGNo. {ping}   Request Timed out")

print(f"\nAverage Round Trip Time: {sum*1000/count} ms")
        



import socket
import time

addr = ("", 11100)
count = 0
sum = 0
for pings in range(10):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"\nPINGNo. {pings}:")
    try:
        start = time.time()
        sock.connect(addr)
        end = time.time()
        print(f"connected to {addr}")
        elapsed = end-start
        count += 1
        sum += elapsed
    except:
        print("Cannot connect to {addr}")

    print(f"RTT: {elapsed*1000}ms")
    sock.close()

print(f"\nAverage Round Trip Time: {sum*1000/count} ms")

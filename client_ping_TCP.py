import socket
import time

addr = ("", 11100)
for pings in range(10):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"\nPINGNo. {pings}:")
    try:
        start = time.time()
        sock.connect(addr)
        end = time.time()
        print(f"connected to {addr}")
        elapsed = end-start
    except:
        print("Cannot connect to {addr}")

    print(f"RTT: {elapsed*1000}ms")
    sock.close()

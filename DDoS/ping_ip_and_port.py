import socket
import time
from datetime import datetime

TIMEOUT = 0.1
IP = '127.0.0.1'
PORT = '8000'

while True:
    time.sleep(1)
    t0 = time.time()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(TIMEOUT)
    try:
        sock.connect((IP, int(PORT)))
    except:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time is :", current_time, 'and server is down')
    else:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        sock.close()
        print("Current Time is :", current_time, 'and server is up')

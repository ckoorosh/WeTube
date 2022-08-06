import socket
import time
from datetime import datetime

TIMEOUT =0.001
IP = '127.0.0.1'
PORT = '8000'

while True:
    time.sleep(1)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(TIMEOUT)
    try:
        t0 = datetime.now()
        sock.connect((IP, int(PORT)))
        now = datetime.now()
        sock.close()

    except:
        print('server is down')
    else:
        print("connecting time is :"+"{:.2f}".format(round((now - t0).total_seconds()*1000), 2)+ 'ms\tand server is up')

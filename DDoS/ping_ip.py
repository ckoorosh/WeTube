import time
from datetime import datetime

from pythonping import ping

TIMEOUT = 0.01
IP = '127.0.0.1'
PORT = '8000'

while True:
    time.sleep(1)
    response_list = ping('127.0.0.1', count=100)
    status = 'up' if response_list.rtt_avg_ms < TIMEOUT else 'down'
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time is :", current_time, 'and server is', status)

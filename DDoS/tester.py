import time
import requests

TIMEOUT = 6000  # microseconds
IP = 'http://127.0.0.1:'
PORT = '8000'

while True:
    time.sleep(1)
    try:
        x = requests.get(IP + PORT)
        if x.elapsed.microseconds > TIMEOUT:
            print('timeout for request')
        else:
            print('server is healthy')
    except:
        print('server is down')

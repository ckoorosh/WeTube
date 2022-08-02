import requests
import threading

NUMBER_OF_THREADS = 1000
IP = '127.0.0.1'
PORT = '8000'


class thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            try:
                requests.get('http://' + IP + ':' + PORT)
            except Exception as e:
                pass


for i in range(NUMBER_OF_THREADS):
    thread().start()

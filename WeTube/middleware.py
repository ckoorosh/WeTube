import os
import threading
import time
from datetime import datetime
from threading import Thread

class DDoS:
    def __init__(self, get_response):
        self.get_response = get_response
        self.ip_list = {}
        self.list_safe = []
        Thread(target=self.checker, args=()).start()

    def __call__(self, request):
        current_ip = request.environ["wsgi.input"].stream.raw._sock.getpeername()[0]
        if current_ip in self.ip_list.keys():
            self.ip_list[current_ip] += 1
        else:
            self.ip_list[current_ip] = 1
        response = self.get_response(request)
        return response

    def checker(self):
        while True:
            attack = False
            for ip, count in self.ip_list.items():
                if count > 20 and ip not in self.list_safe:
                    attack = True
            if attack:
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                log = open('log.txt', "a")
                log.write("Current Time is :" + str(current_time) + ' and DDoS detected\n')
                log.close()
            self.ip_list = {}
            time.sleep(1)

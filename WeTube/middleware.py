import os
import threading
import time
from datetime import datetime
from threading import Thread

"""
how to find number of requests per second threshold?
https://security.stackexchange.com/questions/118344/normal-usage-vs-denial-of-service-how-many-requests-are-needed-to-talk-about-a
simple answer : there is not any specific value for EVERY system.
"""

class DDoS:
    def __init__(self, get_response):
        self.get_response = get_response
        self.ip_list = {}
        # self.list_safe = ['127.0.0.1']
        self.list_safe =[]
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
                if count > 100 and ip not in self.list_safe:
                    attack = True
            if attack:
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                log = open('log.txt', "a")
                log.write("Current Time is :" + str(current_time) + ' and DDoS detected\n')
                log.close()
            self.ip_list = {}
            time.sleep(1)

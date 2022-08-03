import os
import time
from datetime import datetime
from threading import Thread

ip_list = {}
list_safe = []
started = False
completeName = os.path.join('C:\\Users\\malik\\PycharmProjects\\WeTube\\DDoS', 'log' + ".txt")
log = open(completeName, "a")


def check_request(request):
    current_ip = request.environ["wsgi.input"].stream.raw._sock.getpeername()[0]
    if current_ip in ip_list.keys():
        ip_list[current_ip] += 1
    else:
        ip_list[current_ip] = 1


def init():
    global started
    time.sleep(1)
    Thread(target=checker, args=()).start()
    started = True


def checker():
    global ip_list
    while True:
        attack = False
        for ip, count in ip_list.items():
            if count > 10 and ip not in list_safe:
                attack = True
        if attack:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            log.write("Current Time is :" + str(current_time) + ' and DDoS detected\n')
        ip_list = {}
        time.sleep(1)

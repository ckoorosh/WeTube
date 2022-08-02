import os
import time
from datetime import datetime
from threading import Thread

ip_list = {}
started = False
completeName = os.path.join('C:\\Users\\malik\\PycharmProjects\\WeTube\\DDoS', 'log'+".txt")



def check_request(request):
    current_ip = request.environ["wsgi.input"].stream.raw._sock.getpeername()[0]
    if current_ip in ip_list.keys():
        ip_list[current_ip] += 1
    else:
        ip_list[current_ip] = 1
    print(ip_list)


def init():
    global started
    time.sleep(1)
    print('this is init')
    Thread(target=checker, args=()).start()
    print('how hi')
    started = True


def checker():
    print('checker')
    global ip_list
    while True:
        attack = False
        for count in ip_list.values():
            if count > 10:
                attack = True
        if attack:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            log = open(completeName, "a")
            log.write("Current Time is :" + str(current_time) + ' and DDoS detected\n')
            log.close()
        ip_list = {}
        time.sleep(1)


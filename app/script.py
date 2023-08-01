#!/usr/bin/python3

import socket
import time

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('db',6200))
    if result == 0:
        sys.stdout.write("Port is open\n")
    else:
        sys.stdout.write("Port is not open\n")
    sock.close()
    time.sleep(5)

#!/usr/bin/env python
import socket, os
import sys
import select

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 4096
MESSAGE = "Hey! What's up?"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

msg = raw_input('< You > : ')

try:
    s.sendall(msg)
    data = s.recv(BUFFER_SIZE)
    print '< Friend > : ' , str(data)
    
except socket.error, e:
    print 'Send failed' + str(e)
    sys.exit()

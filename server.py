#!/usr/bin.env python
import socket, os, errno, time

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)


while 1:
    c = s.accept()
    cli_sock, cli_addr = c
    if os.fork():
        cli_sock.close()
    else:
        data = cli_sock.recv(BUFFER_SIZE)
        if not data:
            break
        
        print '< Friend > : ' , str(data)
        
        server_msg = raw_input('< You > : ')
        cli_sock.send(server_msg)
        cli_sock.close()

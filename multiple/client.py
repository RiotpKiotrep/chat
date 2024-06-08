import socket
from _thread import *
import select
import sys
import time

def szyfruj(txt):
    zaszyfrowny = ""
    k=3
    for i in range(len(txt)):
        if ord(txt[i]) > 122 - k:
            zaszyfrowny += chr(ord(txt[i]) + k - 26)
        else:
            zaszyfrowny += chr(ord(txt[i]) + k)
    return zaszyfrowny

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


if len(sys.argv)!=4:
    print("Argument format: client.py <IP address> <port> <name>")
    exit()

IPaddr=str(sys.argv[1])
port=int(sys.argv[2])
server.connect((IPaddr,port))
name=str(sys.argv[3])

while True:
    socket_list=[sys.stdin,server]

    read_sockets,write_socket,error_socket=select.select(socket_list,[],[])

    for sock in read_sockets:
        if sock==server:
            message=(sock.recv(2048)).decode()
            print(message)
        else:
            message=sys.stdin.readline()
            message_to_send=szyfruj(f"{name}: {message}")
            server.send(message_to_send.encode())
            sys.stdout.write(f"You ({name}): ")
            sys.stdout.write(message)
            sys.stdout.flush()

server.close()
import socket
import sys
import time

socket_server=socket.socket()
server_host=socket.gethostname()
ip=socket.gethostbyname(server_host)
server_port=8080

print(f"Your IP: {ip}")
server_host=input("Enter server IP:")
name=input("Enter server name:")

socket_server.connect((server_host,server_port))

socket_server.send(name.encode())
server_name=socket_server.recv(1024)
server_name=server_name.decode()

print(f"{server_name} has joined")
while True:
    message=(socket_server.recv(1024)).decode()
    print(f"{server_name}:{message}")
    message=input("Me:")
    socket_server.send(message.encode())
import socket
import sys
import time

new_socket=socket.socket()
host_name=socket.gethostname()
s_ip=socket.gethostbyname(host_name)
port=8080

new_socket.bind((host_name,port))
print("Binding successful")
print(f"Your IP: {s_ip}")

name=input("Enter name:")
new_socket.listen(1)

conn, add=new_socket.accept()
print(f"Retrieved connection from: {add[0]}")
print(f"Connection established from: {add[0]}")

client=(conn.recv(1024)).decode()
print(f"{client} has conneccted")
conn.send(name.encode())

while True:
    message=input("Me: ")
    conn.send(message.encode())
    message=conn.recv(1024)
    message=message.decode()
    print(f"{client}:{message}")
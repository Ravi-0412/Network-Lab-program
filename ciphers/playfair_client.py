import socket
c= socket.socket()
port= 5550
c.connect((socket.gethostname(),port))
txt= c.send(input("enter the text: ").encode())
key= c.send(input("enter the key: ").encode())
print(c.recv(1024).decode())















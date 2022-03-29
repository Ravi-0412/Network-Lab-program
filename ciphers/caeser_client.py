import socket
c= socket.socket()
port= 5550
c.connect((socket.gethostname(),port))
print(c.recv(1024).decode())
txt= input("enter the txt : ")
c.send(txt.encode())
key= input("enter the key value : ")
c.send(key.encode())
print("encrypted text is:",c.recv(1024).decode())
c.close()

import socket
s= socket.socket()
print("socket created")
port=1010
s.bind((socket.gethostname(),port))
s.listen(5)
print("waiting for connections")

while True:
    c, addr= s.accept()
    print("connected with address", addr)
    c.send("welcome to the server!".encode())       




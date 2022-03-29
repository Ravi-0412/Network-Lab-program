import socket
s=socket.socket()
port=4000
s.bind((socket.gethostname(),port))
s.listen(5)
print("waiting for connections")

while True:
    c,addr= s.accept()
    print("connected with address",addr)
    n= int(c.recv(1024).decode())
    if(n%2==0):
        c.send(("number is even").encode())
    c.send(("number is odd").encode())
    c.close()
    
import socket
s=socket.socket()
port=7888
s.bind((socket.gethostname(),port))
s.listen(5)
print("waiting for connections")

while True:
    c,addr= s.accept()
    print("connected with address",addr)
    n= c.recv(1024).decode()
    #l=len(n)
    #for i in range(0,(int)(l/2)):
    #    if(n[i]!=n[l-i-1]):
    #        c.send(("number is not palindrome").encode())
    if(n==n[::-1]):
        c.send(("number is palindrome").encode())
    c.send(("number is  not palindrome").encode())
    c.close()
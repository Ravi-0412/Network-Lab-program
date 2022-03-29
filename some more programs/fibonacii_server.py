import socket
s=socket.socket()
port=7888
s.bind((socket.gethostname(),port))
s.listen(5)
print("waiting for connections")

while True:
    c,addr= s.accept()
    print("connected with address",addr)
    n= int(c.recv(1024).decode())
    a=0;
    b=1;
    res="0 1 "
    for i in range(n-2):
        temp=a+b
        res+=str(temp)+" " # appending temp in res which is of type string
        a=b
        b=temp    
    c.send(("fibonacii sequence is:").encode())
    c.send(res.encode())
    c.close()
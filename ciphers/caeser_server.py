def caeser(txt,key):
    ans= ""
    for i in range(len(txt)):
        if 65<=ord(txt[i])<=90:
            ans+= chr((ord(txt[i])+key-65)%26 +65)
        else:
            ans+= chr((ord(txt[i])+key-97)%26 +97)
    return ans

# print(caeser("zdtx",4))

import socket
s=socket.socket()
port= 5550
s.bind((socket.gethostname(),port))
s.listen(5)
print("waiting for connections:")
while True:
    c,addr= s.accept()
    print("connected to:",addr)
    c.send("welcome to the server!".encode())
    txt= c.recv(1024).decode()
    print(txt)
    key= int(c.recv(1024).decode())
    print(key)
    c.send(caeser(txt,key).encode())
    c.close()

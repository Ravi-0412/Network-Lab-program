
def proper_txt(txt):
    n= len(txt)
    for i in range(0,n-1,2):
        if txt[i]==txt[i+1]:
            txt= txt[:i+1] + "X" + txt[i+1:]
    if len(txt)!= 0:
        txt+= "Z"
    return txt

def fill_matrix(key):
    matrix= [[0 for j in range(5)]for i in range(5)]
    single_arr= []
    for ele in key:
        k= ele
        if k== 'J':
            k= 'I'
        if k not in single_arr:
            single_arr.append(k)
    for i in range(65,91):
        if chr(i) not in single_arr and chr(i)!='J':
            single_arr.append(chr(i))
    k=0
    for i in range(5):
        for j in range(5):
            matrix[i][j]=single_arr[k]
            k+= 1
    return matrix

def index_locator(ch,matrix):
    position=[]
    if ch== 'J':
        ch= 'I'
    for i in range(5):
        for j in range(5):
            if matrix[i][j]==ch:
                position.append(i)
                position.append(j)
                break
    return position

def encryption(txt,key):
    txt=proper_txt(txt.upper())
    ans= ""
    matrix= fill_matrix(key.upper())
    for i in range(0,len(txt)-1,2):
        index1= index_locator(txt[i],matrix)
        index2= index_locator(txt[i+1],matrix)
        if index1[0]==index2[0]:
            ans+= matrix[index1[0]][(index1[1]+1)% 5]
            ans+= matrix[index2[0]][(index2[1]+1)% 5]
        elif index1[1]==index2[1]:
            ans+= matrix[(index1[0]+1)% 5][index1[1]]
            ans+= matrix[(index2[0]+1)% 5][index2[1]]
        else:
            ans+= matrix[index1[0]][index2[1]]
            ans+= matrix[index2[0]][index1[1]]
    return ans



import socket
s= socket.socket()
port= 5550
s.bind((socket.gethostname(),port))
s.listen(5)
print("waiting for connections: ")
while True:
    c,addr= s.accept()
    print("connected to :",addr)
    txt= c.recv(1024).decode()
    key= c.recv(1024).decode()
    c.send(encryption(txt,key).encode())




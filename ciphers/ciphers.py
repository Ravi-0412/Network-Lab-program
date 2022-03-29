# caeser

def encryption(txt, value):
    res=""
    for i in range(len(txt)):
        if 65<= ord(txt[i]) <= 90:  # means upper case
            res+= chr((ord(txt[i]) +value -65)%26 + 65)
        if 97<= ord(txt[i]) <= 122:  # means lower case
            res+= chr((ord(txt[i]) +value -97)%26 + 97)
    return res

        
txt= input("enter the text: ")
value= int(input("enter the value: "))
print(encryption(txt, value))

# columnar

import math

def encryption(txt, key):
    col= len(key)
    row= math.ceil(len(txt)/len(key))
    txt_position= [["*" for i in range(len(key))] for j in range(row)]
    # now fill the matrix with txt
    count= 0
    for i in range(row):
        for j in range(col):
            if count< len(txt):
                txt_position[i][j]= txt[count]
                count+= 1
    
    # For result, sort the key and print acc to the col of sorted key
    key1= sorted(key)  # will convert the string 'key' into a sorted 
                        # list of of characters
    res= ""
    for i in range(len(key)):
        index1= key.index(key1[i])  # getting the index of smallest ele in key
        for j in range(row):
            res+= txt_position[j][index1]  # print the ele of that col keeping row same
    return res
        
 
txt= input("enter the text: ")
key= input("enter the key: ")
# print("encrypted string: ",encryption(txt, key))


# vignere
def key_txt_equal(txt, key):
    if len(txt)== len(key):
        return key
    else:
        n= len(key)  # beacuse after appending in loop key size will increase
        for i in range(n,len(txt)):
            key+= key[i % n]  
        return key

def encryption(txt, key):
    txt= txt.upper()
    key= key.upper()
    key= key_txt_equal(txt, key)
    print(key)
    res= ""
    for i in range(len(txt)):
        res+= chr((ord(txt[i])+ord(key[i]))%26 +65)
    return res

txt= input("enter the text: ")
key= input("enter the key: ")
# key_txt_equal(txt, key)
# print(encryption(txt, key))


# Play fair
def proper_txt(txt):  # make the text into proper format
    for i in range(0,len(txt)-1,2):   # have to check each pair
        if txt[i]== txt[i+1]:   # if both char in a pair is same, 
                               # append special char 'Z' bw the char
            txt= txt[:i+1] + 'Z' + txt[i+1:]
    # now check if len of txt is odd then append again one 
    # special char 'x' at last to make it even to split in pair later  
    if len(txt)%2 != 0:
        txt= txt+ 'Z'
    return txt       

def fill_matrix(key):  # fill the matrix with keys and remaining ele
    key_matrix= [[0 for i in range(5)] for j in range(5)]
    key_array= []   # to store the key after replacing 'J' and after removing the saem ele
    for ele in key:
        k= ele
        if ele== 'J':  # IF 'J' replace it with 'I'
            k= 'I'
            key_array.append(k)
        if ele not in key_array: # if not present then append otherwise skip
            key_array.append(ele)
    # now add the remaining letters if they are not in the key_array
    for i in range(65,91):   # checking by ascii value      
        k= chr(i)
        k=chr(i)
        if k=='J':   # check for 'J'
            k='I'
        if k not in key_array:   # now check if ele is already present
            key_array.append(k)
    print(key_array)
    # Now fill the key_matrix with key_array
    index=0 # to incr the index of key_array 
    for i in range(5):
        for j in range(5):
            key_matrix[i][j]= key_array[index]
            index+= 1
    return key_matrix

    # function to find the row and col of each element of 'text' in key_matrix
def index_locator(ch, key_matrix):
    index1= []    # since we have to store both row and col
    if ch== 'J':
        ch= 'I'
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j]== ch:
                index1.append(i)
                index1.append(j)
                break
    return index1

def encryption(txt, key):
    txt= proper_txt(txt)
    key_matrix= fill_matrix(key)
    print(key_matrix)
    res= ""
    for i in range(0,len(txt)-1,2):
        ch1, ch2= txt[i], txt[i+1]
        index1, index2= index_locator(ch1,key_matrix), index_locator(ch2,key_matrix)
        # if both are in same row , take one col ahead of each  
        if index1[0]== index2[0]:
            res+= key_matrix[index1[0]][(index1[1]+1)% 5]
            res+= key_matrix[index2[0]][(index2[1]+1)% 5]
        # if both are in same col , take one row ahead of each 
        elif index1[1]== index2[1]:
            res+= key_matrix[(index1[0]+1)% 5][index1[1]]
            res+= key_matrix[(index2[0]+1)% 5][index2[1]]
        # if both not in same row or col, take the end point of rectangle
        # i.e keep the row same and swap the col
        else:
            k1,k2= index1, index2
            print(k1)
            print(k2)
            res+= key_matrix[index1[0]][index2[1]]
            res+= key_matrix[index2[0]][index1[1]]
    return res

# give all the inputs in capital letter
txt= input("enter the text: ")
key= input("enter the key: ")
print(proper_txt(txt))
print(fill_matrix(key))
print("encrypted string: ",encryption(txt, key))


# Railfence
def encryption(txt, key):
    txt_position= [[0 for i in range(len(txt))] for j in range(key)]
    # now put the txt into above matrix
    row= 0
    down= False # down== false means we can't traverse below
    for i in range(len(txt)):
        # 'i' will work as col since we hav eto incr col always
        txt_position[row][i]= txt[i]
        # now check the value of down to incr/decr the row
        if row==0 or row== key-1:
            down= not down  # change the down to traverse in opposite direction
        if down:  # go on incr row(go below) until down becomes false
            row+= 1
        else:     # go on decr row(go below) until down becomes false
            row-= 1

    # now matrix is filled so now now traverse the matrix to get the result
    res= ""
    for i in range(key):
        for j in range(len(txt)):
            # check if '0' is not presnt at ele, then only store the result
            if txt_position[i][j]!= 0:
                res+= str(txt_position[i][j])
    return res

        
txt= input("enter the text: ")
key= int(input("enter the key: "))
print(encryption(txt, key))


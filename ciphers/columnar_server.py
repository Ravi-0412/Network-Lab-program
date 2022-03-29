import math
def columnar(txt,key):
    ans= ""
    col= len(key)
    row= math.ceil(len(txt)/len(key))
    matrix= [[' ' for i in range(col)] for i in range(row)]
    k=0
    for i in range(row):
        for j in range(col):
            if k<len(txt):
                matrix[i][j]= txt[k]
                k+= 1
    temp= sorted(key)
    for i in range(len(key)):
        index1= key.index(temp[i])
        for j in range(row):
            ans+= matrix[j][index1]
    return ans

print(columnar("geeks for geeks","hack"))

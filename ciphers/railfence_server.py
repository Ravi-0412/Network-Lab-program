
def railfence(txt,key):
    matrix= [[' ' for j in range(len(txt))]for i in range(key)]
    down= False
    row=0
    ans= ""
    for i in range(len(txt)):
        matrix[row][i]= txt[i]
        if row== 0 or row== key-1:
            down= not down
        if down:
            row+= 1
        else:
            row-= 1
    for i in range(key):
        for j in range(len(txt)):
            if matrix[i][j]!= ' ':
                ans+= matrix[i][j]
    return ans

print(railfence("geeksforgeeks",3))



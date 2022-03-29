def vignere(txt,key):
    ans= ""
    n= len(key)
    for i in range(n,len(txt)):
        key+= key[i%n]
    for i in range(len(txt)):
        ans+= chr((ord(key[i])+ord(txt[i]))%26 +65)
    return ans
print(vignere("GEEKSFORGEEKS","AYUSH"))

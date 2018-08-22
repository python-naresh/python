#it will print enter file
x=open("xyz.txt","r")
#print(x.read())
#print(x.read())
print(x.read(1))
#already 1 letter readed so it will start from next letter
int(x.read(2))
print(x.read(3))
print(x.read(4))

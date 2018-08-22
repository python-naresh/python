x=open("xyz.txt","r")

print(x.read())
#already file readed fully so it will not read again 
print(x.read(1))
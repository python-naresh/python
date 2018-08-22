x=1
while x< 11:
    y=1
    while y<11:
     print(x,"*",y,"=",x*y)
     y+=1
    x+=1

# if u miss any space it will not execute beacause that line will be in another while loop
#see y+=1 is in middel while loop,x+=1 is in first while loop

for i in range(1,11):
    for s in range(1,11):
        print(i,"*",s,"=",i*s)
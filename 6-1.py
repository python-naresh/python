#for x in list:
# print(x)

#list=(234,14253,123,1234,435)

for x in (1,2,3,4,5):
    print(x)

y=open("xyz.txt","r")
x=y.read()
for p in x:
    print(p)	


	
for x in "hello":
    print(x)
	
	
	
	# above both 3 codes are same 
	# both code will execute as list and letter by letter in file and element by element in list
	
	
y=open("xyz.txt","r")
for x in y:
    print(x)
	
	#it will print line by line of that file



for x in {"hello"}:
    print(x)

for z in range(1,20,2):
    print(z)
for p in range(1,6,1):
    for u in range(1, 10, 1):
        print(p,"*",u,"=",p*u)
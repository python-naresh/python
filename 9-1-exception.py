x=input("enter x value")
y=input("enter y value")
try:
    print(int(x)+int(y))
except:
    print("you entered wrong ")
finally:
    print("u entered coorect values , u got output")
# if u entered wrong syntax like if u enter string for x or y it will print    expect
#if u entered number it will execute try and next finally
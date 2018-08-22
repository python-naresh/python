def age():
    t=input("give me seconds (s) or years (y)")
    if t=="s":
        re=int(input("enter your age in years"))
        gt=re*365*24*60*60
        print("your age is {} seconds".format(gt))
    elif t == "y":
        re = int(input("enter your age in seconds"))
        gt = re / 365 / 24 / 60 / 60
        print("your age is {} years".format(gt))
    else:
          print("enter corect value")

age()
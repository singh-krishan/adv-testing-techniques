def addthis(x,y):
    #print(f"x is {x} and y is {y}")
    try:
        result = x+y
    except TypeError:
        print(f"wrong type passed as parameter")

print(addthis(1,'a'))
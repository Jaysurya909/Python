x=99


def myfun():
    global x #this is used to change the global varible in a function
    x=44
    y=67
    print("y=",y)
 

myfun()
print("x=",x)


#print(y)#this will give error as y is local variable


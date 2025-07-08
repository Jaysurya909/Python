from functools import reduce


def addition(x,y):
    return x+y


l=[1,2,3,4,5]

print(reduce(addition,l))


print(reduce(lambda x,y:x*y,l))
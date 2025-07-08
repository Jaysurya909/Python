def square(x):
    return x*x


l=[23,44,5,65,3]

print(list(map(square,l)))# we can use lambda function in place of square function

def even_number(x):
    return x%2==0

numbres=[1,2,4,5,45,6]

evens=list(filter(even_number,numbres))  # i can also typecast it as a list in print statement

print(evens)  
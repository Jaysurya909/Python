def my_generator():
    for i in range(54):
        yield i         # it will only generate values when required and do not take memory space when not required

gen=my_generator()


for j in gen:       # prints the yield value from the function when called only
    print(j)        


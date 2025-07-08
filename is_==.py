#COMPARISON OPERATORS 

# "is" exact location of a object in memory
# "==" as compared to the object 

#values which are immutable returns true in every case

a=4 #int is immutable
b=4

print(a is b)
print(a==b)

a=(1,2,5) #tuple is immutable
b=(1,2,5)

print(a is b)
print(a==b)

a={1,2,5} #lists are un-immutable
b={1,2,5}

print(a is b) # this will return false because 
print(a==b)
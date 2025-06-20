tup=(1,24,544,3423,)
#tup[0]=456     this will throw error we cant change tuple
print(tup)

tup2=tup #this makes a new tuple and wont change the existing one
print(tup2)

regions=("india","russia","Spain","china")
print(type(regions))
temp=list(regions) # tuple to list conversion
print(type(temp))
temp.pop(3)
temp.append("Antartica")
regions=tuple(temp) # list back into tuple
print(regions)

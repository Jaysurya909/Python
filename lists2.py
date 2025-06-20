l= [2,45,65,78,11,234]
m=[34,600,599,999,999]

n=l.copy()
print(n)
print(l.index(65))
l.insert(0,1)
print(l)

print("The count of 999 in m is",m.count(999))
m.reverse()
print(m)

l.sort()
print("the sorted list",l)
l.sort(reverse=True)
print("The reverse sorted list",l)



k=l+m
print(k)
l.extend(m)
print(l)
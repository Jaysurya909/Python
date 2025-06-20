marks=[85,90,78,92,88]
n=0
lowest=marks[0]
p=0

#find the lowest using loop
for i in marks:
    if i<lowest:
       p=i

print(p)

#print list 
print(marks)

#sum the marks
total=sum(marks)
print("The total is ",total)

#find the average
average=total/len(marks)
print("The average of the marks is ",average)

#add more marks
marks.append(456)
print(marks)

#remove the lowest mark
lowest=min(marks)
marks.remove(lowest)

lowest = marks[0]
for i in marks:
    if i < lowest:
        p = i

print(p)

#final string
print(marks)


   





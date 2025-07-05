f=open("marks.txt",'r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    
    m1=int(line.split(",")[0])
    m2=int(line.split(",")[1])
    m3=int(line.split(",")[2])

    print(f"The marks of student{i} For Maths are {m1}")
    print(f"The marks of student{i} For Maths are {m2}")
    print(f"The marks of student{i} For Maths are {m3}")
    print(line)



    
    
class noob():
    def __init__(h1,rollno,name):  # we can use h1 or whatever in place of self
        h1.__rollno=rollno
        h1._name=name
        h1.__salary=5000



p1=noob
p1._name="naruto"
print(p1._name)     #we can access name directly without any error as it is only protected and not private

p1.__rollno=44  #this __rollno is accessable becoz it is defined outside the class and not inside the constructor

print(p1.__rollno)


p2=noob(14,"shinchan") 

print(p2.__rollno) 
#print(p2.__salary)        #salary is not accessable becoz it is defined inside the constructor and has a default value and it can be accessed by p2._noob__salry it is called name mangling
print(p2._noob__salary)



# a single underscore (_)   means it is a protected object but can be accessed without name mangling
# a double underscore (__) means it is a private object and needs name mangling to be accessed
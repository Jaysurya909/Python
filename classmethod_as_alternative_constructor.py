class strs1():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @classmethod
    def seprate(cls,string):
        name,salary=string.split("-") #or we can use *string.split("-") to unpack the string in two seprate things
        return cls(name,int(salary)) 


    



p0=strs1("new1",55000)

str11="Bot-25000"
p1=strs1.seprate(str11)

print(p1.name)
print(p1.salary)

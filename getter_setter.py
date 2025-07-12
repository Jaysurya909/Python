class person():
    def __init__(self,name,age):
        self.name=name
        self._age=age

    @property
    def age(self):
        return self._age  # this is the getter
    
    @age.setter           # this is the setter
    def age(self,value):
        if(value>=0):
            self._age=value
        else:
            print("Age cant be negative")



x=person("bot",9)

print(x._age)  # can also use x.age






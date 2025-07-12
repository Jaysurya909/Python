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

print(x.age)  # can also use x._age but using _age will directly access the variable self._age 

x.age=-5        #if we use x._age the value will change because we are directly accesing the private variable and not the setter

print(x.age)  #the value didnt change as we access the getter x.age and then calles the setter x.age





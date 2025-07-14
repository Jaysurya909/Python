#example 1
class calc():
    def __init__(self,num):
        self.num=num

    def selfadd(self,n):
        self.num=self.num+n
    
    @staticmethod
    def add(a,b):
        return a+b
    
# the add function is in the class but it does not depend on input like self or anything

a=calc(66)

a.selfadd(45)
print(a.num)# we need to make a object to access the selfadd function


print(a.add(45,65))# no need to make a object to access the add function



class greet():
    # def hello():
    #     print("Hello sir") even though there is no self arguemnt given but python automatically adds it
    @staticmethod
    def hello():
        print("Hello sir")


a=greet()
#a.hello()  this gives error as python automatically gives 1 arguement to hello function as its not a static method and gives error
a.hello()   #this runs without error as hello is now a static method and it does not take any self arguements automatically
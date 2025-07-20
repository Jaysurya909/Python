class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return f"{self.x}i + {self.y}j"

    def __add__(self,other):    # the __add__ is acting like the built in function (+) and add the p1 and p2 for example
        return f"{self.x+other.x}i + {self.y+other.y}j"



p1=Vector(2,4)
p2=Vector(5,7)
print(p1) # finds and uses the __str__ function
print(p2)
print(p1+p2)# it finds and uses the __add__ function


#just like add there are also other magic/dunder methods for subtraction,multiplication,comparison,etc.
    
        
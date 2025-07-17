class real():
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

class bot(real):
    def __init__(self, name, rollno,lang):
        super().__init__(name, rollno)# no need to define name and rollno logic in bot class as we are using super keyword to access it from real class
        self.lang=lang


p1=real("noob",54)
print(p1.name)

p2=bot("new",67,"English")
print(p2.rollno)
print(p2.lang)
class bot1():
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def showinfo(self):
        print(f"The id of the employee is {self.id} and name is {self.name}")


class bot2(bot1):
    def greet(self):
        print(f"Good morning {self.name}")







x1=bot1(500,"kenzo")

x1.showinfo()

x2=bot2(400,"Miyazaki")

x2.showinfo()
x2.greet()


















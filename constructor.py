class new():
    def __init__(self,x,y):
        print("This is init function")
        self.name=x
        self.job=y

    def info(self):
        print(f"The work of {self.name} is as a {self.job}")
  




a=new("bot","cleaner")# the first arguement is automatically given always!

print("The person",a.name,"is a",a.job) # No need to define a.name and a.job again to give value as it is already given in line 14

a.info() #it is printing a.name and a.job which is written as self.name and self.job in the info function so a=self











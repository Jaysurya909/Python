class animal:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound


    def sound_make(self):
        print(f"{self.name} makes the sound {self.sound}")


class Dog(animal):
    def __init__(self,name,breed):
        animal.__init__(self,name,sound="Bark!") # we do not need to define sound and name again here we just give the values (i only gave sound without constructor use)
        self.breed=breed # We defined breed here

    def sound_make(self): # This overwrites the animal sound_make() function
        print(f"The name of the dog is {self.name} and the sound it makes is {self.sound}")

class Lion(animal):
    def __init__(self,name,sound,age):
        super().__init__(name,sound)    # Think about this line!!!!!!!
        self.age=age
    
    def sound_make(self): #overwriting the sound_make from animal class
        print(f"The Lion {self.name} makes the sound {self.sound} and its age is {self.age}")

class monkey(animal):
    def __init__(self, name, sound ,age):
        super().__init__(name, sound) # no need to writ self when using super keyword
        self.age=age
    

        


p0=animal("Cat","Meow!")
p0.sound_make() #The sound_make function of animal class

p1=Dog("Bot22","Rotwheeler")
p1.sound_make() #The sound make functiom of Dog class

p2=Lion("Simba","Roar!!",8)
p2.sound_make()
        
p3=monkey("Chimpazi","hehe!!",45)
p3.sound_make() # monkey class used the sound_make function of animal class
# single inheritance is the most commonly used inheritance method 
class Engine:
    def feature(self):
        print("Engine: Powerful engine")

class Wheels:
    def feature(self):
        print("Wheels: Alloy wheels")

class Car(Engine, Wheels):
    def show_features(self):
        Engine.feature(self)
        Wheels.feature(self)

c = Car()
c.show_features()

# Simple level code
class Animal:
    def __init__(self,name):
        self.name=name
        

class sound1:
    def __init__(self,sound):
        self.sound=sound
        
    
class make_animal:
    def __init__(self,name,sound):
        Animal.__init__(self,name)
        sound1.__init__(self,sound)
        print(f"The name of the animal is {self.name} and sound of the animal is {self.sound} ")# it took the name from 



c=make_animal("Dog","!Bark!")


# Complex level code as we are using super keyword in the parent class aswell
class Animal:
    def __init__(self, name, **kwargs):
        self.name = name
        super().__init__(**kwargs)

class sound1:
    def __init__(self, sound, **kwargs):
        self.sound = sound
        super().__init__(**kwargs)

class make_animal(Animal, sound1):
    def __init__(self, name, sound):
        super().__init__(name=name, sound=sound)
        print(f"The name of the animal is {self.name} and sound of the animal is {self.sound}")



k=make_animal("Cat","Meow!!")        
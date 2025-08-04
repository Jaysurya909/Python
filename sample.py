class Animal:
    def __init__(self,Animal_name):
        self.Animal_name=Animal_name

    def showinfo(self):
        print(f"The name of the animal is:- {self.Animal_name}")

class Dog(Animal):
    def __init__(self,breed):
        super().__init__(Animal_name="Dog") # We are hardcoding Animal_name here
        self.breed=breed
    
    def showinfo(self):
        Animal.showinfo(self)
        print(f"The breed of the dog is:- {self.breed}")

class Bulldog(Dog):
    def __init__(self, dog_name,color):
        super().__init__(breed="Bulldog") # We are hardcoding breed here
        
        self.dog_name=dog_name
        self.color=color

    def showinfo(self):
        Dog.showinfo(self) # Also have to give self for first arguement here also
        print(f"The name of the dog is:- {self.dog_name}\nAnd the color of the dog is:- {self.color}")
        
p2=Dog("Rotwheeler")
p2.showinfo()

p3=Bulldog("Tommy","black")
p3.showinfo()

# super does not need self input at all
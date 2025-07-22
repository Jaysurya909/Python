# The hardcode method for Multilevel inheritance

class Animal:
    def __init__(self,Animal_name):
        self.Animal_name=Animal_name

    def showinfo(self):
        print(f"The name of the animal is:- {self.Animal_name}")

class Dog(Animal):
    def __init__(self,breed):
        Animal.__init__(self,Animal_name="Dog") # We are hardcoding Animal_name here
        self.breed=breed
    
    def showinfo(self):
        Animal.showinfo(self)
        print(f"The breed of the dog is:- {self.breed}")

class Bulldog(Dog):
    def __init__(self, dog_name,color):
        Dog.__init__(self,breed="Bulldog") # We are hardcoding breed here
        
        self.dog_name=dog_name
        self.color=color

    def showinfo(self):
        Dog.showinfo(self) # Also have to give self for first arguement here also
        print(f"The name of the dog is:- {self.dog_name}\nAnd the color of the dog is:- {self.color}")
        

p1=Bulldog("Tommy","White")
p1.showinfo()

# The more scalable and flexible method

class Animal:
    def __init__(self, Animal_name):
        self.Animal_name = Animal_name

    def showinfo(self):
        print(f"The name of the animal is:- {self.Animal_name}")

class Dog(Animal):
    def __init__(self, Animal_name, breed):
        super().__init__(Animal_name)
        self.breed = breed

    def showinfo(self):
        super().showinfo()
        print(f"The breed of the dog is:- {self.breed}")

class Bulldog(Dog):
    def __init__(self, Animal_name, breed, dog_name, color):
        super().__init__(Animal_name, breed)
        self.dog_name = dog_name
        self.color = color

    def showinfo(self):
        super().showinfo()
        print(f"The name of the dog is:- {self.dog_name}\nAnd the color of the dog is:- {self.color}")

# Now pass everything when creating the object
p1 = Bulldog("Dog", "Bulldog", "Tommy", "White")
p1.showinfo()

        

        
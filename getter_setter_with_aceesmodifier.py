#Getter and setter are basically used to access and update the private and protected objects
#Getter access them and setter updates them , we must first use getter to access them before updating with setter

class Noob:
    def __init__(self, rollno, name):
        self._rollno = rollno       # protected
        self._name = name           # protected
        self.__salary = 5000        # private

    # Getter for name
    def get_name(self):
        return self._name

    # Setter for name
    def set_name(self, new_name):
        self._name = new_name

    # Getter for rollno
    def get_rollno(self):
        return self._rollno

    # Setter for rollno
    def set_rollno(self, new_rollno):
        self._rollno = new_rollno

    # Getter for salary
    def get_salary(self):
        return self.__salary

    # Setter for salary
    def set_salary(self, new_salary):
        self.__salary = new_salary


# Create object
p1 = Noob(14,"Naruto") #to avoid error we are using this

# Using setter methods
p1.set_name("Sasuke")
p1.set_rollno(22)
p1.set_salary(10000)

# Using getter methods
print("Name:", p1.get_name())         # Sasuke
print("Roll No:", p1.get_rollno())    # 22
print("Salary:", p1.get_salary())     # 10000

# Second object
p2 = Noob(14, "Shinchan")
print("Name:", p2.get_name())         #we used the getter function to print the name
print("Roll No:", p2.get_rollno())
print("Salary:", p2.get_salary())

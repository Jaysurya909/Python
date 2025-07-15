class company():
    
    company_name="Samsung"  #Its a class variable
    employee_count=0

    def __init__(self,name):
        self.name=name  # this are the instance variables
        self.salary=5000  
        self.company_name="Google" #Instance variable will be shown as it has high priority
        company.employee_count+=1  #This will increment when the constructor is called to make a new employee e.g.,emp1 or emp2

    def show(self):
        print(f"The name of the employee is {self.name} and its salary is {self.salary} and they work in {self.company_name} which has {company.employee_count} employees")


# If we use self.employee_count in place of company.employee_count it will give same output but if we make a instance variable like emp1.employee_count it will overwrite
# the class variable which is not desired




emp1=company("Bot")
emp1.employee_count=5  # this would take place if we change the company.employee_count to self.employee_count in the show() function
emp1.show()
emp2=company("jay") 
emp2.company_name="Tesla"   #the instance variable has higher priority than class variable
emp2.salary=60000000
emp2.show()

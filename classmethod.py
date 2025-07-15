class company():
    company_name="Google"

    def show(self):
        print(f"The name of the person is {self.name} and name of the company is {self.company_name}")

    @classmethod        # This decorator is used to change class variables
    def changename(x,name):
        x.company_name=name














p1=company()
p1.name="Jay"
p1.show()
p1.changename("Apple")
p1.show()
print(company.company_name) # The name will be chnaged becoz classmethod is used 
                            # and if the classmethod is not used then the company name will only be changed for the instance p1
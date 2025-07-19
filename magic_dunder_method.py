class names:
    def __init__(self,name):
        self.name=name
    
    
    def __repr__(self):
        return f"The name is gives as {self.name} repr" # repr is used when str is absent
    
    def __str__(self):
        return f"The name is give as {self.name} str" # str has higher priority than repr
    
    def __call__(self):
        print("Hello i am bot")








p=names("Bot")
print(p)# it finds the str function(actually str is a object) and calls it automatically coz str is used for strings related things
p() # it is using the __call__ object to print without the call object this line will give error
print(repr(p))# The repr became a function and we used it without the underscores
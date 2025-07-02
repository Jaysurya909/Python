def nowelcome():
    print("You are not welcome here noob")

# this two lines below will run in main.py automatically
nowelcome()
print(__name__)



# it will only run in jay.py file not in main.py file
if __name__=="__main__":  
    nowelcome()

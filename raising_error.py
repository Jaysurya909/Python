class Quiterror(Exception):
    "When the quit word is used"
    pass


try:
    x=int(input("Enter a value in between 5 and 9"))
    if(x>9 or x<5 ):
        raise ValueError("Wrong value entered")
    elif(x=="quit"):
        raise Quiterror("Qutting the program")
except Quiterror as e:
    print(e)

    




    



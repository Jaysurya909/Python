def sample():
    try:
        ind1=[1,4,5,7]
        new1=int(input("Enter the index value you want"))
        print(ind1[new1])
        return 0
    except:
        print("You entered the wrong value")
        return 1
    finally:
        print("I am inevitable")



x=sample()
print(x)



#even if a value is returned in a fuction finally keyword still runs unlike a simple print or any other statement
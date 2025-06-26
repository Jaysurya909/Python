try:
    in1=int(input("Give the input in integer please"))
    for i in range(1,11):
        print("The table of given integer is",i*in1)
except:
    print("The input is not an integer")
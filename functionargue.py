def addition(a=10,b=23):
    print(a+b)
    
addition(3)

def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("The average is: ", sum/len(numbers))    

average(1,2,4,5,7)    

def multiply(a,b,c=10):
    print("The multiplication is: ", a*b*c)

multiply(10,25)
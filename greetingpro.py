import time

#n=int(time.strftime('%H'))
#print(n)
n=int(input("Enter the time"))

if((n>=6)and(n<12)):
    print("Good morning")
elif((n>=12)and(n<18)):
    print("Good Afternoon")
elif((n>=18)and(n<20)):
    print("Good Evening")
else:
    print("Good night")    
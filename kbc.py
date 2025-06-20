questions=["1. Which of the following is the largest planet in our solar system?\na.Mars b.Jupiter c.Earth d.Venus", 
           "2. What is the chemical symbol for water?\na.O2 b.CO2 c.H2O d.NaCl",
           "3. Who painted the Mona Lisa?\na.Vincent van Gogh b.Pablo Picasso c.Leonardo da Vinci d.Claude Monet"]

answers=['b','c','c']

input1=[]
j=0
for i in questions:
    print(i)
    option=input("Enter your answer ")
    input1.append(option)
    if input1[j]==answers[j]:
        print("Your answer is correct")
        if j==0:
            print("You won $100")
        elif j==1:
            print("You won $200")
        elif j==2:
            print("You won $300")
    else:
        print("Your answer is wrong")
    j+=1

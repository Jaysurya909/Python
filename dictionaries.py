new={911:"paimon","cgpa":9,}# here 911 is a key and cgpa is also a key
#print(new['paimon']) this will give error as paimon is not a key it is a value
print(new)
print(new.values())
print(new.keys())

#using for loop
for key in new:
    print(f"The value of {key} in new_dictionary is {new[key]}")

print(new.items())

#print(new[899]) this gives error
print(new.get(899)) #this gives None value

bot={89:'bot',89:'noob'}  #this gives the last assigned value to a key

print(bot)


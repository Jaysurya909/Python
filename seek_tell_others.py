with open("noob.txt",'r') as f:
    f.seek(9)
    bot=f.tell() #it tells from which line the reading has start
    print(bot)
    vari=f.read(10)
    print(vari)

print("Use of truncate")

with open("noob1.txt",'w') as f:
    f.write("Heloow am i doing something helowrwe")
    f.truncate(8) # It determines how much characters can be written in a file

with open("noob1.txt",'r') as f:
    new=f.read()
    print(new)
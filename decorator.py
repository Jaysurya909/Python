def bot(fx):
    def mfx():
        print("Good morning sir!!")
        fx()
    return mfx # dont need to use () when returning a function
   


@bot
def hello():
    print("Hello world")


hello()

# bot(hello)()   anotheer way of calling the bot function without using @

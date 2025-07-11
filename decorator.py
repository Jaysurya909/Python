def bot(fx):
    def mfx():
        print("Good morning sir!!")
        fx()
    return mfx
   


@bot
def hello():
    print("Hello world")


hello()

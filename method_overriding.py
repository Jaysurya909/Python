class real():
    def state(self):
        print("This is the real class")


class bot(real):
    def state(self): # this method/function was defined in the real class which is the parent class but the bot class override the method and made its own original state method 
        print("This is the bot class")
        super().state() # calling the real class method without override



p=real()
p2=bot()

p.state()
p2.state()
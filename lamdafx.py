square= lambda x:x*x

def bot(fx,value):
    return 6+fx(value)


print(square(4))

print(bot(lambda x:x*x*x,5))



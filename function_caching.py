from functools import lru_cache
import time


@lru_cache(maxsize=None)
def square(n):
    time.sleep(5)
    return n*n

print(square(5))
print("5 is done")
print(square(10))
print("10 is done")
print(square(15))
print("15 is done")


print(square(5))# it will print rapidly from here
print("5 is done")
print(square(10))
print("10 is done")
print(square(15))
print("15 is done")

print(square(40))# will wait again 5 second to compute 40 for first time
print("Done for 40")

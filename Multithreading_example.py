import threading
import time

def greet(name):
    print(f"Hello, {name}!")
    time.sleep(2)  # Simulate some delay
    print(f"Goodbye, {name}!")

# Create two threads
t1 = threading.Thread(target=greet, args=("Alice",))
t2 = threading.Thread(target=greet, args=("Bob",))

# Start both threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print("Main program ends.")

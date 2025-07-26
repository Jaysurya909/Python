import multiprocessing
import time

def worker(num):
    print(f"Worker {num} is running")
    time.sleep(2)
    print(f"Worker {num} is done")

if __name__ == '__main__':
    # Create two processes
    p1 = multiprocessing.Process(target=worker, args=(1,))
    p2 = multiprocessing.Process(target=worker, args=(2,))

    # Start the processes
    p1.start()
    p2.start()

    # Wait for them to finish
    p1.join()
    p2.join()

    print("Both workers finished")

# It provides true parallelism which is not possible in multithreading due to global interpretor lock
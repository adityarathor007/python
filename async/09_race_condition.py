#happens because the other thread might be holding the older value on which it updates rather on the actual value which has been updated 

import threading
import time

# Shared resource
counter = 0

def increment():
    global counter
    for _ in range(10000):
        # Explicitly splitting the step to simulate how the OS 
        # interrupts threads during non-atomic updates
        current_value = counter
        time.sleep(0.000001)  # Forces a context switch / thread swap
        counter = current_value + 1

if __name__ == "__main__":
    threads=[threading.Thread(target=increment) for _ in range(2)]

    for t in threads: t.start()
    for t in threads: t.join()

    print(f"Expected value: 2000000")
    print(f"Actual value:   {counter}") 
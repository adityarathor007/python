# GIL: ensures that only one thread can execute Python bytecode at a time 
# OS: schedules the threads onto CPU cores.
# Python GIL: determines which thread can execute Python bytecode in CPython.
# Thus because of this threading works best in 
# - i/o bnd task, web request  

import time
import threading

# def brew_chai():
#     print(f"{threading.current_thread().name} start brewing...")
#     count=0
#     for _ in range(100_000_000):
#         count+=1
    
#     print(f"{threading.current_thread().name} finished brewing...")


# thread1=threading.Thread(target=brew_chai,name="Barista-1")
# thread2=threading.Thread(target=brew_chai,name="Barista-2")

# start=time.time()
# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()
# end=time.time()

# print(f"total time taken: {end-start}")


#multiprocesing is ideal for cpu intensive task (like image processing or running ai models)
from multiprocessing import Process

def cpu_heavy():
    print("Crunching some numbers...")
    total=0
    for i in range(10**8):
        total+=i
    print("Done")

if __name__=="__main__":
        
    start=time.time()
    processes=[Process(target=cpu_heavy) for _ in range(2)]
    [t.start() for t in processes]
    [t.join() for t in processes]
    end=time.time()

    print(f"Time taken: {end-start}")


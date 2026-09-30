import threading
import time

def take_order():
    for i in range(1,4):
        print(f"Taking order for #{i}")
        time.sleep(2) #this pauses the current executing thread and tells the OS to free up the CPU so that other process can run

def brew_chai():
    for i in range(1,4):
        print(f"Brewing chai for #{i}")
        time.sleep(3)

#creating threads 
order_thread=threading.Thread(target=take_order)
brew_thread=threading.Thread(target=brew_chai)

#start the threads
order_thread.start()
brew_thread.start()

#wait for threads to finish (because the parent thread needsa to synchronize with the background work it started) -> if the main thread finishes then the bg threads may have ran incomplete leading to inconsistent results
order_thread.join()
brew_thread.join()

print("All order taken and chai brewed")
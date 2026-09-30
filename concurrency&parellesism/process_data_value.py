from multiprocessing import Process,Value

def increment(counter):
    for _ in range(100000):
        # lock is needed because 2 process could read the same value and overwrite each other's increment 
        with counter.get_lock(): #acquires lock -> inc the counter -> release lock
            counter.value+=1


if __name__=="__main__":
    counter=Value('i',0)
    processes=[Process(target=increment,args=(counter,)) for _ in range(4)]
    [p.start() for p in processes]
    [p.join() for p in processes]

    print("Final counter value:", counter.value)

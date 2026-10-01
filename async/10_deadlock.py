import threading 

lock_a=threading.Lock()
lock_b=threading.Lock()

def task1():
    with lock_a:
        print("Task 1 acquired lock a")
        with lock_b:
            print("Task 1 acquired lock b")


def task2():
    with lock_b:
        print("Task 2 acquired lock b")
        with lock_a:
            print("Task 2 acquired lock a")


t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)

t1.start()
t2.start()

#sometime the code will run if the thread1 completes its execution and another thread comes in
#but when half thread1 runs then thread2 comes and run, then both locks are occupied so cant move forward
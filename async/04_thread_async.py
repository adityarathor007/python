import asyncio
import time
from concurrent.futures import ThreadPoolExecutor 

def check_stock(item):
    print(f"Checking {item} in store")
    time.sleep(3) #blocking operation
    return f"{item} stock: 42"

#takes the heavy duty task and keep inside another thread -> rather than main thread
async def main():
    loop = asyncio.get_running_loop() #which event loop is currently running my async function
    with ThreadPoolExecutor() as pool:  #pool of worker threads (5 threads). When you give it jobs, it distributes them among these threads.
        result=await loop.run_in_executor(pool,check_stock,"Masala Chai") #takes the blocking function -> hands it over to the ThreadPoolExecturo to run in the bacground
        # it sits inside the async event loop and waits for the threads to finish 
        print(result)


asyncio.run(main())
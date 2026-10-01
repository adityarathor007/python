# Not blocked by asyncio while the order is being fetched from the background, and logging continues. 
# Once the fetch order completes the program ends and thus the daemon thread needs to stop

import asyncio, threading, time

def background_worker():
    while True:
        time.sleep(1)
        print(f"Logging the system health")
    
async def fetch_orders():
    await asyncio.sleep(3) #fetching the orders data from db
    print("order fetched")


threading.Thread(target=background_worker,daemon=True).start() 
asyncio.run(fetch_orders())


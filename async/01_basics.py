#async develops a coroutine, which is a special function that can be paused 
#await, the fn needs to be async, and its task to pause the execution untill the result is ready 
# so you gracefully wait for somethings to happens while you serve/do other task as well 

#asyncio is a library that provides the above functionality
#Event loop: the engine that runs and schedules co-routine, so when a coroutine waits and completes the work this brings that function back into execution 

import asyncio 
async def brew_chai():
    print("Brewing chai...")
    await asyncio.sleep(2)
    print("Chai is ready!")

asyncio.run(brew_chai())

# multithreading relies on the OS to constantly switch bw multiple OS-level threads,
# while asyncio.gather uses a single thread managed by a cooperative event loop 

import asyncio

async def brew(name):
    print(f"Brewing {name}...")
    await asyncio.sleep(2)  #its waiting with non blocking fashion
    print(f"{name} is ready...")

async def main():
    await asyncio.gather(
        brew("Masala chai"),
        brew("Green chai"),
        brew("Ginger chai"),
    )


asyncio.run(main())
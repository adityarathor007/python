import asyncio, aiohttp
#with keyword ensures files and connections close safely even if error occurs

async def fetch_urls(session, url):
    # for asynchrnous context managers (async with) -> allows the program to perform no blocking operations while entering and exiting the code block 
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")


async def main():
    urls=["https://httpbin.org/delay/2"]*3
    async with aiohttp.ClientSession() as session:
        tasks=[fetch_urls(session, url) for url in urls]
        await asyncio.gather(*tasks) #shorthand notation for unpacking things 


asyncio.run(main())
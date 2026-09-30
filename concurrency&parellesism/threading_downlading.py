import time
import threading
import requests

def download(url):
    print(f"Starting download from {url}")
    resp=requests.get(url)
    print(f"Finished downloading from {url}, size: {len(resp.content)} bytes")

urls=[
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/svg",
    "https://httpbin.org/image/png"
]

start=time.time()
threads=[]

for url in urls:
    t=threading.Thread(target=download,args=(url,))
    t.start()
    threads.append(t)


for t in threads:
    t.join()

end=time.time()

print(f"all downloads completed in {end-start} secs")
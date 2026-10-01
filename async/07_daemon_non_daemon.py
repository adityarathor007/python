import threading, time

def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temperature...")
        time.sleep(2)

# threading.Thread(target=monitor_tea_temp,daemon=True).start()
# print("Main program done")


#for non-deamon (continously run even if the main thred completes)
threading.Thread(target=monitor_tea_temp).start()
print("Main program done")


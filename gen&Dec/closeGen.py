def chai_stall():
    
    try:
        while True:
            order = yield "Waiting for chai order"
            print(f"Preparing {order}")
    except:
        print("Stall closed, no more chai")

stall = chai_stall()
print(next(stall))
stall.send("Masala Chai")
stall.send("Masala Corn")
#.close injects a generatorExit and terminate generator
stall.close() #its better to clean it yourself rather than cleaned by garabageCollector
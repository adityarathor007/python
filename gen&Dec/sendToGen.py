def chai_customer():
    print("Wlcm ! What chai would you like to have ?")
    order=yield #after the generator starts it wait for some data to come in and when it comes it moves forward
    while True:
        print(f"Preparing: {order}")
        order=yield #again it waits for new data to come in


stall=chai_customer()
next(stall) #start the generator

stall.send("Masala Chai")
stall.send("Lemon Chai")

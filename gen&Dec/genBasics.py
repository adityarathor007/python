# yield keyword is used to convert standard function into a generator function
# instead of returning a single value and terminating a function entirely like a return, it pauses the function and saves the state

# when the function is called again, it resumes execution exactly where it was paused 

def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Elachi Chai"


stall=serve_chai() #stall is just sotring the reference to the generator 
print(stall)

print(next(stall))
print(next(stall))
print(next(stall))
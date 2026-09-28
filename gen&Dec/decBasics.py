def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper
    

@my_decorator # IMP: this does this -> greet=my_decorator(greet) 
def greet():
    print("Hello from decorator class")

greet() #so when we call it we are actually calling the wrapper func
print(greet.__name__) #it will print wrapper

#we can prserve the name by using wraps from functools
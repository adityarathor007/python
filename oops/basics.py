class Car:
    origin="Germany"
    def describe(self):
        print(f"This is car's origin is from {self.origin}")



# 1. Basic IMPL
# print(Car.origin)
# tesla=Car()
# tesla.origin="USA"
# print("Class origin: ", Car.origin)
# #each object has its own namespace that doesnt interfer with others
# print("Tesla origin: ", tesla.origin)


# 2. Attribute shadowing (will fallback to the attribute of the class if present)
# del tesla.origin
# print(tesla.origin)

# tesla.top_speed=120
# del tesla.top_speed 
# print(tesla.top_speed) #this will give error



# 3. Self argument
mercedes=Car()
tesla=Car()
tesla.origin="USA"
mercedes.describe() #internally it does this Car.describe(Mercedes)
tesla.describe() #changes in the attributes does not affect others objects attributes 
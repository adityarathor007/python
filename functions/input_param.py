# its always pass by object reference
# def prepare_dish(food="None",arr): #all the variable in the function defination is called parameter. ANd one of them has a default value
#     print(f"preparing: {food}")
#     food="burger"  #since it is immutable so any modification that is made changes the object and the local scope reference starts pointing it
#     arr[1]=1 #but since this is mutable the same object is changed and since both the local and global scope are pointing to the changes are visible

# food="pasta"
# arr=[1,2,3]
# prepare_dish(food,arr)  #here whatever you pass is argument (this is positional argument)
# print(food)
# print(arr)


#keyword arguments
# def fun(v1,v2):
#     print(f"{v1} , {v2}")

# fun(v2=1,v1=3)


#args and kwargs
def fun(*args, **kwargs):
    print("the args are: ", args) #it creates a tuple of all the argument values    
    print("the kwargs are: ",kwargs) #it creates a dictionary


fun(1,2,3,v1=4,v2=5)
#statement (it assigns a value but doesnt return anything)
x=10

#expresion (something that retusn a value): 3+3


#so walrus is called assignment expressino operator

value=13
if remainder := value%5:
    print(f"Not divisble, remainder is: {remainder}")


avial_size=["S","M","L"]
if(requested_size := input("Enter your size")) in avial_size:
    print(f"Yes this size: {requested_size} is in stock")
else 
    print("Size not in stock")




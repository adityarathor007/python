# #by default starts with 0 and ends at e-1   
# for digit in range(10): 
#     print(f"Digit: {digit}")


# #using enumerate (can also specify the starting i)
cars=["mercedes","rangeRover","Mclaren"]
# for i,c in enumerate(cars,start=1):
#     print(f"{i}: {c}")


#using zip
# models=["E class","Evoque","720s"]
# for car,model in zip(cars,models):
#     print(f"{car} {model}")

# break, continue keyboard  
staff=[("Amit",14),("Zara",12),("Aditya ",22)]
for name,age in staff:
    if age>=22:
        print(f"{name} is eligible to maage the staff")
        break
else:
    print("no one is eligible")
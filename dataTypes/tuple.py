#tuple  -> means bracket
cars=("Mercedes","RangeRover","Mclaren")
(c1,c2,c3)=cars
print(f"{c1} {c2} {c3}")

#check if exist in tuple
if('Mercedes' in cars):
    print("Mercedes is present in car collection")

#its immutable thus on using the + operator it creates new tuple
cars=cars+("Ferrari",);
print(cars)
#set->{} 

cars={"mercedes","rangeRover","mclaren"};
cars_2={"ferrari","rollsRoyce","mclaren"};

# union operation
# all_cars=cars|cars_2
# print(all_cars)

# intersection 

# most_loved=cars & cars_2
# print(most_loved)

#rmove the one which is intersecting 
others=cars-cars_2
print(others)

#membership check
print(f"Is mercedes in optional cars? {'mercedes' in others}")


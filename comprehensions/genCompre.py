# (expression for item in iterable if condition)

# parethesis create a generator when they contain a for loop inside them
daily_sales=[5,8,10,12,7,3,8,9,15]
total_cups=(sale for sale in daily_sales if sale>5)
# print(total_cups) #it gives a generator object which yields as per requirement

# print(next(total_cups))
# print(next(total_cups))
# print(next(total_cups))
# print(next(total_cups))

#if want to print wihtout using next 
for cup in total_cups:
    print(cup, end=", ")

print("")    

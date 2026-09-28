def find_total(cups,unit_price):
    return cups*unit_price

#multiple return values
def report():
    return 100,2 

# print(find_total(3,15))

sold,remaining=report()
print(f"{sold},{remaining}")
def process_order(item,quantity):
    try:
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be a number")
        price={"masala": 20}[item] #creating the dictionary and then accessing the item
        cost=price*quantity
        print(f"total cost is {cost}")
    except KeyError:
        print("Sorry the chai flavour not avialalbe")
    except TypeError:
        print("Quantity must be in number")
    

process_order("ginger",2)
process_order("masala","three")
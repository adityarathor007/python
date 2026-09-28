# [ expression for item in iterable if condition ]
menu=[
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger chai"
]


#get list of items that contains Iced in their name
iced_tea=[tea for tea in menu if "Iced" in tea]
print(iced_tea)


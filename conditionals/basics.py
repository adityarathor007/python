class_type=input("Enter the class: ").upper()

if class_type=="A":
    print("economy class")
elif class_type=="E":
    print("the higher variant")
elif class_type=="S":
    print("the premium variant")
else:
    print("invalid input")


is_student=False
#ternery operator
ticket_price=15 if is_student else 30
print(ticket_price)

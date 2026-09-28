#Nutshell: you modify the object does it create a new object, if yes than immutable datatype

#immutable decided by identity not value 
# x=2
# print(id(x))
# x=12
# print(id(x)) #change in address of the object

#mutable (no change in address even after modification of the object )
days=set()
print(id(days))
days.add("Monday")
days.add("Tuesday")
print(id(days))



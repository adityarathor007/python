#list -> [] and are mutable (thus on adding elements new object is not created)
tech_stack=["cpp","java"]

#adding element
tech_stack.append("python")


#printing list
print(tech_stack)

#merge 2 list
framework=["pytorch","springboot"]
# tech_stack.extend(framework)
# alternative for this (operative overloading)
tech_stack=tech_stack+framework
print(tech_stack)

# creating a list with element repeated n times
arr=["abc"]*3
print(arr)


# #insert at index 1
# tech_stack.insert(2,"docker")
# print(tech_stack)


# #removing elemnt
# tech_stack.remove("cpp")
# #removing the lsat element
# stack=tech_stack.pop();
# print(tech_stack)


# #reverse the list
# tech_stack.reverse() 
# print(tech_stack)


# #sorting the list
# tech_stack.sort()
# print(tech_stack)


# #finding max and min in array
# val=[1,2,3,4,5]
# print(max(val))
# print(min(val))


#iterating  a list
for stack in tech_stack:
    print(stack)



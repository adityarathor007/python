# impure fn
#if a fn uses global variables, time or random functions -> has side effect


# lambda fn [lambda arguments: expression]
# square_lambda = lambda x: x ** 2
# print(square_lambda(5))

# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# print(even_numbers)


#buid-in funcs
def fn():
    """Describe the parameters of the functions and what does fucntion actually do""" #this is the doc string
    return 0


print(fn.__doc__)
print(fn.__name__)
#You can use lambda expressions to create anonymous functions. That is, functions that don’t have a name. They are helpful for creating quick functions that aren’t needed later in your code. This can be especially useful for higher order functions, or functions that take in other functions as arguments.

#lambda functions are very similar to array syntax for functions, but they do not have a multi-line scope

#With a lambda expression, this function:
def multiply(x, y):
    return x * y

#can be reduced to:
multiply = lambda x, y: x * y

#Both of these functions are used in the same way. In either case, we can call multiply like this:
multiply(4, 7) #This returns 28.



# --- Quiz --- #
#Lambda with Map
#map() is a higher-order built-in function that takes a function and iterable as inputs, and returns an iterator that applies the function to each element of the iterable.

numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

#def mean(num_list):
 #   return sum(num_list) / len(num_list)

averages = list(map(lambda num_list: sum(num_list) / len(num_list), numbers))
print(averages)


#Quiz: Lambda with Filter
#filter() is a higher-order built-in function that takes a function and iterable as inputs and returns an iterator with the elements from the iterable for which the function returns True.

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

#def is_short(name):
 #   return len(name) < 10

short_cities = list(filter(lambda name: len(name) < 10, cities))
print(short_cities)
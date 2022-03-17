# dictionaries are like dummy objects. it had keys and values, and keys can correspont to different data types
#to access an item in a dictionary squared braces or get() should be used

elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
elements["helium"] #giver an error in case the key does not exist
elements.get("dilithium") #returns None  in case the key does not exist
elements.get('kryptonite', 'There\'s no such element!') #returns  a default value in case the key does not exist
"There's no such element!"
elements["lithium"] = 3 

print(elements)

#Identity Operators  typechek?

#`is``  evaluates if both sides have the same identity 
#`is not`` #evaluates if both sides have different identities


print("carbon" in elements) #returns boolean


# -- Quiz -- #
# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5}
print(population)


animals = {
    'dogs': [20, 10, 15, 8, 32, 15], 
    'cats': [3,4,2,8,2,4], 
    'rabbits': [2, 3, 3], 
    'fish': [0.3, 0.5, 0.8, 0.3, 1]}

print(animals['dogs'][3])
print(animals['fish'])

#Summary
#A dictionary is a mutable, unordered data structure that contains mappings of keys to values. Because these keys are used to index values, they must be unique and immutable. For example, a string or tuple can be used as the key of a dictionary, but if you try to use a list as a key of a dictionary, you will get an error.
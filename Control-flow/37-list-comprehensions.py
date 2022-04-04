#lists comprehension seems to be a very complex version of the spread operator used to create an array from a new set...
# using list comprehension makes the code much shorter when a new list must be refurned from a for loop after a modification in itself
#basically this:
from itertools import count


cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())

#becomes this:
capitalized_cities = [city.title() for city in cities]

#capitalized_cities: is the variable where the new list will be stores
#[]: represents that a new list will be created
# city.title() : gets ieach item, in this case city, ans modifies it to be returned to the array
# for city in cities: makes the for loop into cities


#Conditionals

#in case an element in the array should be returned ONLY if a certain condition is met, the simples way to implementing it is to add an if statemenr in the end of the [] structure:

squares = [x**2 for x in range(9) if x % 2 == 0]

#in case the item must be manipulated also in the else of the condition, the whole condition will be moved to before the for loop line this:
squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]

# --- Quiz --- #

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split(' ')[0].lower() for name in names]
print(first_names)

#multiples_3 =  [num for num in range(1, 20*3 + 1) if num % 3 == 0]

multiples_3 =  [x*3 for x in range(1, 21)]
print(multiples_3)


scores = {
    "Rick Sanchez": 70,
    "Morty Smith": 35,
    "Summer Smith": 82,
    "Jerry Smith": 23,
    "Beth Smith": 98
}

passed = [score[0] for score in scores.items() if score[1] >= 65]
print(passed)
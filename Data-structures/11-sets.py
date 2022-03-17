#sets has the same concept of sets in JS

#sets are mutable and unordered type of container

common_last_names = ['souza', 'silva','andrade','figueiredo','pereira', 'souza','sousa','santos', 'andrade']

last_names_set = set(common_last_names)
print(last_names_set)
print(len(last_names_set))

last_names_set.add('macedo') #use add instead of append in sets

print(last_names_set)

last_names_set.pop() #removes a random item from the set
print(last_names_set)

#as an advantage, sets are much faster than lists and giver better support to other mathematical sets, such as union, intersection etc
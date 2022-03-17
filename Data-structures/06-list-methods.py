number_list = [0,3832,942,385,2849,342,32]
str_list = ['tired', 'cansada', 'trött']
mixed_List = [True, False, 2342,32, 'sdas']

# As lists are mutable, assigning an arrray to another variable and modifying the original array will reflect in the variable that does a reference to thar.
numeric_list = number_list
number_list[2] = 500
print(number_list)
print(numeric_list)


#the min() and max() functions works in lists that contains one object type, for example only string or numbers, for strings the min and max will be related to the alphabetical order
print(min(number_list))
print(max(number_list))
print(min(str_list))
print(max(str_list))


# the sorted() method creates a sorted version of the list, with asc way, if desc wants to be used, reverse=True can be passed as second parameter

print(sorted(number_list))
print(sorted(number_list, reverse=True))
print(sorted(str_list))
print(sorted(str_list, reverse=True))

#TypeError: '<' not supported between instances of 'str' and 'int'
#print(sorted(mixed_List))


#Join
#the join() method works different in python as it does in JS, it joins a list from the separator as a string, and it can only join string typed lists

print('-'.join(str_list))

#append
print(number_list.append(50))
print(number_list)
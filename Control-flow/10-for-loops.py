cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
#iterable can be a string, list, tuple, dictionaries and files
# iterating in a for...in loop:
for city in cities:
    print(city.title())
print("Done iterating!")

# creating a new list:
capitalized_cities = [] 
for city in cities:
    capitalized_cities.append(city.title())

print('New list created based on iteration:', capitalized_cities)

# the range() built-in function creates a range of numbers it receives the integer params start, stop and step, it works in the same way as the for(start, condition to stop, iterator), but it returns a the first and last generated number (or indexes if you want to simplify it) based on the step...
#start is inclusive, and stop is not inclusive
#the range function has 0 a default star and 1 as default step, then only stop needs to be passed:

print(range(4)) # range object is printed

# a list can be created by using the list constructor:
print(list(range(4))) # translates to: start = 0, stop = 4-1 and step = 1

#only start and stop can also be passse to use the desault step:
print(list(range(2, 6))) # translates to: start = 2, stop = 6-1 and step = 1


# or all parameters can be passed as in
print(list(range(1, 10, 2))) # translates to: start = 1, stop = 10-1 and step = 2


#the range function can be used in combination with the for loop in order to generate the range values and use them as indexes.

cities_length = len(cities)
#using rande with the index is the only way to modify a list
for index in range(cities_length): #the range does the same as len(cities)-1
    cities[index] = cities[index].title() #actually modifies the list

print(cities)


sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

# Write a for loop to print out each word in the sentence list, one word per line

for word in sentence:
    print(word)

# Write a for loop using range() to print out multiples of 5 up to 30 inclusive
for num in range(5,31,5):
    print(num)

# -- QUiz -- #

#Create Usernames

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    usernames.append(name.replace(' ', '_').lower())

print(usernames)


#Modify Usernames with Range

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for i in range(len(usernames)):
    usernames[i] = usernames[i].replace(' ','_').lower()


print(usernames)

 #Tag Counter

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    if token.startswith('<') and token.endswith('>'):
        count += 1

print(count)

#Create an HTML List

items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    html_str += '<li>{}</li>\n'.format(item)

html_str += '</ul>'

print(html_str)
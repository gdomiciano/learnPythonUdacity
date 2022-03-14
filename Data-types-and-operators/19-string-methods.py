from sqlite3 import Date


name = 'Geiseany Domiciano'
my_string = 'my own string'

#methods

print('capitalize() =>', my_string.capitalize())
print('casefold() =>', name.casefold())
print('center() =>', my_string.center(20))
print('count() =>', name.count('a'))
print('encode() =>', my_string.encode())
print('endswith() =>', name.endswith('y'))
print('expandtabs() =>', my_string.expandtabs())
print('find() =>', name.find('e'))
print('format() =>', my_string.format())
print('format_map() =>', name.format_map(' '))
print('index() =>', my_string.index('i'))
print('isalnum() =>', name.isalnum())
print('isalpha() =>', my_string.isalpha())
print('isdecimal() =>', name.isdecimal())
print('isdigit() =>', my_string.isdigit())
print('isidentifier() =>', name.isidentifier())
print('islower() =>', my_string.islower())
print('isnumeric() =>', name.isnumeric())
print('isprintable() =>', my_string.isprintable())
print('isspace() =>', name.isspace())
print('istitle() =>', my_string.istitle())
print('isupper() =>', name.isupper())
print('join() =>', my_string.join(['o','u']))
print('ljust() =>', name.ljust(20))
print(Date.today().year)

#print(13.37.islower())

# Format
print('I am turning {} years old in {}!'.format(Date.today().year - 1993, Date.today().year))


#split
print(my_string.split())
print(name.split('i'))
print(my_string.split(None, 1))
print(name.split('i', 2))
print()

# -- Quiz -- #
# What is the length of the string variable verse?
# What is the index of the first occurrence of the word 'and' in verse?
# What is the index of the last occurrence of the word 'you' in verse?
# What is the count of occurrences of the word 'you' in the verse?
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)
print()
# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!
answer = "The verse length is {}, The word 'and' occurrs first at index {}, the word 'you' last at index {} and {} times in total"
verse_length = len(verse)
first_and = verse.find('and')
total_you = verse.count('you')
last_you = verse.rfind('you')

print(answer.format(verse_length,first_and, last_you, total_you))
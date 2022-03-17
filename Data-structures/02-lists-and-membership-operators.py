#container of data
#list have 0 based index and behave as an array in javascript
list_sample = ['a', 2, 3.5, False]
list_length = len(list_sample)
print(list_length)

#slicing notation
#first is inclusive and second is exclusive?
middle = list_sample[1:2] #index : amount
first_half = list_sample[:2] #shortcut to 0 untill index 2
last_half = list_sample[3:] #shortcut to index until -1
print(middle, first_half, last_half)

#membership operators
#both ìn`and `not in`operators can be used with strings and containers of data
name = 'Geiseany Domiciano'
print('is' in name)
print('bra' not in name)
print(True in list_sample)
print(False not in list_sample)

# Lists are mutable and ordered (depend on index)
list_sample[0] = 'mutable'
print(list_sample)

# Strings are imutable and ordered
#TypeError: 'str' object does not support item assignment
#name[-1] = 'o Bispo '
print(name)

# -- Quiz -- #

month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month
num_days = days_in_month[month+1]

print(num_days)


eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])
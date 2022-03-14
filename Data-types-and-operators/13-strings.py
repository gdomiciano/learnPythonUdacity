# multiplu *, can multiply a work by the number passed to it
print(' hello' * 5)

#divition and subtract do not work with strinf, while plus is used to concatenate like in JS

# len() is used to return the lenfth of an object (strings included)
udacity_length = len('Udacity')
print(udacity_length)

# -- QUIZ -- #
username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."
print(username + ' accessed the site ' + url + ' at ' + timestamp + '.')


given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"
full_name = given_name + ' ' + middle_names + ' ' + family_name
name_length = len(full_name)

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)

len(835)
# functions declarations require the def keywork, followed by the function name (same rules as variables apply) followed by parenthesis with or without parameters and :

#inside the function any added variable is valid only inside that scope, and can be used pretty much in the same way as we do it in JS

#  a function may or may not return a value from it based on the usage of thr return keyword

from xmlrpc.client import DateTime


def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2

#python allows default parameer by using an assignment on the function parameter definition:
def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2


# it is also possible to call a function by passing its parameters, by name or by position

cylinder_volume(10, 7)  # pass in arguments by position
cylinder_volume(height=10, radius=7)  # pass in arguments by name


# --- Quiz --- #

# write your function here

def population_density(population, land_area):
    return population / land_area


# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))



# write your function here
def readable_timedelta(days):
    weeks = days // 7 
    remaining_days = days % 7
    return '{} week(s) and {} day(s).'.format(weeks, remaining_days)
    
# test your function
print(readable_timedelta(10))
# in most of the cases scope in python is the same as in JS, however the two programming languages deal with global variables differently

#in case a function wants to change the value of a global variable, then the return of the function must be assigned to the variable in question, otherwise ´UnboundLocalError´ will be thrown

#wrong
egg_count = 0

def buy_eggs():
    egg_count += 12 # purchase a dozen eggs

buy_eggs()

#right
egg_count = 0

def buy_eggs(count):
    return count + 12  # purchase a dozen eggs

egg_count = buy_eggs(egg_count)
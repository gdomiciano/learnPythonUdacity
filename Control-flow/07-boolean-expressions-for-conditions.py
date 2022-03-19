#python seems to have a better wau to double check an condition in a shorter version than JS:

height = 1.67
weight = 66.5
bmi = weight/height**2

 # in JS it would be (bmi <= 18.5 && bmi < 25)
if 18.5 <= bmi < 25:
    print('BMI is considered normal')

#bad boolean check examples:
is_cold = True

if is_cold or not is_cold:
    print('should not use or and not together like this, since not behaves like the !')
weather = 'snow'
if weather == 'snow' or 'rain':
    print('this is not a boolean comparisson, but a boolean comparisson and a string')
    print("the correct if should be `weather == 'snow' or weather == 'rain'` then it is 2 boolean conditional statements being evaluated")

# None, False, 0 and empty sequences or collections evaluates to false, otherwise true, same as in js

# -- Quiz -- #

points = 190  # use this as input for your submission
# establish the default prize value to None

prize = None

# use the points value to assign prizes to the correct prize names
# if points >= 1 and points <= 50:
#     prize = 'wooden rabbit'
# elif points >= 151 and points <= 180:
#     prize = 'wafer-thin mint'
# elif points >= 181 and points <= 200:
#     prize = 'penguin'

if 1 <= points <= 50:
    prize = 'wooden rabbit'
elif 151 <= points <= 180:
    prize = 'wafer-thin mint'
elif points <= 200:
    prize = 'penguin'

# use the truth value of prize to assign result to the correct prize
if prize:
    result = 'Congratulations! You won a {}!'.format(prize)
else:
    result = 'Oh dear, no prize this time.'


print(result)
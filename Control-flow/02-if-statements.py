
# if statement, in python the if statement is followed by the condition and the `:` sign is the one that ' finalizes'  the condition part, then everything that is indented after that line is going to execute if the condition is met

phone_balance = 4
bank_balance = 50
print('before', phone_balance, bank_balance)

if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10

print('after', phone_balance, bank_balance)

#else is used backing the indetention followed by the `:`

# elif is the keyword shorteen version of a else if and it is followed by an condition and `:`

season =  'spring'

if season == 'spring':
    print('plant the garden!')
elif season == 'summer':
    print('water the garden!')
elif season == 'fall':
    print('harvest the garden')
elif season == 'winter':
    print('stay indoors!')
else:
    print('unrecognized season')


#indentation is very important as a block statement, there are no curly braces to signal it

# -- Quiz -- #

points = 4  # use this input to make your submission

# write your if statement here
if points >= 1 and points <= 50:
    result = 'Congratulations! You won a {}!'.format('wooden rabbit')
elif points >= 151 and points <= 180:
    result = 'Congratulations! You won a {}!'.format('wafer-thin mint')
elif points >= 181 and points <= 200:
    result = 'Congratulations! You won a {}!'.format('penguin')
else:
    result = 'Oh dear, no prize this time.'

print(result)


# '''
# You decide you want to play a game where you are hiding 
# a number from someone.  Store this number in a variable 
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 50
guess = 50

if guess < answer:
    result = "Oops!  Your guess was too low."
elif guess > answer:
    result = "Oops!  Your guess was too high."
elif guess == answer:
    result = "Nice!  Your guess matched the answer!"

print(result)

# '''
# Depending on where an individual is from we need to tax them 
# appropriately.  The states of CA, MN, and 
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and 
# the corresponding state to assure that they are taxed by the right
# amount.
# '''
#Either CA, MN, or NY
state = 'NY'
purchase_amount = 10

if state == 'CA':
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'MN':
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'NY':
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)
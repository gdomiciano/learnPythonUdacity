# type check
from calendar import week


print(type(633))
print(type('633'))
print(type(633.0))
print(type(True)) #boolean type is capitalized, super weird

# type conversion

print(str(10))
print(int(7.5))
print(int('15'))
print(float(20))
print(float('25'))

#playing with types

print('0' + '5')# "05"
print(0 + 5) # 5
#print('0' + 5) # TypeError: can only concatenate str (not "int") to str
#print(0 + '5')# TypeError: can only concatenate str (not "int") to str


# -- QUIZ -- #

mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"
week_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.

print("This week's total sales: ", str(week_sales))
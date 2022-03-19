# while loop structure/syntax
# number to find the factorial of
from unittest import result


number = 6   

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while current <= number:
    # multiply the product so far by the current number
    product *= current
    
    # increment current with each iteration until it reaches number
    current += 1

# print the factorial of number
print(product)

# -- Quiz -- #

start_num = 0 #provide some start number
end_num = 29 #provide some end number that you stop when you hit
count_by = 3 #provide some number to count by 
break_num = start_num
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
while break_num <= end_num:
    break_num += count_by

print(break_num)

start_num = 40
# write a condition to check that end_num is larger than start_num before looping
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num

if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."
else:
    while break_num <= end_num:
        break_num += count_by
    result = break_num  

print(result)


limit = 40
root = 2
nearest_square = 0
# write your while loop here
while root*root < limit:
    nearest_square = root*root
    root += 1

print(nearest_square)



num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
odd_num = []
index = 0
while len(odd_num) <= 5 :
    if num_list[index] % 2 != 0:
        odd_num.append(num_list[index])
    index += 1

print(sum(odd_num))
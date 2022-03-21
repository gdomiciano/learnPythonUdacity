#break stops the loop all together at any point
#continue allows the loop to skip a specific alterarion until it goes to the next one

from typing import no_type_check


manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking loop now!")
        break
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit
print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))


# -- Quiz -- #

# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here
# for headline in headlines:
#     if len(news_ticker) >= 140:
#         print('break the loop', len(news_ticker))
#         break
#     elif (len(news_ticker) + len(headline)) >= 140:
#         print('try next', len(news_ticker))
#         continue
#     else:
#         news_ticker += headline
#     news_ticker += ' '
# last = headlines[-1]

# print('last', last)
# if len(news_ticker) < 140:
#     for i in range(len(last)):
#         if(len(news_ticker) < 137):
#             news_ticker += last[i]
#         else:
#             news_ticker += '...'
#             break


# print(news_ticker, len(news_ticker) )

for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)



## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor

for number in check_prime:
    factors=[]
    if number % 2 == 0:
        factors.append(str(2))
    if number % 3 == 0:
        factors.append(str(3))
    if number % 5 == 0:
        factors.append(str(5))

    if len(factors):
        factors_str = ', '.join(factors)
        print('{} is NOT a prime number, because {} is a factor of {}'.format(number, factors_str, number))
    else:
        print('{} Is a prime number'.format(number))
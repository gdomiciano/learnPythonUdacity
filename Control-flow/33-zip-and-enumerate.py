#zip returns an iterator that combines multiple iterables into one sequence of tuples. Each tuple contains the elements in that position from all the iterables. 

print(list(zip(['a', 'b', 'c'], [1, 2, 3])))


#unpack each tuple

letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))



# unzip a list into tuples
some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)

#enumerate is a built in function that returns an iterator of tuples containing indices and values of a list.

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)


# -- Quiz -- #
#Quiz: Zip Coordinates
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = list(zip(labels, x_coord, y_coord, z_coord))

# write your for loop here
for i in range(len(points)):
    label, x, y, z = points[i]
    points[i] = '{}: {}'.format(label, str(x) + ', ' + str(y) + ', ' + str(z))


for point in points:
    print(point)


#Quiz: Zip Lists to a Dictionary
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print(cast)

#Quiz: Unzip Tuples
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))
print()
# define names and heights here
names, heights = list(zip(*cast))

print(names)
print(heights)


data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
# input
# 0,  1,  2               0, 3, 6, 9
# 3,  4,  5               1, 4, 7, 10
# 6,  7,  8               2, 5, 8, 11
# 9, 10, 11

unziped = list(zip(*data))
print(unziped.transpose())
# data_transpose = list(zip(data, list(range(4))))[0][:-1]
data_transpose = zip(unziped)
print(data_transpose)


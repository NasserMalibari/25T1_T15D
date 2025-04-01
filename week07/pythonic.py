#!/usr/bin/env python3


# Looping over a collection 

colors = ['red', 'green', 'blue', 'yellow']

n = len(colors)
# for i in range(n):
#     print(colors[i])

# for color in colors:
#     print(color)

# ####################


# Looping backwards

colors = ['red', 'green', 'blue', 'yellow']
# for color in reversed(colors):
#     print(colors)


# Looping with index
#######################

colors = ['red', 'green', 'blue', 'yellow']
# for i, color in enumerate(colors):
#     print(f"{i}, {color}")


names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

# n = min(len(names), len(colors))
# for i in range(n):
#     print (names[i], '--->', colors[i])

for name, color in zip(names, colors):
    print(name, color)



colors = ['red', 'green', 'blue', 'yellow']

# # Forward sorted order
# for color in sorted(colors):
#     print(color)


# # Backwards sorted order
# for color in sorted(colors, reverse=True):
#     print(color)


# # Multiple exit points in a loop

def find(seq, target):

    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i

    # found = False
    # for i, value in enumerate(seq):
    #     if value == target:
    #         found = True
    #         break
    # if not found:
    #     return -1
    # return i

# list1 = [1, 3, 5]
# target = 3
# print(find(list1, target))



# ###### DICTIONARIES ##############################

d = {'a': 1, 'b': 2, 'c': 3}

# loop through keys
for k in d:
    print(k)

# loop through item (pairs)
for key, item in d.items():
    print(key, item)


# # construct from pairs
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue']

pair_dic = dict(zip(names, colors))
print(pair_dic)

# # COUNTING WITH DICTIONARIES

my_list = ['a', 'b', 'c', 'a', 'c', 'a']
# {'a': 3, 'b': 1, 'c': 2}
counter = {}
for character in my_list:
    if character in counter:
        counter[character] += 1
    else:
        counter[character] = 1
# # print(counter)
# for character in sorted(counter):
#     print(f"{character}: {counter[character]}")
#     # s = character + ":" + counter[character]


# from collections import default_dict, Counter

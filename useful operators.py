# for x in range(3, 11, 3):
#     print(x)
# print(range(5))
# print(list(range(1,6)))

# letter_index = 0
# my_string = 'sbdjcbklksd'
# for letter in my_string:
#     print(letter + ' is at index' + str(letter_index))
#     letter_index += 1

# my_string = 'sbdjcbklksd'
#
# for index, letter in enumerate(my_string):
#     print(letter + ' is at index ' + str(index))

# letter_list = ['a', 'b', 'c', True]
# print(True in letter_list)

# dict_1 = {1: 'a', 2: 'b', 3: 'c'}
# print('a' in dict_1.values())
# print(1 in dict_1.keys())

# print(min(1, 3, 56, 4))
# print(max(1, 3, 56, 4))
#
# my_list = [1, 3, 56, 4]
# print(min(my_list))
# print(max(my_list))
#
# print(max('Hello'))
#
# for letter in 'Hello':
#     print(ord(letter))

from random import shuffle

my_list = [1, 3, 56, 4]
shuffle(my_list)
print(my_list)

from random import randint
print(randint(1, 10))

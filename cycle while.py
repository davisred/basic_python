# x = 5

# while x >= 1:
#     print(x)
#     x = x - 1

# while x < 10:
#     print(x)
#     x += 1

# while x < 10:
#     print(x)
#     x += 2
# print('Next code')

# x = 0
# while x < 10:
#     print('x is {}. That less than 10'.format(x))
#     x += 1
# else:
#     print('x is {}. That more or equal than 10'.format(x))
#
# for x in range(10):
#     print('x is {} less than 10'.format(x))
# else:
#     x += 1
#     print('x is {}. That more or equal 10'.format(x))

# break. continue, pass

my_list = [1, 2, 3]

# for item in my_list:
#     pass
# print('Another code')

# for item in my_list:
#     if item == 2:
#         break
#     print(item)
# print('Another code')

for item in my_list:
    if item == 2:
        continue
    print(item)
print('Another code')
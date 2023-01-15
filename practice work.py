# Задача 1
#
# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
#
# Выведите все элементы, которые меньше 5.

b = []
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for numbers in a:
    if numbers < 5:
        b.append(numbers)
print(b)


# Задача 2
#
# Даны списки:
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
#
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
#
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# вариант исключит повторения:
print(list(filter(lambda numbers: numbers in a, b)))
# без исключения повторений:
print(list(numbers for numbers in a if numbers in b))


# Задача 3
#
# Отсортируйте словарь по значению в порядке возрастания и убывания.

import operator

dictionary = {
    'December': 12, 'March': 3, 'September': 9,
    'May': 5, 'January': 1, 'June': 6}
print(dict(sorted(dictionary.items(), key=operator.itemgetter(1))))
print(dict(sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)))

# Задача 4
#
# Напишите программу для слияния нескольких словарей в один.

# 1

time_of_the_year = {
    'winter': ['december', 'january', 'february'],
    'spring': ['march', 'april', 'may'],
    'summer': ['june', 'july', 'august'],
    'fall': ['september', 'october', 'november']}
join = dictionary | time_of_the_year
print(join)

# 2

result = {}
for i in (dictionary, time_of_the_year):
    result.update(i)
print(result)

# 3
result_1 = {**dictionary, **time_of_the_year}
print(result_1)


# Задача 5
#
# Найдите три ключа с самыми высокими значениями в словаре
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}.

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}

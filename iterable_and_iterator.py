# number_list = [1, 2, 3, 4]
# for number in number_list:
#     print(number)
#
# for letter in 'my string':
#     print(letter)
#
# number_list_iterable = iter(number_list)
# print(number_list_iterable)
# print(type(number_list_iterable))
#
# string_iterator = iter('my string')
# print(type(string_iterator))
# print(number_list_iterable.__next__())
# print(next(number_list_iterable))

def my_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator.__next__())
        except StopIteration:
            print('Iteration is finished')
            break
my_for_loop('hello')
my_for_loop([1, 2, 3, 4])
# def my_function(x):
#     return x
# print(my_function(5))

# def count_up_to(x):
#     count = 1
#     while count <= x:
#         yield count
#         count += 1

# print(count_up_to(4))
# counter = count_up_to(4)
# print(counter.__next__())
# print(counter.__next__())
# print(counter.__next__())
# print(counter.__next__())
# print(counter.__next__())
# while True:
#     print(next(counter))
#     break

# counter = count_up_to(10)
# for number in counter:
#     print(number)

# counter.__next__()

# for number in counter:
#     print(number)
week_day = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}

def count_up_to(day_list):
    day_list.keys = 1
    while day_list.keys <= 7:
        yield day_list.keys
        day_list.keys += 1
current = count_up_to(week_day())
print(current.__next__())
print(current.__next__())
print(current.__next__())

#
# current_day = get_week_day(week_day)
# print(current_day.__next__())
# print(current_day.__next__())
# print(current_day.__next__())
# print(current_day.__next__())
# print(current_day.__next__())
# print(current_day.__next__())

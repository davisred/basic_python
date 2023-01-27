#
#
# # def get_week_days():
# #     count = 1
# #     week_day = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}
# #     while count <= max(week_day.keys()):
# #         current_day = week_day[count]
# #         yield current_day
# #         count += 1
#
# def get_week_day():
#     week = [
#         "Sunday",
#         "Monday",
#         "Tuesday",
#         "Wednesday",
#         "Thursday",
#         "Friday",
#         "Saturday",
#     ]
#     for day in week:
#         yield day
#
# current_day = get_week_day()
# print(current_day.__next__())
# print(current_day.__next__())
# print(current_day.__next__())
# print(current_day.__next__())
# print(current_day.__next__())
# print(current_day.__next__())
# print(current_day.__next__())

# def even_odd():
#     for number in range(2, 100):
#         yield number
#
# even_odd_generator = even_odd()
#
# print(next(even_odd_generator))  # 'even'
# print(next(even_odd_generator))  # 'odd'
# print(next(even_odd_generator))  # 'even'
# print(next(even_odd_generator))  # 'odd'

def even_odd():
    string = 'even'
    while True:
        yield string
        if string == 'even':
            string = "odd"
        else:
            string = "even"

even_odd_generator = even_odd()

print(next(even_odd_generator))
print(next(even_odd_generator))
print(next(even_odd_generator))
print(next(even_odd_generator))

# from functools import wraps
#
# def hello_from_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         wrapper_text = f'{func(*args, **kwargs)} Hello from decorator!'
#         return wrapper_text
#     return wrapper
#
# @hello_from_decorator
# def my_data(first_name, last_name, age):
#     my_data_text = f'My name is {first_name} {last_name}. I\'m {age} years old.'
#     return my_data_text
#
# print(my_data('Davis', 'Redfield', 35))


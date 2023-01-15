# def ten_percent_of_product(x, y, z):
#     return (x * y * z) * 0.1
#
# print(ten_percent_of_product(10, 20, 70, 2))

# def ten_percent_of_product_with_args(*args):
#     product = 1
#     for number in args:
#         product = product * number
#     return product * 0.1
#
# print(ten_percent_of_product_with_args(10, 20, 2, 1, 4, 345))

# def percent_of_product_with_args(percent, *args):
#     product = 1
#     for number in args:
#         product = product * number
#     return product / 100 * percent
#
# print(percent_of_product_with_args(20, 10, 20, 2, 1, 4, 345))
# dict = {'first': 1, 'second': 2, 'third': 3}
# def func_with_kwargs(**kwargs):
#     print(kwargs)
#
# func_with_kwargs(first=1, second=2, third=3)

# def hello_with_kwargs(**kwargs):
#     if "name" in kwargs:
#         print('Hello! Nice to meet you, {} '.format(kwargs['name']) )
#     else:
#         print('Hello! What is your name?')
# hello_with_kwargs(gender = "male", age = 35, name = 'Vadim')
# hello_with_kwargs(gender = "male", age = 35)

# def hello_with_greeting_and_kwargs(greeting, **kwargs):
#     if "name" in kwargs:
#         print('{} Nice to meet you, {} '.format(greeting, kwargs['name']) )
#     else:
#         print('{} What is your name?'.format(greeting))
# hello_with_greeting_and_kwargs('Hello!', gender = 'male, age = 35', name = 'Vadim')
# hello_with_greeting_and_kwargs('Good morning!', gender = 'male, age = 35', name = 'Vadim')

def func_with_args_and_kwargs(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['sex']))

func_with_args_and_kwargs(5, 6, 'vadim', drink='coffee', sex='male')
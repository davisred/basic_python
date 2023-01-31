from functools import wraps

def print_args(func):
    '''
    This function printing arguments of decorated function
    :param func:
    :return:
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'args : {args}')
        print(f'kwargs: {kwargs}')
        return func(*args, **kwargs)
    return wrapper

@print_args
def my_data(first_name, last_name, age):
    '''
    This function printing string with first name, last name and age of person in format:
    ""Hi, my first name is FIRST NAME, "
          f"my last name is LAST NAME. "
          f"I'm AGE years old""
    :param first_name:
    :param last_name:
    :param age:
    :return:
    '''
    print(f"Hi, my first name is {first_name}, "
          f"my last name is {last_name}. "
          f"I'm {age} years old")

my_data('Davis', 'Redfield', '35')



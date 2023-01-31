from functools import wraps

def prohibit_more_than_2_args(func):
    @wraps(func)
    def wrapper(*args):
        if len(args) < 3:
            return func(*args)
        else:
            raise ValueError("Function must have less than 3 arguments!")
    return wrapper


@prohibit_more_than_2_args
def my_data(first_name, last_name, age):
    return f'My name is {first_name} {last_name}. I\'m {age} years old'


print(my_data('Davis', 'Redfield', '35'))

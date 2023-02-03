from functools import wraps
import time


def sleep(timeout):
    def the_real_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            print(f'There was a pause {timeout} second before execution {function.__name__}')
            time.sleep(timeout)
            return function(*args, **kwargs)

        return wrapper

    return the_real_decorator


@sleep(3)
def some_function(x, y):
    print(f'Hi, {x} {y}!')


some_function('Davis', 'Redfield')
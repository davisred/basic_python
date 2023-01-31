from time import time
from functools import wraps
# start_time = time.time()
# sum([number for number in range(1,100000)])
# end_time = time.time() - start_time
#
# start_time = time.time()
# sum(number for number in range(1,100000))
# end_time = time.time() - start_time

def speed_test(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = function(*args, **kwargs)
        end_time = time()
        print(f'Time of code execution: {end_time - start_time}')
        return result
    return wrapper


@speed_test
def sum_with_list():
    return sum([number for number in range(1,10000000)])


@speed_test
def sum_with_gen():
    return sum(number for number in range(1,10000000))

@speed_test
def product(range_value):
    result = 1
    for number in range(1, range_value):
        result *= number
    return result

print(product(100000))
print(sum_with_gen())
print(sum_with_list())
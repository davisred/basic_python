import time


def sleep(timeout, retry=3):
    def the_real_decorator(function):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < retry:
                try:
                    value = function(*args, **kwargs)
                    if value is None:
                        return
                except:
                    print(f'Сон на {timeout} секунд')
                    time.sleep(timeout)
                    retries += 1

        return wrapper

    return the_real_decorator


@sleep(3, 2)
def some_function(name, name_2):
    print(f'Some {name}, {name_2}')


some_function()

from functools import wraps
from csv import writer, reader


def new_string_csv(func):
    @wraps(func)
    def wrapper(*args):
        print(f'Function {func.__name__} is added data: {args}')
        return func(*args)
    return wrapper


@new_string_csv
def add_student(first_name, last_name, age):
    """
    The function checking data in file before writing  ("if file.tell() == 0").
    If file is empty - headers has been added, after it add user data
    If data in file - header not writing in.
    :param first_name:
    :param last_name:
    :param age:
    :return:
    """
    with open('students.csv', 'a') as file:
        csv_writer = writer(file)
        if file.tell() == 0 :
            csv_writer.writerow(['First name', 'Last name', 'Age'])
            csv_writer.writerow([first_name, last_name, age])
        else:
            csv_writer.writerow([first_name, last_name, age])


def print_students():
    with open('students.csv', 'r') as file:
        csv_reader = reader(file)
        next(csv_reader)
        for string in csv_reader:
            print(string)

add_student(input('Enter your name: '),
            input('Enter your last name: '),
            input('Enter your age: '))
add_student('Dyusha', 'Booblikova', '6')
# print_students()


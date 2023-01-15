# def print_greeting():
#     '''
#     kjlksdlkhfskjdh
#     :return:
#     '''
#     print('Hello')
# print_greeting()
#
# help(print_greeting)

# def print_greeting_with_name(name = 'NoName'):
#     '''
#
#     :param name:
#     :return: None
#     '''
#     print('hello, ' + name + '!')
# print_greeting_with_name('Vadim')

# def sum_of_two_numbers(a = 0, b = 0):
#     '''
#         :param a: The first addend
#         :param b: The second addend
#         :return: Sum of a and b
#     '''
#     return a + b
#
# x = sum_of_two_numbers(1,1)
# x = sum_of_two_numbers(54,19)
# print(x)
# help(sum_of_two_numbers)

# def is_hello_in_text(text):
#     if 'hello'  in text.lower():
#         return True
#     else:
#         return False
# print(is_hello_in_text('Say Hello everyone!'))

# def is_hello_in_text(text):
#     return 'hello' in text.lower()
#
# print(is_hello_in_text('Say Hello everyone!'))

# def is_string_in_text(string, text):
#     return string in text
#
# print(is_string_in_text('he', 'The apple'))


def greeting_depends_of_gender(name, gender):
    if gender == 'male':
        print('Hello, ' + name + '! You look great')
        return gender
    elif gender == 'female':
        print('Hello, ' + name + '! You are so beautiful!')
        return gender
    else:
        print('Hello, ' + name + '! I\'ve never seen the creature like you!')
        return gender


returned_value = greeting_depends_of_gender('Vadim', 'male')
returned_value = greeting_depends_of_gender('Jane', 'female')
returned_value = greeting_depends_of_gender('Shkvarka', 'cmale')
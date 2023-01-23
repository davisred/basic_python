# print('Some code')
# try:
#     print(len(23))
#     print(my_variable)
# except NameError:
#     print('NameError has happen')
# except TypeError:
#     print('TypeError has happen')
# print('Code after error')
user_dictionary = {'first_name': 'Jack', 'last_name': 'White', 'age': 24}
# print(user_dictionary['last_name'])
# print(user_dictionary['name'])
# print(user_dictionary.get('last_name'))
# print(user_dictionary.get('name'))

def get_dictionary_value(dictionary, key):
    '''
    if dictionary haven't specified key, the function returns None
    :param dictionary:
    :param key:
    :return:
    '''

    try:
        return dictionary[key]
    except KeyError:
        return None

print(get_dictionary_value(user_dictionary, 'age'))
print(get_dictionary_value(user_dictionary, 'a'))
print(get_dictionary_value(user_dictionary, 'first_name'))
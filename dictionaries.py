# car_prices = {'opel': 5000, 'toyota': 7000,
#               'bmw': 10000}
# print(car_prices)
# print(car_prices['toyota'])
# car_prices['mazda'] = 4000
# print(car_prices)
# del car_prices['toyota']
# print(car_prices)
# car_prices.clear()
# print(car_prices)

person = {
    'first name': 'Vadim',
    'last name': 'Shtripkin',
    'age': 35,
    'hobbies': ['video', 'plants', 'read'],
    'children': {'son': 'Michael', 'daughter': 'Dyusha'}
}
print(person['age'])
print(person['hobbies'])
hobbies = person['hobbies']
print(hobbies[2])

print(person['hobbies'][2])

children = person['children']
print(children['son'])

print(person['children']['son'])
person['car']  = 'mazda'
person['hobbies'][0] = 'music'
print(person.keys())
print(person.values())
print(person.items())

time_of_the_year = {
    'winter': ['december', 'january', 'february'],
    'spring': ['march', 'april', 'may'],
    'summer': ['june', 'july', 'august'],
    'fall': ['september', 'october', 'november']
}
print(time_of_the_year['summer'])
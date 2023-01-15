greeting = 'hello!'
# letter_list = []
# for letter in greeting:
#     letter_list.append(letter)
# print(letter_list)

# letter_list = [letter for letter in greeting]
# print(letter_list)
#
# number_list = [number for number in '0123456789']
# print(number_list)
# number_list_1 = [num for num in range(10)]
# print(number_list_1)
#
# number_list_2 = [num ** 2 for num in range(10)]
# print(number_list_2)
#
# number_list_3 = [((num - 3) / 2 ) ** 2 for num in range(10)]
# print(number_list_3)

# number_list = [6, 43, -2, 11, -55, -12, 3, 345]
# new_list = [number ** 3 / 2 for number in number_list if number > 0]
# print(new_list)
#
# new_list_1 = ['+' if number > 0 else '-' for number in number_list]
# print(new_list_1)


new_greetings=[]
greetings = ['hello', 'hi', 'hey', 'hola']
for letter in greetings:
    new_greetings.append(letter[1])
print(new_greetings)

greetings = ['hello', 'hi', 'hey', 'hola']
print([letter[1]for letter in greetings])

new_list = []
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in digits:
    if num % 2 == 1:
        new_list.append(num)
print(new_list)

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print([num for num in digits if num % 2 == 1])
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __len__(self):
        return self.age

    def __add__(self, other):
        return self.age + other.age

    def __del__(self):
        print(f'Object "{self.first_name} {self.last_name}" is deleted from memory.')

jack = Person('Jack', 'White', 45)
jane = Person('Jane', 'Air', 23)
print(jack + jane)
# print([1, 2, 3, 4, 5])
# print(jack)
# print(len(jack))
# del(jack)
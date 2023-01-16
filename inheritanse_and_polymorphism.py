# # Inheritance
#
# class Car:
#     wheels_number = 4
#
#     def __init__(self, name, color, year, is_crashed):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
#         print('Car is created')
#
#     def drive(self, city):
#         print(f'{self.name} is driving to {city}')
#
#     def change_color(self, new_color):
#         self.color = new_color
#         print(f'Color of {self.name} is changed to {new_color}')
#
#
# class Truck(Car):
#
#     wheels_number = 10
#
#     def __init__(self, name, color, year, is_crashed):
#         Car.__init__(self, name, color, year, is_crashed)
#         print('Truck is created')
#
#     def drive(self, city):
#         print(f'Truck {self.name} is driving to {city}')
#
#     def load_cargo(self, weight):
#         print(f'The cargo is loaded. Weight is {str(weight)}' )
#
#
#
# man_truck = Truck('Man', 'white', 2015, False)
# man_truck.drive('London')
# man_truck.change_color('black')
# print(man_truck.color)
# print(man_truck.wheels_number)
# man_truck.load_cargo(2000)
#
# # polymorphism
#
#

class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('Class successor must implement this method ')

class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} is saying "WOOF"')

class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} is saying "MEOW"')

class Mouse(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} is saying "PEE-PEE-PEE"')

class Fish(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} is saying nothing')

spike = Dog('Spike')
tom = Cat('Tom')
jerry = Mouse('Jerry')
freddy = Fish('Freddy')
pet_list = [spike, tom, jerry,freddy]
for pet in pet_list:
    pet.speak()

def pet_voice(pet):
    pet.speak()

pet_voice(spike)
pet_voice(tom)
pet_voice(jerry)
pet_voice(freddy)
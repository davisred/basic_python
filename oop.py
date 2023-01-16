# class Car:
#     wheels_number = 4
#
#     def __init__(self, name, color, year, is_crashed):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
#
#
#     def drive(self, city):
#         print(f'{self.name} is driving to {city}')
#
#
#     def change_color(self, new_color):
#         self.color = new_color
#
# opel_car = Car('opel', 'red', 2007, True)
# opel_car.drive('Kiev')
# mazda_car = Car('Mazda', 'black', 2020, False)
# mazda_car.drive('Moscow')
# mazda_car.change_color('blue')
# print(mazda_car.color)

class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.circumference = 2 * self.pi * self.radius

    def get_area(self):
        return self.pi * (self.radius ** 2)

    # def get_circumference(self):
    #     return 2 * self.pi * self.radius


circle_1 = Circle()
print(circle_1.get_area())
print(circle_1.circumference)
# print(circle_1.get_circumference())
# circle_2 = Circle(3)
# print(circle_2.get_area())
# print(circle_2.get_circumference())
# circle_3 = Circle(5)
# circle_area = circle_3.get_area()
# print(circle_3.get_circumference())
# print(circle_area)
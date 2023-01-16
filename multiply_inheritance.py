class Swimable:
    def __init__(self, name):
        print('Method init () of Swimable')
        self.name = name

    def greeting(self):
        print(f'Hello, my name is {self.name} and I can swim.')

    def swim(self):
        print('I\'m swimming')


class Walkable:
    def __init__(self, name):
        print('Method init () of Walkable')
        self.name = name

    def greeting(self):
        print(f'Hello, my name is {self.name} and I can walk.')

    def walk(self):
        print('I\'m walking')

class Flyable:
    def __init__(self, name):
        print('Method init () of Flyable')
        self.name = name

    def greeting(self):
        print(f'Hello, my name is {self.name} and I can fly.')

    def fly(self):
        print('I\'m flying')

class GameCharacter(Walkable, Flyable, Swimable):
    def __init__(self, name):
        print('Method init () of GameCharacter')
        self.name = name
        Swimable.__init__(self,name)
        Walkable.__init__(self, name)
        Flyable.__init__(self, name)


    def greeting(self):
        print(f'Hello, my name is {self.name}.')

james = GameCharacter('James')
james.greeting()
# james.swim()
# james.walk()
# james.fly()
#
# print(isinstance(james, Walkable))
# print(isinstance(james, Swimable))
# print(isinstance(james, Flyable))
# print(isinstance(james, GameCharacter))
# print(isinstance(james, object))



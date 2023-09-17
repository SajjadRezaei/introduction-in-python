import datetime


class Person:
    def __int__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):  # instance | regular method
        print(f'{self.name} is {self.height} is {self.age}')

    @classmethod
    def from_birth(cls, name, height, age):
        return cls(name, height, datetime.datetime.now().year - age)

    @staticmethod
    def is_adult(age):
        if age > 18:
            print('Yes')
        else:
            print('No')


a = Person.from_birth('sajjad', 179, 28)

b = Person.from_birth('ali', 180, 23)

a.name = 'sajjad'
a.age = 28

b.name = 'ali'
b.age = 23

a.show()

print(f'{a.name} has age {a.age}')


class Car:
    obj_num = 0  ## class varibales

    def __init__(self, name):
        self.name = name
        Car.obj_num += 1

    def show(self):
        print(self.name)


a = Car('benz')
v = Car('benzcc')
a.show()

print(Car.obj_num)

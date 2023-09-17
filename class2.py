# Python program to demonstrate
# use of a class method and static method.
from datetime import date


class Person:
    def __init__(self, name, heigt, age):
        self.name = name
        self.age = age
        self.heigt = heigt

    # a class method to create a
    # Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, heigt, year):
        return cls(name, heigt, date.today().year - year)

    def display(self):
        print("Name : ", self.name, "Age : ", self.age, "Height : ", self.heigt)


person = Person('mayank', 128, 21)
person.display()


#############

class Car:
    wheel = 4  ## class varaible

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'i have a {self.name}')


class Motor(Car):
    wheel = 2

    def __init__(self, name, helmet):
        super().__init__(name)
        self.helmet = helmet

    def show(self):
        super().show()
        print(f'i ride {self.name}')


m = Motor("Honda", "xzxz")

m.show()

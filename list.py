names = ['sajjad', 'mamad', 'zahra']

names2 = ['kevin', 'tahmores']

print(names)

print(names + names2)

names[1:] = ['sohrad']

print(names)

print(len(names))

cars = ['benz', 'bmw', ['audi', 'pride'], 'ford', 'tesla']
print(cars)
print(cars[::-1])
print(cars[2][1])

print(cars[:])

print(cars[:3])

print(cars[-5:-3])

####################### functions

cars.append("test")

print(cars)

cars.extend(["test2", "test3"])

print(cars)

cars.append(["test2", "test3"])

print(cars)

cars.insert(0, "pejo")

print(cars)

cars.pop(0)

print(cars)

print(cars.count('test2'))

print(cars.reverse())

del cars[1:3]

print(cars)

print(cars.index('benz'))

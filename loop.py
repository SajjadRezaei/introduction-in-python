x = 0

while x < 10:
    print(x, end=',')
    x += 1

print('Done')

# infinity loop
# while True:
#     print("hello")


num = 10
while num > 6:
    print(num)
    num = num - 1
else:
    print("loop is finished")

num = 10
while num > 6:
    break
    print(num)
    num = num - 1
else:
    print("loop is finished")

################ if statment #####################

x = 12

if x > 18:
    print('No')
elif x == 12:
    print('12')
else:
    print('Nothing')

#################### For #################

digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")

names = ['jack', 'kevin', 'mark', 'bob']
for name in names:
    if name == 'mark':
        break
    print(name)
else:
    print('Done...')

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

for number in range(1, 11):
    if number % 2 == 0:
        continue
    print(number)

###################### range

nums = list(range(1, 100, 3))
num2 = list(range(1, 100, 3))
print(nums)

print(nums == num2)

def fib(num):
    pass


def show(name='sajjad'):
    print(name + " hello word")
    return name


show()


double = lambda x: x * 2

print(double(5))


def greeting(name, *args):
    print(args)



greeting('amir', 'kevin', 12, ['a', 'b'])



def greeting(name, *args, **kwargs):
    print(args)
    print(kwargs)


greeting('amir', 'kevin', 12, city='Tehran', code='+98')


BASE_VAL = 100
#https://www.python.org/dev/peps/pep-0008/#constants

def value_tester(a, b):
    val = a + b
    if val > BASE_VAL:
        statement = 'bigger than'
    elif val == BASE_VAL:
        statement = 'the same as'
    else:
        statement = 'smaller than'

    print(f'The value is {statement} the base value.')

value_tester(10, 10)

#slide 4

def value_tester(a, b):
    val = sum([a, b])
    if val > BASE_VAL:
        statement = 'bigger than'
    elif val == BASE_VAL:
        statement = 'the same as'
    else:
        statement = 'smaller than'

    print(f'The value is {statement} the base value.')

value_tester(10, 10)

#slide 5
x, y = [10, 20]
print(x)
print(y)

x, y = [10, 20, 30]

x, *y = [10, 20, 30]
print(x)
print(y)

#slide 7
def value_tester(*ab):
    val = sum(ab)
    if val > BASE_VAL:
        statement = 'bigger than'
    elif val == BASE_VAL:
        statement = 'the same as'
    else:
        statement = 'smaller than'

    print(f'The value {val} is {statement} the base value.')

value_tester(10, 10)

#slide 11
def value_tester(*ab, func=sum):
    val = func(ab)
    if val > BASE_VAL:
        statement = 'bigger than'
    elif val == BASE_VAL:
        statement = 'the same as'
    else:
        statement = 'smaller than'

    print(f'The value is {statement} the base value.')

value_tester(10, 10, 10)

#slide 12
def value_tester(*ab, func=sum):
    val = func(ab)
    if val > BASE_VAL:
        statement = 'bigger than'
    elif val == BASE_VAL:
        statement = 'the same as'
    else:
        statement = 'smaller than'

    print(f'The value is {statement} the base value.')

my_func = sum

my_func is sum
my_func == sum

import numpy as np
value_tester(10, 10, func=np.prod)

#slide 13
def my_func(a, b):
    return (a + b) / 2

lambda a, b: (a + b) / 2

#slide 17
value_tester(10, 10, func=lambda ab: sum(ab) / len(ab))

value_tester(150, 50, func=lambda ab: sum(ab) / len(ab))

def my_func(arg):
    return arg + 10
my_func(10)

my_func = lambda arg: arg + 10
my_func(10)

#slide 21
class Vehicle():
    def __init__(self, kind):
        self.kind = kind

    def what_am_i(self):
        print(f'I am a {self.kind}.')

    def fuel(self):
        print('I use oil for fuel.')

vehicle = Vehicle('car')
vehicle.what_am_i()
vehicle.fuel()

class Bicycle(Vehicle):
    def fuel(self):
        print('I am people-powered.')

    def peddle_me(self):
        print('You have to peddle fast.')

bike = Bicycle('bike')
bike.what_am_i()
bike.fuel()
bike.peddle_me()

#slide 25
class MyString(str):
    def say_hello(self):
        print('Hello world!')

    def lower(self):
        print("No, I don't want to be in lower case!")

ms = MyString('Hello my name is Jeff.')
ms.lower()
ms.upper()
ms.say_hello()

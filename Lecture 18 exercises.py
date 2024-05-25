x = 10
y = 0

z = x / y


x = 10
y = 0
assert(y != 0), 'Error: y cannot be 0'
z = x / y


x = 10
y = 0

try:
    z = x / y
except ZeroDivisionError:
    print('Error: y cannot be 0')

#slide 4-5
x = 10
y = [5]
try:
    z = x / y
except ZeroDivisionError:
    print('Error: y cannot be 0')
except IndexError:
    print('Error: the length of list y is not correct')
except:
    print('Something else went wrong...')
    

#slide 6
def string_fixer(s):
    assert(isinstance(s, str)), 'string_fixer requires string arg'
    s = s.lower().strip()
    if s.startswith('a'):
        return "it's an a!"
    else:
        return "it's not an a."
    
string_fixer(42)

isinstance('Hello world!', str)
isinstance('Hello world!', int)

class MyClass():
    pass

my_instance = MyClass()

isinstance(my_instance, MyClass)

#slide 9
def math_some_numbers(a, b):
    val = (a + b) * 2
    return val

math_some_numbers(10, 20)
math_some_numbers('Hello', 'World')

import numbers
#https://docs.python.org/3/library/numbers.html

def math_some_numbers(a, b):
    assert(isinstance(a, numbers.Number) and 
           isinstance(b, numbers.Number)), 'Must pass in numeric arguments!'
    val = (a + b) * 2
    return val

math_some_numbers(10, 20)
math_some_numbers('Hello', 'World')

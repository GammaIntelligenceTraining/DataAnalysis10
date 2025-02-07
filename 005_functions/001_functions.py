# 1. Function basics

def area(a, b):
    print(f'Area of a rectangle with sides {a} and {b} is {a*b}')

x = area(7, 5)

area(7)  # This will raise an error due to missing argument

def area(a, b):
    return a * b

print(area(4, 8))

x = area(2, 5)
print(x)

# only one return can be executed!
def number_size(num):
    if num > 10:
        return 'Number more than 10!'
    if num > 100:
        return 'Number more than 100!'
    if num > 1000:
        return 'Number more than 1000!'

print(number_size(1001))

# 2. Scope

x = 10

def power_of_3():
    return x*x*x

print(power_of_3())

def power_of_3():
    x = 5
    return x*x*x

print(power_of_3())

def power_of_3():
    x = 5
    x = x*x*x
    return x

print(power_of_3())
print(x)

def power_of_3():
    global x
    x = 5
    x = x*x*x
    return x

print(power_of_3())
print(x)

# 3. Import functions from another file

from my_functions import main

main(38806040384)

# Functions in separate Python file
def main(code):
    code = str(code)
    if not code.isdigit():
        print('ID must contain only digits!')
    elif len(code) > 11:
        print('Your ID is too long!')
    elif len(code) < 11:
        print('Your ID is too short!')
    else:
        check_gender(code)
        check_dob(code)

def check_gender(code):
    if code[0] in ['1', '3', '5']:
        print('You are male')
    elif code[0] in ['2', '4', '6']:
        print('You are female')
    else:
        print('Your gender is undefined')

def check_dob(code):
    print(f'Your date of birth is: {code[5:7]}.{code[3:5]}.{code[1:3]}')

# 4. Types of arguments
def sum_of_els(a, b=5):
    return a + b

print(sum_of_els(2))
print(sum_of_els(2, 10))
print(sum_of_els(b=7, a=8))

def sum_of_els(a, b=5, *args):
    print(args)
    return a + b + sum(args)

print(sum_of_els(3, 7, 8, 9, 10))
print(sum_of_els(3))

def sum_of_els(a, b=5, *args, **kwargs):
    print(args)
    print(kwargs)
    return a + b + sum(args) + kwargs['age']

print(sum_of_els(1, 2, 3, 4, 5, name='Jack', age=37))

# 5. Recursion
def factorial(num):
    if num > 1:
        f = num * factorial(num-1)
        return f
    else:
        return 1

print(factorial(5))

# 6. Mapping
lst1 = [*range(1, 11)]
print(lst1)
print(list(map(str, lst1)))

def pow_of_3(num):
    return num ** 3 + num

print(list(map(pow_of_3, lst1)))

lst2 = [3, 2, 5, 11, 6, 0, 4]

def compare_els(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return 'equal'

print(list(map(compare_els, lst1, lst2)))
print(list(map(lambda num: num**3 + num, lst1)))

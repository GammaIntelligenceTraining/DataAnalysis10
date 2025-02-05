# 1. Logical conditions

## 1.1 Comparison operators
a = 7
b = 10

print(a > b)  # False
print(b >= a)  # True
print(a < b)  # True
print(b <= a)  # False
print(a == b)  # False
print(a != b)  # True
print(0 < a < 15)  # True

## 1.2 Comparison of words and symbols
print('a' > 'b')  # False
print('b' > 'a')  # True
print('A' > 'a')  # False
print(ord('a'))  # 97
print(chr(97))  # 'a'
print('apple' == 'apple')  # True
print('apple' == 'applepie')  # False
print('apple' < 'applepie')  # True

## 1.3 Boolean operators

### 1.3.1 And
print(True and True)  # True
print(True and False)  # False
print(True and False and True)  # False
print(5 > 2 and 7 == 5)  # False
print(10 % 2 == 0 and 'hello'.isalpha())  # True

### 1.3.2 Or
print(True or True)  # True
print(True or False)  # True
print(False or False)  # False
print(10**3 <= 1000 or None)  # True

### 1.3.3 Not
print(not True)  # False
print(not False)  # True
print(not 5 > 0)  # False
print(not [])  # True

### 1.3.4 Complicated clause
code = '51306040387'
print(len(code) == 11 and code.isdigit() and (0 < int(code[0]) <= 4 and 0 <= int(code[1:3]) <= 99 or 5 <= int(code[0]) <= 6 and 0 <= int(code[1:3]) <= 23))

# 2. If, else, elif
## 2.1 Basic clause
code = '12345678910'

if len(code) == 11:
    print('Your national ID is:', code)
elif len(code) > 11:
    print('Your ID is too long!')
else:
    print('Your ID is too short!')

# Many elif statements
age = int(input('Please enter your age: '))
if 0 < age <= 12:
    print('You are a child')
elif 12 < age <= 18:
    print('You are a teenager')
elif 18 < age <= 65:
    print('You are an adult')
elif 65 < age <= 120:
    print('You are a senior')
else:
    print('Wrong input!')

## 2.2 Nested clauses
if code.isdigit():
    if len(code) == 11:
        print('Your national ID is:', code)
    elif len(code) > 11:
        print('Your ID is too long!')
    else:
        print('Your ID is too short!')
else:
    print('Your code must contain only digits')

## 2.3 Clause in for loop
string = 'This string will be iterated soon!'
for i in range(len(string)):
    if string[i] == ' ':
        print('_', end='')
    elif string[i] == 'i' or i % 2 == 0:
        print(string[i].upper(), end='')
    else:
        print(string[i], end='')
print()

## 2.4 Clause in one line
x = 7
print('X more than ten') if x > 10 else print('X less or equal to ten')

# 3. Other operators
## 3.1 In, not in
lst = [1, 2, 3, 4, 'a', 'b', 'c']
print('a' in lst)  # True
print(2 not in lst)  # False

## 3.2 Is, is not
x = 10
y = 10
print(x == y)  # True
print(x is y)  # True
print(id(x))
print(id(y))

lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
print(lst1 == lst2)  # True
print(lst1 is lst2)  # False
print(lst1[0] == lst2[0])  # True
print(lst1[0] is lst2[0])  # True
print(id(lst1))
print(id(lst2))
print(id(lst1[0]))
print(id(lst2[0]))

## 3.3 Any, All
lst = [-2, -1, 0, 1, 2]
print(any(lst))  # True
print(all(lst))  # False
lst.remove(0)
print(all(lst))  # True

# Some examples
# FizzBuzz
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(num, 'FizzBuzz')
    elif not num % 3:
        print(num, 'Fizz')
    elif not num % 5:
        print(num, 'Buzz')

# Finding indexes of 's' in a string
string = 'she sells seashells by the seashore'
for i in range(len(string)):
    if string[i] == 's':
        print(i)

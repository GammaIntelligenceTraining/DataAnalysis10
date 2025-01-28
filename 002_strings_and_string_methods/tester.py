"""
asd
as
dsa
d
as
das
das
"""
string_sample1 = "Hello world world"
                # 0123456....
                        #-5-4-3-2-1
string_sample2 = "fiRst leTtEr is Not CApitAL. Hello world."
string_sample3 = " ***    hello world !!!  "
german_sample = "der Fluß"

print(len(string_sample1))

# print(string_sample1[len(string_sample1) - 1])
# print(string_sample1[-1])
# [START:END:STEP]
# print(string_sample1[3:10])
# print(string_sample1[:10])
# print(string_sample1[10:])
# print(string_sample1[::-1])
# string_sample1 = string_sample1[::-1]
# print(string_sample1)

# print(string_sample1[:5] + " " + string_sample1[6:11])

# print(string_sample2.upper())
#
# print(german_sample.lower())
# print(german_sample.casefold())
#
# print(string_sample2.title())
# print(string_sample2.capitalize())
#
# print(string_sample3.strip(' *!'))
# print(string_sample3.lstrip(' *!'))
# print(string_sample3.rstrip(' *!'))
#
# print(string_sample1.replace('world', 'planet', 1))
# print(string_sample1.replace(' ', '').replace('w', 'W'))

# print('HELLO12312WORLD'.isalpha())

# print(string_sample1.split(', '))
# print(string_sample1.count('world', 6, 12))
# print(string_sample1.find('world'))

# print(' hello '.center(30, "*"))
# print('123'.zfill(10))

# string = ("My favourite book is\n"
#           "\"Metro 2033\". \' \\")
#
# print(string)

# print("Hello", "John.", "You are", 40, "years old.", sep='', end='****')

# print('_' * 30)

# salary = 1500
# name = 'Jack'
# message = "{1}s salary is ${0}."
# print(message.format(salary, name))
# price = 2000
# message = "This {product} costs ${price:,.2f}."
# print(message.format(price=price, product='computer'))

# # Formated string used in Python 2
# x = 12231.3456789
# y = 131.1314
# print('The value of x is %.4f' % x)
# print('The value of y is %.2f' % y)
#
# emp_name = 'John'
# emp_age = 30
# emp_salary = 1500
#
# emp_string = ('Hi, my name is %(name)s! I am %(age)s old. My salary is %(salary).2f' %
#               {'name': emp_name, 'salary': emp_salary, 'age': emp_age})
# print(emp_string)

salary = 2000
name = 'jack'
is_manager = True

print(f'This {name.title()}. His salary is ${salary:.2f}. It is {str(is_manager).lower()} that he is a manager.')
print(r"C:\User\new")
byte_sting = b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'
print(byte_sting.decode('utf-16'))
print("hello world".encode("utf-16"))
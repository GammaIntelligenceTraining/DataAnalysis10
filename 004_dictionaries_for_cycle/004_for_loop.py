# 1. Range function

print(range(10))
print(*range(10))
print(*range(1, 15, 2))
print(*range(5, -15, -1))

lst = [*range(15)]
print(lst)
print(list(range(15)))

# 2. For loop

for x in range(1, 10):
    x **= 2
    print(x)

string = 'Hello world!'
lst = []
cnt = 1

for char in string:
    lst.append(f'Char {cnt}: {char}')
    cnt += 1

print(lst)

string = ''
for el in lst:
    string += el[-1].upper()

print(string)

courses = ['Math', 'Art', 'Physics', 'English', 'History']
names = ['Jack', 'Jane', 'Tom', 'Ann']
grades = ['A+', 'A', 'A-', 'B']

for course in courses:
    for name in names:
        for grade in grades:
            print(f'{name} got {grade} in {course} yesterday')

lst = ['A', 'B', 'C', 'D', 'E']

for i in range(len(lst)):
    print('Element', lst[i], 'has an index:', i)

num_string = '12 17 24 1 -8 19 27 132 -50 4 -21'
num_lst = []

for num in num_string.split():
    num = int(num)
    num_lst.append(num)

print(f'''The numbers are:
{num_lst}

The min value is: {min(num_lst)}
The max value is: {max(num_lst)}
The sum is: {sum(num_lst)}''')

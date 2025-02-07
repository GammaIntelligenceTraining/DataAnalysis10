# 1. Set
empty_set = set()

new_set = set('data')
print(new_set)

set1 = {'Estonia', 'Lithuania', 'Latvia', 'Poland'}
set2 = {'Estonia', 'Finland', 'Sweden', 'Poland'}

# 1.1 Set methods
set1.add('Denmark')
print(set1)

set1.add('Latvia')
print(set1)

# Remove random element
print(set1.pop())
print(set1)

set1.remove('Latvia')
print(set1)

# Discarding elements
set1.discard('Poland')
print(set1)

set1.discard('Poland')  # No exception if element not present

# issubset & issuperset
print({'Estonia', 'Latvia'}.issubset(set1))
print(set1.issuperset(['Estonia', 'Latvia']))

# 1.2 Set operations
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.union(set2))
print(set1 & set2)  # Intersection
print(set1 - set2)  # Difference

# Update set1 with set2
set1 |= set2
print(set1)

# 2. Dictionary

# 2.1 Create a dictionary
empty_dict = {}
print(empty_dict)

d = dict(name='Joe', age=20)
print(d)

d = {'name': 'Ann', 'Age': 15}
print(d)

different_dict = {1: 'int_value', 'str_key': 'str_value', 3.3: 'float_value', 'names': ['Mike', 'John', 'David'], (1, 2, 3): 'tuple_value'}
print(different_dict)

employee = dict([('Name', 'Sam'), ('Age', 37), ('Salary', 2200)])
print(employee)

# 2.2 Get a value
print(different_dict['str_key'])
print(different_dict[1])
print(different_dict.get(1))
print(different_dict.get(10, 'Key not found'))

# 2.3 Add, delete and change items
employee['Last name'] = 'Gold'
employee['Name'] = 'Marie'
print(employee)

name = employee.pop('Name')
print(name)
print(employee)

employee.update({'First name': 'Marie', 'Tel number': '123-4567', 'Rest days per year': 28})
print(employee)

# 2.4 Get keys, values and items
print(employee.keys())
print('***'.join(employee.keys()))
print(employee.values())
print(employee.items())

# 2.5 For loops in dictionaries
for key in employee:
    print(key)

for value in employee.values():
    print(value)

for key, value in employee.items():
    print(key, 'is', value)

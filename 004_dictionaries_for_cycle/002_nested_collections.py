# 1. Indexing of nested collections

nested_list = [
    [1, 2, 3],
    [{'name': 'Ann', 'surname': 'Smith'}, {'name': 'Ben', 'surname': 'Adams'}],
    [{7, 4, 9, 15, 19}, ('ABC', 'DEF')]
]

print(nested_list[0])
print(nested_list[0][1])
print(nested_list[1][0]['surname'])

nested_list[1][1]['name'] = 'Kate'
print(nested_list)

nested_list[2][0].add(10)
print(nested_list)

# 2. Zip, enumerate functions

lst1 = ['winter', 'spring', 'summer', 'autumn']
lst2 = ['white', 'green', 'red', 'yellow', 'blue']

print(list(enumerate(lst1)))
print(dict(enumerate(lst1)))
print(list(zip(lst1, lst2)))
print(dict(zip(lst1, lst2)))

# 3. Pascal triangle

lines_number = 7
triangle = []

for i in range(lines_number):
    line = [1] * (i + 1)
    triangle.append(line)
    for j in range(len(line)):
        if j != 0 and j != len(line) - 1:
            line[j] = triangle[i - 1][j] + triangle[i - 1][j - 1]

print(*triangle, sep='\n')

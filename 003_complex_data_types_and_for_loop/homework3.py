# Print to console what is different in each set compared to another
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a.difference(set_b))
print(set_b.difference(set_a))


# Create a string from a list and save it to variable
# Make each name on a new line.
names = ['Jack', 'Mary', 'Samantha', 'George', 'Simon', 'John']
new_line = '\n'.join(names)
# print(new_line)
# nl = ''
# for name in names:
#     nl += name + "\n"
# print(nl)

# print sum of all numbers in a list
# print sum of all unique numbers in a list
numbers = [2, 53, 12, 87, 65, 32, 12, 2, 65, 32]
print(sum(numbers))
print(sum(set(numbers)))


# create a new list from studentsA and studentsB
# make sure there is no duplicates in a new lists
studentsA = ['Jack', 'Bob', 'Mary']
studentsB = ['Bob', 'Sarah', 'Simon']
new_lst = list(set(studentsA + studentsB))
print(new_lst)

# What elements are common for both tuples?
numbersA = (23, 52, 12, 75, 42)
numbersB = (75, 22, 42, 94, 70)
# common = set(numbersA).intersection(set(numbersB))
# print('Common numbers are:', end=" ")
# for num in common:
#     print(num, end=", ")


# add 5 to the tuple on a right position
a = (1, 2, 3, 4, 6, 7, 8)
a = list(a)
# a.insert(4, 5)
a.append(5)
a.sort()
a = tuple(a)
print(a)

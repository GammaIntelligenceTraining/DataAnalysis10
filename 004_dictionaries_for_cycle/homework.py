# Add a list of elements to a set
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
# sample_set.update(sample_list)
# sample_set |= set(sample_list)
# print(sample_set)

# Return a new set of identical items from two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
# set3 = set1.intersection(set2)
# set3 = set()
# set3 &= set2
# print(set1)


# Create two empty lists (long_names, short_names)
# Iterate through names list and add names that are longer than 5 characters
# to long_names, and others to short names
names = ['Sarah', 'Jessica', 'Anthony', 'Jack', 'Simon', 'Arthur', 'Maria', 'Samantha']
# long_names, short_names = [], []
# for name in names:
#     if len(name) > 5:
#         long_names.append(name)
#     else:
#         short_names.append(name)
# print(long_names)
# print(short_names)


# Given a list where each element is a year. Determine whether the given year is a leap year. If the year is a leap year,
# print YES, otherwise print NO. According to the Gregorian calendar, a year is a leap year if its number is a multiple of 4,
# but not a multiple of 100 OR if it is a multiple of 400.


years_list = [2012, 2011, 1492, 1861, 1600, 1700, 1800, 1900, 2000]
for y in years_list:
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        print(y, 'YES')
    else:
        print(y, 'NO')


# Write a program that prompts the user for a string and checks if the string contains only unique characters.
user_prompt = input('Enter something: ')
if len(user_prompt) == len(set(user_prompt)):
    print('Unique')
else:
    print('Not unique')

print(set('Hello world!'))

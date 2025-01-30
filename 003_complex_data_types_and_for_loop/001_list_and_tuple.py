# 1. List

# 1.1 Create a list
empty_list = []
empty_list = list()
print(empty_list)  # []
print(type(empty_list))  # <class 'list'>

not_empty_list = [1, 0.01, 'hello', True, None, [1, 'world', 0.5]]
print(not_empty_list)

# 1.2 List to variables
var1, var2, var3 = [1, 2, 3]
print(var1, var2, var3)

var1, var2, *var3 = [1, 2, 3, 4, 5]
print(var1)
print(var2)
print(var3)

var1, *var2, var3, var4 = [1, 2, 3, 4, 5, 6, 7, 'a', 'b', 'c']
print(var1)
print(var2)
print(var3)
print(var4)

print(*not_empty_list)

# 1.3 Indexing
print(not_empty_list[0])
print(not_empty_list[-1])
print(not_empty_list[2:5])
print(not_empty_list[:-2:2])
not_empty_list[2] = 'hi'
print(not_empty_list)
not_empty_list[1:4] = ['new', 'elements']
print(not_empty_list)
not_empty_list[0:3] = ['more', 'then', 2, 'elements']
print(not_empty_list)

# 1.4 List methods
cities = ['Tallinn', 'London', 'Tokyo', 'Rome', 'Paris']
nums = [1, 4, 6, 3, 8, 3, 4, 2]

# 1.4.1 Adding elements
cities.append('Oslo')
cities.insert(2, 'Madrid')
print(cities)
nums.extend([0, 12, 19])
print(nums)
nums.extend('number')
print(nums)

# List operations
print([1, 2, 3] + [4, 5, 6])
print([1, 2, 3] * 5)

# 1.4.2 Removing elements
cities.remove('London')
print(cities)
cities.pop()
print(cities)
popped_item = cities.pop(3)
print(cities)
print(popped_item)
p_item = cities.pop(1)
cities.insert(2, p_item)
print(cities)

# 1.4.3 Sorting methods
cities.reverse()
print(cities)
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
cities_sorted = sorted(cities)
print(cities)
print(cities_sorted)

# 1.4.4 Find methods
print(cities.index('Tokio'))
print(nums.count(3))

# 1.4.5 String - List methods
text = 'These     words will be the elements of the list soon!'
lst = text.split()
print(lst)
new_text = ', '.join(lst)
print(new_text)
print(new_text.split(', ', maxsplit=4))

# 1.4.6 Copy and clear
lst.clear()
print(lst)

lst1 = [1, 2, 3]
lst2 = lst1
print(lst1)
print(lst2)
lst1[0] = 10
lst2[-1] = 11
print(lst1)
print(lst2)
print(id(lst1))
print(id(lst2))

lst1 = [1, 2, 3]
lst2 = lst1.copy()
lst1[0] = 10
lst2[-1] = 11
print(lst1)
print(lst2)
print(id(lst1))
print(id(lst2))

# 1.4.7 Statistics functions
lst = [1, 13, 45, 2, 4, 12, 6, 3]
print(min(lst))
print(max(lst))
print(sum(lst))

# 2. Tuple
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1[1])
# t1[1] = 10  # This will raise an error
print(t1 + t2)

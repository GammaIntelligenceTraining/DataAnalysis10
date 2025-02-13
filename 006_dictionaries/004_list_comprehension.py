# Creating a list using a loop (traditional way)
numbers = [1, 2, 3, 4, 5]
squared_numbers = []
for num in numbers:
    squared_numbers.append(num ** 2)
print("Squared Numbers:", squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Using list comprehension (simpler way)
squared_numbers = [num ** 2 for num in numbers]
print("Squared Numbers:", squared_numbers)

# Filtering even numbers using list comprehension
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even Numbers:", even_numbers)

# Using if-else in list comprehension
labels = ["Even" if num % 2 == 0 else "Odd" for num in numbers]
print("Labels:", labels)

# Nested loops in list comprehension
pairs = [(x, y) for x in range(3) for y in range(3)]
print("Pairs:", pairs)

# Using a function inside list comprehension
def square(n):
    return n ** 2
squared_numbers = [square(num) for num in numbers]
print("Squared Numbers with function:", squared_numbers)

# List comprehension with zip()
list1 = [1, 2, 3]
list2 = [4, 5, 6]
summed = [x + y for x, y in zip(list1, list2)]
print("Summed Lists:", summed)

# Dictionary comprehension
squared_dict = {num: num ** 2 for num in numbers}
print("Squared Dictionary:", squared_dict)

# Set comprehension
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_squares = {num ** 2 for num in numbers}
print("Unique Squares:", unique_squares)

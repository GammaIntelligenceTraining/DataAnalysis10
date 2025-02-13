# ====================================
# 1. Using zip() to Combine Iterables
# ====================================

# Combining two lists into a list of tuples
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))
print("Zipped List:", zipped)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# Unzipping using zip(*)
numbers, letters = zip(*zipped)
print("Unzipped Numbers:", numbers)  # Output: (1, 2, 3)
print("Unzipped Letters:", letters)  # Output: ('a', 'b', 'c')

# Handling different-length iterables
list3 = [100, 200]
zipped_short = list(zip(list1, list3))
print("Zipped with Different Lengths:", zipped_short)  # Output: [(1, 100), (2, 200)]


# ====================================
# 2. Using map() to Apply a Function
# ====================================

# Squaring a list of numbers
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared Numbers with map:", squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Converting a list of strings to uppercase
words = ["hello", "world", "python"]
uppercase_words = list(map(str.upper, words))
print("Uppercase Words:", uppercase_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']

# Summing corresponding elements from two lists
list_a = [1, 2, 3]
list_b = [4, 5, 6]
summed = list(map(lambda x, y: x + y, list_a, list_b))
print("Summed Lists:", summed)  # Output: [5, 7, 9]


# ====================================
# 3. Using filter() to Select Elements
# ====================================

# Filtering even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Filtered Even Numbers:", even_numbers)  # Output: [2, 4]

# Filtering words with more than 5 letters
long_words = list(filter(lambda word: len(word) > 5, words))
print("Long Words:", long_words)  # Output: ['python']

# Filtering numbers greater than a threshold
threshold = 3
greater_than_threshold = list(filter(lambda x: x > threshold, numbers))
print("Numbers Greater Than Threshold:", greater_than_threshold)  # Output: [4, 5]
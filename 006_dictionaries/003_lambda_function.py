# Simple lambda function to square a number
square = lambda x: x ** 2
print("Lambda Square:", square(5))  # Output: 25

# Lambda function with multiple arguments
add = lambda x, y: x + y
print("Lambda Addition:", add(3, 7))  # Output: 10

# ====================================
# Using Lambda with Built-in Functions
# ====================================

# Using lambda with map() to square a list of numbers
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared Numbers with map:", squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Using lambda with filter() to extract even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Filtered Even Numbers:", even_numbers)  # Output: [2, 4]

# Using lambda with sorted() to sort by the second element in a list of tuples
tuples = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_tuples = sorted(tuples, key=lambda x: x[0])
print("Sorted Tuples:", sorted_tuples)  # Output: [(1, 'one'), (2, 'two'), (3, 'three')]

# ====================================
# Using Lambda Inside Functions
# ====================================

def power(n):
    return lambda x: x ** n

square_fn = power(2)
cube_fn = power(3)
print("Square of 4:", square_fn(4))  # Output: 16
print("Cube of 4:", cube_fn(4))  # Output: 64

# ====================================
# Lambda with Conditional Expressions
# ====================================

# Lambda function with if-else for checking even or odd
even_or_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print("Number 5 is:", even_or_odd(5))  # Output: Odd
print("Number 6 is:", even_or_odd(6))  # Output: Even
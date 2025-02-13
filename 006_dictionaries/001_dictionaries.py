# ====================================
# 1. Creating a Dictionary
# ====================================

dict_example = {"name": "Alice", "age": 25, "city": "New York"}
print("Dictionary:", dict_example)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# ====================================
# 2. Accessing Values
# ====================================

print("Name:", dict_example["name"])  # Output: Alice
print("Age:", dict_example.get("age"))  # Output: 25

# Accessing a non-existent key using get() with a default value
print("Country:", dict_example.get("country", "Not Found"))  # Output: Not Found

# ====================================
# 3. Modifying a Dictionary
# ====================================

dict_example["age"] = 26  # Updating a value
dict_example["email"] = "alice@example.com"  # Adding a new key-value pair
print("Updated Dictionary:", dict_example)

# ====================================
# 4. Removing Items
# ====================================

del dict_example["city"]  # Removing a key
print("Dictionary after deletion:", dict_example)

removed_value = dict_example.pop("age")  # Removing a key and getting its value
print("Removed Age:", removed_value)
print("Dictionary after pop:", dict_example)

# ====================================
# 5. Looping Through a Dictionary
# ====================================

# Looping through keys
for key in dict_example:
    print("Key:", key)

# Looping through values
for value in dict_example.values():
    print("Value:", value)

# Looping through key-value pairs
for key, value in dict_example.items():
    print(f"{key} -> {value}")

# ====================================
# 6. Dictionary Comprehension
# ====================================

numbers = [1, 2, 3, 4, 5]
squared_dict = {num: num ** 2 for num in numbers}
print("Squared Dictionary:", squared_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# ====================================
# 7. Nested Dictionaries
# ====================================

students = {
    "Alice": {"age": 25, "grade": "A"},
    "Bob": {"age": 22, "grade": "B"}
}
print("Alice's Grade:", students["Alice"]["grade"])  # Output: A

# ====================================
# 8. Converting Other Data Types to Dictionary
# ====================================

pairs = [("name", "Alice"), ("age", 25), ("city", "New York")]
person_dict = dict(pairs)
print("Converted Dictionary:", person_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
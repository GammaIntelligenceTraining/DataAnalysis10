# Write a code to return "Hero" from given string

example_string1 = "Hello bro"
print(example_string1[:2] + example_string1[-2:])

# Write a code to return "Jack is my name"
example_string2 = "jack Is My NAME"
print(example_string2.capitalize())


# Write a code to return "Get rid of junk please"
example_string3 = "%-*Get rid of *junk* please*-L%*"
print(example_string3.strip('%*-L').replace('*', ''))

# Write a code to return "Hello my name is Jack"
example_string4 = "hello my name is jack"
print(example_string4.capitalize().replace('jack', 'Jack'))

# Find all occurrences of “Estonia” in a given string ignoring the case.
example_string5 = "Welcome to estonia. Estonia is awesome, isn't it? I moved to ESTONIA 5 years ago."
print(example_string5.lower().count('estonia'))
print(example_string5.upper().count('ESTONIA'))


# Write a code to return f-string "Hello, my name is Jack"
var1 = "jack"
var2 = "hello"
var3 = "MY NAME IS"
print(f'{var2.capitalize()}, {var3.lower()} {var1.title()}')

# Write a code to return byte_string text value
byte_string = b"\316\273"
print(byte_string.decode('utf8'))

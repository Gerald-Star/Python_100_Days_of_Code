# DATA TYPES IN PYTHON
# Python has the following data types built-in by default, in these categories:

# 1. String
# 2. Integer
# 3. Float
# 4. Boolean
# 5. List

# 1. Numbers
# 2. Strings
# 3. List
# 4. Tuple
# 5. Set
# 6. Dictionary


# Print the first character of the string

print("New York"[0])  # Output: N
# The method of accessing characters in a string is called indexing.
# Indexing in Python starts from 0.

# What is subscripting?
# Subscripting is the process of selecting a character from a string using its index.
# The syntax for subscripting is string_name[index].

# Print the second character of the string
print("New York"[1])  # Output: e
print("New York"[-2])  # Output: k
# The negative index starts from the end of the string.

# Print the last character of the string
print("New York"[-1])  # Output: k

#* Thi is a string "112"

street_name = "Abbey Road"
print(street_name[4] + street_name[7])  # Output: yo

# Large Integers
print(123_456_789)  # Output: 123456789

# Float Data Type
# Float is a data type that represents real numbers.
print(3.14)  # Output: 3.14

# Boolean Data Type
# Boolean is a data type that represents True or False.
print(True)  # Output: True
print(False)  # Output: False

# List Data Type
# List is a data type that represents a collection of items.
# A list can contain items of different data types.

# Example 1: Creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

#? Data Types and functions
#* The data type of a variable can be found using the type() function.

# Example 1: Find the data type of a variable
name1 = "John"
print(type(name1))  # Output: <class 'str'>

name2 = 123
print(type(name2))  # Output: <class 'int'>

name3 = 3.14
print(type(name3))  # Output: <class 'float'>

name4 = True
print(type(name4))  # Output: <class 'bool'>

#! Length function len() doesn't work on integers or floats
# print(len(123))  # Error: TypeError: object of type 'int' has no len()
# print(len(3.14))  # Error: TypeError: object of type 'float' has no len()


#? Data Type Conversion or Type Casting
#* Data type conversion is the process of converting one data type to another.

# Example 1: Convert a string to an integer
number = "123"
print(type(number))  # Output: <class 'str'>
number = int(number)
print(type(number))  # Output: <class 'int'>


# ! ValueError: invalid literal for int() with base 10: '3.14'
# number = "3.14"
# number = int(number)
# print(number)

# Example 2: Convert an integer to a string
number1 = 123
print(type(number1))  # Output: <class 'int'>
number1 = str(number1)
print(type(number1))  # Output: <class 'str'>

# Example 3: Convert a string to a float
number2 = "3.14"
number2 = float(number2)
print(number2)  # Output: 3.14
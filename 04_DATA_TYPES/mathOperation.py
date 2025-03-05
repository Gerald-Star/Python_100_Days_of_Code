# Mathematical Operations
# +, -, *, /, %, **, //


# The // operator is used for floor division.
# It returns the floor value for the quotient.
print(10 // 3)  # 3

# The % operator is used for finding the remainder.
print(10 % 3)  # 1

# The ** operator is used for exponentiation.
print(2 ** 3)  # 8


# PEMDAS Rule
# Parentheses, Exponents, Multiplication and Division (from left to right), Addition and Subtraction (from left to right)
# Parentheses have the highest precedence and are evaluated first.
# Exponents have the next highest precedence.
# Multiplication and Division have the same precedence.
# Addition and Subtraction have the same precedence.
# Operators with the same precedence are evaluated from left to right.


# PEMDAS Examples : The orders matters

# Example 1
result = 10 + 2 * 3
print(result)  # Output: 16

# Example 2
result = (10 + 2) * 3
print(result)  # Output: 36

# Example 3
result = (10 + 2) ** 2 * 3 / 2
print(result)  # Output: 78.0



# Example 1: Addition of two integers
num1 = 10
num2 = 20
sum = num1 + num2
print(sum)  # Output: 30

# Example 2: Addition of string(higher) data type and integer(lower) datatype
num1 = "10"
num2 = 20

# This will give an error
# print(num1 + num2)  # Error: TypeError

# We can overcome this error by explicitly converting the integer to a string.
num1 = "10"
num2 = 20
num1 = int(num1)
print(num1 + num2)  # Output: 30



# Calculate bmi
height = 1.75
weight = 70
bmi = weight / height ** 2
print(bmi)  # Output: 22.857142857142

# Round the bmi to two decimal places using the round() function
rounded_bmi = round(bmi, 2)
print(rounded_bmi)  # Output: 22.86

# Round the bmi to int
rounded_bmi = round(bmi) 
print(rounded_bmi)  # Output: 23
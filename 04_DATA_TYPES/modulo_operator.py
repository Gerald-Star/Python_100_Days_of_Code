# What is a Modulo Operator?
# The modulo operator (%) returns the remainder of the division of the two numbers.
# The syntax for the modulo operator is dividend % divisor.

# Example 1: Modulo Operator
print(10 % 3)  # Output: 1
# The remainder of the division of 10 by 3 is 1.

# Example 2: Modulo Operator
print(15 % 4)  # Output: 3
# The remainder of the division of 15 by 4 is 3.

# Example 3: Modulo Operator
print(20 % 6)  # Output: 2

# Example 4: Modulo Operator
print(25 % 5)  # Output: 0

# Example 5: Modulo Operator

# The modulo operator can be used to check if a number is even or odd.
# If a number is divided by 2 and the remainder is 0, then the number is even.

# Check if a number is even
number = 10
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

studentScore = 35
if studentScore % 2 != 0:
  print("The student passed the exam.")
else:
  print("The student failed the exam.")
  
# The modulo operator can also be used to check if a number is divisible by another number.
# If a number is divisible by another number and the remainder is 0, then the number is divisible.

# Check if a number is divisible by another number
number = 15
divisor = 5
if number % divisor == 0:
    print("The number is divisible by", divisor)
else:
    print("The number is not divisible by", divisor)
    
# Example 6: Modulo Operator
# The modulo operator can be used to extract the last digit of a number.

# Extract the last digit of a number
number = 123
last_digit = number % 10
print("The last digit of", number, "is", last_digit)

# Example 7: Modulo Operator
number = 135
last_digit = number % 10
print("The last digit of", number, "is", last_digit)
    
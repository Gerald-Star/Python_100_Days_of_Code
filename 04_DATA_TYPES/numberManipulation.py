

#* Number Manipulation in Python

# Using += Operator
#* The += operator adds the right operand to the left operand and assigns the result to the left operand.

# Example 1: Using += Operator
num = 10
num += 5
print(num)  # Output: 15


# Using -= Operator
#* The -= operator subtracts the right operand from the left operand and assigns the result to the left operand.

# Example 2: Using -= Operator
num = 10
num -= 5
print(num)  # Output: 5


# Using *= Operator
#* The *= operator multiplies the right operand with the left operand and assigns the result to the left operand.

# Example 3: Using *= Operator
num = 10
num *= 5
print(num)  # Output: 50


# Using /= Operator
#* The /= operator divides the left operand by the right operand and assigns the result to the left operand.

# Example 4: Using /= Operator
num = 10
num /= 5
print(num)  # Output: 2.0


# Using %= Operator
#* The %= operator divides the left operand by the right operand and assigns the remainder to the left operand.

# Example 5: Using %= Operator
num = 10
num %= 3
print(num)  # Output: 1



# Using //= Operator
#* The //= operator divides the left operand by the right operand and assigns the floor value of the quotient to the left operand.

# Example 6: Using //= Operator
num = 10
num //= 3
print(num)  # Output: 3



# Using **= Operator
#* The **= operator raises the left operand to the power of the right operand and assigns the result to the left operand.

# Example 7: Using **= Operator

num = 2
num **= 3
print(num)  # Output: 8


# Using Unary Operators
#* Unary operators operate on a single operand.

# Example 8: Using Unary Operators

num = 10
print(-num)  # Output: -10

num = -10
print(+num)  # Output: -10


# Challenge :

# Welcome message
print("Welcome to the tip calculator.")

# Get user inputs
bill = float(input("What was the total bill?\n $"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Calculate the total amount including tip
tip_amount = bill * (tip_percent / 100)
total_bill = bill + tip_amount

# Calculate amount per person
amount_per_person = total_bill / people

# Format to 2 decimal places
final_amount = "{:.2f}".format(amount_per_person)

# Print result
print(f"Each person should pay: ${final_amount}")


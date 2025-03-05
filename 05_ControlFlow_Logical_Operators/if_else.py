# if else Statement
# if else statement is used to execute a block of code if the condition is true and another block of code if the condition is false.

# Syntax of if else statement
# if condition:
#     # block of code to be executed if the condition is True
# else:
#     # block of code to be executed if the condition is False
# Example 1: Using if else statement

age = 18

if age >= 18:
   print("You are eligible to vote.")
else:
  print("You are not eligible to vote.")
# Output
# You are eligible to vote.


# Example 2: Using if else statement with input()

age = int(input("Enter your age:\n "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
  
  
amount_in_account = 100  # Example balance amount
amount = int(input("Enter the amount to withdraw:\n"))  
if amount_in_account >= amount:
  print("Withdrawal successful")
else:
  print("Insufficient balance")
# Output15

score = 75
if score >= 90:
  print("You passed the exam: ")
else:
  print("You failed the exam: ")
  
  
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
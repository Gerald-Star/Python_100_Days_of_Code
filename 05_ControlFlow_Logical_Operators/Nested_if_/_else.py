# Nested if / else statement
# Nested if / else statement is used to check multiple conditions.

# Syntax of nested if / else statement
# if condition1:
#     # block of code to be executed if condition1 is True
#     if condition2:
#         # block of code to be executed if condition2 is True
#     else:
#         # block of code to be executed if condition2 is False
# else:
#     # block of code to be executed if condition1 is False

# Example 1: Using nested if / else statement
age = 18

if age >= 18:
    print("You are eligible to vote.")
    if age == 18:
        print("This is your first vote.")
    else:
        print("You have voted before.")
else:
    print("You are not eligible to vote.")
    
    
studentScore = 100
if studentScore >= 75:
  print("You have passed the exam.")
  if studentScore == 100:
    print("You have an excellent score.")
  else:
    print("You have a good score.")
else:
  print("You have failed the exam.")
    
    
    
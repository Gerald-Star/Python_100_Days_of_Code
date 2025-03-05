# Logical Operators
# Logical operators are used to combine conditional statements.

# Python has three logical operators:

# and: Returns True if both statements are true
# or: Returns True if one of the statements is true
# not: Reverse the result, returns False if the result is true


# Example 1: Using and logical operator
age = 18
studentScore = 100

if age >= 18 and studentScore >= 75:
  print("You are eligible to vote and you have passed the exam.")
  
# Example 2: Using and logical operator
pass_test_score = 30
pass_exam_score = 50

if pass_test_score <= 20 and pass_exam_score >= 50:
  print("You have passed the test or exam.")
else:
  print("You have failed the test and exam.")
  
# Example 3: Using or logical operator
smoking_age = 18
drinking_age = 21

if smoking_age <= 12 or drinking_age >= 21:
  print("You are eligible to smoke or drink.")
else:
  print("You are not eligible to smoke or drink.")


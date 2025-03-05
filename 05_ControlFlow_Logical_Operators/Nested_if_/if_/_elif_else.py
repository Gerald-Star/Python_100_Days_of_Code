# if/elif/else statement

# if/elif/else statement is used to check multiple conditions.

# Syntax of if/elif/else statement

# if condition1:
#     # block of code to be executed if condition1 is True
# elif condition2:
#     # block of code to be executed if condition1 is False and condition2 is True
# else:
#     # block of code to be executed if condition1 is False and condition2 is False


# Example 1: Using if/elif/else statement

age = 18

if age >= 18:
    print("You are eligible to vote.")
elif age == 17:#
    print("You can volunteer but not to vote.")
else:
    print("You are not eligible to vote.")
    
    
    
studentScore = 100
if studentScore >= 75:
  print("You have passed the exam.")
elif studentScore == 100:
  print("You have an excellent score.")
else:
  print("You have failed the exam.")
  
  
# Challenge 1: Using if/elif/else statement
# BNI Calculator
# Write a program that calculates the BNI (Body Mass Index) of a person.

weight = 85  # weight in kg
height = 1.75  # height in meters

bmi = weight / (height ** 2)
print("Your BMI is:", bmi)

if bmi < 18.5:
  print("You are underweight:")
elif bmi >= 18.5 and bmi < 24.9:
  print("You are healthy:")
elif bmi >= 25 and bmi < 29.9:
  print("You are overweight:")
else:
  print("You are obese:")
  
  
  
# Challenge 2: Using if/elif/else statement

print("Welcome to the Grade Rollercoaster!")
height = int(input("Enter your height in cm:\n"))

if height >= 120:
  print("You can ride the rollercoaster.")
  age = int(input("Enter your age:\n"))
  if age < 12:
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
  want_photo = input("Do you want a photo taken? Y or N\n")
  if want_photo == "Y":
    print("Photo taken.")
  else:
    print("No photo taken.")
else:
  print("You cannot ride the rollercoaster.")
  
  
# Challenge Pizza Order

print("Welcome to Python Pizza Deliveries!")
bill = 0

if input("Do you want a small pizza? Y or N\n") == "Y":
  bill += 15
if input("Do you want a medium pizza? Y or N\n") == "Y":  
  bill += 20
if input("Do you want a large pizza? Y or N\n") == "Y":
  bill += 25
  
if input("Do you want pepperoni? Y or N\n") == "Y":
  if bill == 0:
    bill += 3
  else:
    bill += 2

print(f"Your final bill is: ${bill}.") # Using the f-string to format the output


# Challenge using the if elif else statement

print("Welcome to the Love Calculator!")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = name1 + name2
lower_names = combined_names.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")

true = t + r + u + e

pizza_order = 0
size = input("Enter the size of the pizza (S, M, L):\n")

if size == "S":
  pizza_order += 3
elif size == "M":
  pizza_order += 5
elif size == "L":
  pizza_order += 7

add_pepperoni = input("Do you want to add pepperoni? Y or N:\n")
if add_pepperoni == "Y":
  if size == "S":
    pizza_order += 2
  else:
    pizza_order += 3
      
  print("The total bill is: $", pizza_order)
  print(f"Your price is ${pizza_order}.")


  
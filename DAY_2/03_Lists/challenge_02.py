# Rock Paper Scissors Game

# Importing the random module

import random

# Rock Paper Scissors Game

# Rock wins against Scissors

# Scissors wins against Paper

# Paper wins against Rock

# User choice

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

# Computer choice

computer_choice = random.randint(0, 2)

# Rock

if user_choice == 0 and computer_choice == 2:
    print("You win! You chose Rock and the computer chose Scissors.")
    
elif computer_choice == 0 and user_choice == 2:
    print("You lose! You chose Scissors and the computer chose Rock.")
    
elif computer_choice > user_choice:
    print("You lose!")
    
elif user_choice > computer_choice:
  
    print("You win!")
    
elif computer_choice == user_choice:
    print("It's a draw!")
    
# Paper

elif user_choice == 1 and computer_choice == 0:
  
    print("You win! You chose Paper and the computer chose Rock.")
    
elif computer_choice == 1 and user_choice == 0:
  
    print("You lose! You chose Rock and the computer chose Paper.")
    
elif computer_choice > user_choice:
  
    print("You lose!")
    
elif user_choice > computer_choice:
  
    print("You win!")
    
elif computer_choice == user_choice:
  
    print("It's a draw!")
    
# Scissors

elif user_choice == 2 and computer_choice == 1:
  
    print("You win! You chose Scissors and the computer chose Paper.")
    
elif computer_choice == 2 and user_choice == 1:
  
    print("You lose! You chose Paper and the computer chose Scissors.")
    
elif computer_choice > user_choice:
  
    print("You lose!")
    
elif user_choice > computer_choice:
  
    print("You win!")
    
elif computer_choice == user_choice:
  
    print("It's a draw!")
    
else:
  
    print("Invalid input! You have not entered 0, 1, or 2.")
    
# Output

# What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.
# 1

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

print(rock)

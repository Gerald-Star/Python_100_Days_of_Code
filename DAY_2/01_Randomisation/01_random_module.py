# Randomization in Python
# Randomization is a process of generating random numbers. 
# In Python, the random module is used to generate random numbers.
# A random is a Python module
# Example 1: Using the random module
# Import the random module

import random
import my_module

#random.randint(a, b)
#Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).

random_integer = random.randint(1, 10)  # Generate a random number between 1 and 10
print(random_integer)

print(my_module.my_favorite_number)


# How to Generate a Random Float number

random_number_0_to_1 = random.random()  # Generate a random float number between 0 and 1
print(random_number_0_to_1)

# How to Generate a Random Float number within a range

random_float = random.uniform(1, 10)  # Generate a random float number between 1 and 10
print(random_float)


random_heads_or_tails = random.randint(0, 1)  # Generate a random number between 0 and 1
if random_heads_or_tails == 1:
    print("Heads")
else:
    print("Tails")
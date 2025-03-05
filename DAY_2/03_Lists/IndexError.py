# IndexError is raised when the index is out of range.


# Example 1: IndexError

fruits = ["Apple", "Blackberry", "Cherry"]

# IndexError: list index out of range
print(fruits[3])  # This will raise an IndexError

# The list fruits has only three elements, so the index 3 is out of range.

num_fruits = len(fruits)
print(num_fruits)  # Output: 3


city_names = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
# IndexError: list index out of range

print(city_names[5])  # This will raise an IndexError
# The list city_names has five elements, so the index 5 is out of range.

num_cities = len(city_names)
print(num_cities)  # Output: 5

print(city_names[4])  # Output: Phoenix
# The index 4 is within the range of the list city_names.

# Example 2: IndexError in List Slicing

fruits = ["Apple", "Banana", "Cherry"]

# IndexError: list index out of range
print(fruits[1:4])  # This will raise an IndexError

# The list fruits has only three elements, so the index 4 is out of range.

print(city_names -1)  # Output: Phoenix
# The index 4 is within the range of the list city_names.
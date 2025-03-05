# Nested Lists

# A list can contain other lists as its elements. These are called nested lists.

# Example: Nested Lists

city_names = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
city_names_europe = ["Paris", "London", "Berlin", "Madrid", "Rome"]

my_fave_cities = [city_names, city_names_europe]
print(my_fave_cities)

# Output: [['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'], ['Paris', 'London', 'Berlin', 'Madrid', 'Rome']]

# Here, my_fave_cities is a nested list that contains two lists: city_names and city_names_europe.

# Create a nested list called matrix that contains two lists: [1, 2, 3] and [4, 5, 6].

matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix)
# Output: [[1, 2, 3], [4, 5, 6]]
# To access elements in a nested list, you can use multiple indices.

# Example: Accessing Elements in Nested Lists

matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix[0][1])  # Output: 2
print(matrix[1][1])  # Output: 5

# Here, matrix[0][1] accesses the second element in the first list, which is 2.

# matrix[1][1] accesses the second element in the second list, which is 5.

# Nested lists can be used to represent matrices, tables, or any other multi-dimensional data structures.

# Example: Matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access the first row
print(matrix[0])  # Output: [1, 2, 3]

# Access the second row
print(matrix[1])  # Output: [4, 5, 6]


# Access the third row
print(matrix[2])  # Output: [7, 8, 9]

# Access the first element of the first row

print(matrix[0][0])  # Output: 1

# Access the second element of the second row
print(matrix[1][1])  # Output: 5



fruits_fave = ["Apple", "Banana", "Cherry", "Mango", "Orange"]
fruits_not_fave = ["Pineapple", "Grapes", "Strawberry", "Kiwi", "Watermelon"]

my_fave_fruits = [fruits_fave, fruits_not_fave]
print(my_fave_fruits)

print(my_fave_fruits[0][1])  # Output: Banana
print(my_fave_fruits[1][0])  # Output: Pineapple
print(my_fave_fruits[1][1])  # Output: Cherry
print(my_fave_fruits[1][2])  # Output: Strawberry
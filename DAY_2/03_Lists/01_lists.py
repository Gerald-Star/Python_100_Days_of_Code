# Python Lists

# Lists are a data structure in Python that can store multiple values.
# They are ordered and changeable.

# Example 1: Creating a List
# Create a list of fruits
fruits = ["Apple", "Banana", "Cherry"]
print(fruits)

# Example 2: Accessing Items
# Access the first item of the list

print(fruits[0])

# Example 3: Negative Indexing
# Access the last item of the list

print(fruits[-1])

# Example 4: Range of Indexes

# Access the second and third items of the list

print(fruits[1:3])

# Example 5: Change Item Value
# Change the second item of the list

fruits[1] = "Blackberry"
print(fruits)


# Example 6: Loop Through a List
# Loop through the list of fruits

for fruit in fruits:
    print(fruit)
    
# Example 7: Check if Item Exists
# Check if "Apple" is present in the list

if "Apple" in fruits:
    print("Apple is present in the list")
    
# Example 8: List Length

# Get the number of items in the list
print(len(fruits))

# Example 9: Add Items
# Add "Orange" to the list

fruits.append("Orange") # Adds the item at the end of the list
print(fruits)

# Example 10: Insert Items

# Insert "Grapes" at the second position
fruits.insert(1, "Grapes")
print(fruits)

# Example 11: Remove Item
# Remove "Cherry" from the list

fruits.remove("Cherry")
print(fruits)




#? More Examples of List Methods


# Example 1: Creating a List

fruits = ["Apple", "Banana", "Cherry"]
print(fruits)
# Here, we create a list called fruits that contains three string elements: "Apple", "Banana", and "Cherry".
# The print(fruits) statement outputs the entire list.

# output ['Apple', 'Banana', 'Cherry']


# Example 2: Accessing Items

fruits = ["Apple", "Banana", "Cherry"]
print(fruits[0])

#Lists use zero-based indexing, which means the first item is at index 0, the second at 1, and so on.
#fruits[0] retrieves the first item in the list ("Apple") and prints it.
# Output: Apple


# Example 3: Negative Indexing

fruits = ["Apple", "Banana", "Cherry"]
print(fruits[-1])

# In Python, negative indexing allows us to access list elements from the end.
# fruits[-1] refers to the last item in the list, which is "Cherry".
# Output: Cherry


# Example 4: Range of Indexes

fruits = ["Apple", "Banana", "Cherry"]
print(fruits[1:3])

# This is list slicing, which retrieves a subset of the list.
# fruits[1:3] means:
# Start from index 1 ("Banana")
# Stop at index 3 (not included)
# So, it returns ["Banana", "Cherry"].
# Output: ['Banana', 'Cherry']


# Example 5: Change Item Value

fruits = ["Apple", "Banana", "Cherry"]
fruits[1] = "Blackberry"
print(fruits)

# Lists in Python are mutable, meaning we can change their values.
# Here, we replace "Banana" (index 1) with "Blackberry".
# Output: ['Apple', 'Blackberry', 'Cherry']


# Example 6: Loop Through a List

fruits = ["Apple", "Blackberry", "Cherry"]
for fruit in fruits:
    print(fruit)
# This for loop iterates over each item in the fruits list and prints it one by one.
# Output:

# Apple
# Blackberry
# Cherry

# Example 7: Check if Item Exists

fruits = ["Apple", "Blackberry", "Cherry"]

if "Apple" in fruits:
    print("Apple is present in the list")
    
# The in keyword checks if "Apple" exists in the fruits list.
# If "Apple" is found, it prints the message.
# Output: Apple is present in the list

# Example 8: List Length

fruits = ["Apple", "Blackberry", "Cherry"]
print(len(fruits))

#The len() function returns the number of items in the list.
# Output:  3


#Example 9: Add Items


fruits.append("Orange")  # Adds the item at the end of the list
print(fruits)

# output ['Apple', 'Blackberry', 'Cherry', 'Orange']

# The .append() method adds "Orange" to the end of the list.
# Output: ['Apple', 'Blackberry', 'Cherry', 'Orange']

#*Example 10: Insert Items


fruits.insert(1, "Grapes")
print(fruits)

# The .insert(index, item) method inserts "Grapes" at index 1, shifting other elements to the right.
# Output: ['Apple', 'Grapes', 'Blackberry', 'Cherry', 'Orange']
# Example 11: Remove Item

fruits.remove("Cherry")
print(fruits)

# The .remove(value) method removes "Cherry" from the list.
# Output:
# ['Apple', 'Grapes', 'Blackberry', 'Orange']

#these examples cover the basics of Python lists, including: 
#✅ Creating lists
#✅ Accessing items (positive & negative indexing)
#✅ Modifying lists
#✅ Looping through lists
#✅ Checking for an item
#✅ Adding and removing elements


# Negative Indexing
# In Python, negative indexing allows you to access elements from the end of the list.

# Example: Negative Indexing
# Access the last item of the list

city_names = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]

print(city_names[-1])  # Output: Phoenix
# Access the last item of the list using negative indexing.

print(city_names[-2])  # Output: Houston
# Access the second last item of the list using negative indexing.

print(city_names[-3])  # Output: Chicago
# Access the third last item of the list using negative indexing.
# Negative indexing starts from -1, which refers to the last element in the list.
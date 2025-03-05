 
import random
 
friends = ["Ann", "Jenny", "Lily", "Chloe"]

# Option 1: Using the random module
random_friend = random.randint(0, len(friends) - 1)
print(f"Random friend: {friends[random_friend]}")

# Option 2
print(random.choice(friends))

random_index = random.randint(0, 4)
print(friends[random_index]) # This will not raise an IndexError


city_names = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
city_names[-1]  # Output: Phoenix
city_names.append("San Francisco")
print(city_names)

city_names.insert(2, "Miami")
print(city_names)

# Output: ['New York', 'Los Angeles', 'Miami', 'Chicago', 'Houston', 'Phoenix', 'San Francisco']
# The .insert(index, value) method inserts the element "Miami" at index 2.

city_names.remove("Chicago")
print(city_names)

# Output: ['New York', 'Los Angeles', 'Miami', 'Houston', 'Phoenix', 'San Francisco']
# The .remove(value) method removes the element "Chicago" from the list.

city_names.pop(1)
print(city_names)

# Output: ['New York', 'Miami', 'Houston', 'Phoenix', 'San Francisco']
# The .pop(index) method removes the element at index 1, which is "Miami".

city_names.clear()
print(city_names)

# Output: []
# The .clear() method removes all the elements from the list.
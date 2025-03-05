# The Power of f-strings

# f-strings are a way to format strings in Python. They are prefixed with 'f' or 'F' and contain expressions inside curly braces {}. The expressions are replaced with their values. f-strings are evaluated at runtime, which allows you to embed expressions inside string literals.
# f-strings provide a concise and readable way to embed variables and expressions inside strings. 
# They are available in Python 3.6 and later versions.
# Mastering the use of f-string is essential for writing clean and readable code. Let's look at some examples to understand how f-strings work.




# Example 1: f-strings
name = "Alice"
age = 10
print(f"Hello, {name}. You are {age}.")
# Output: Hello, Alice. You are 10.

# In this example, we use f-strings to embed the variables name and age inside the string. The expressions inside curly braces are replaced with their values. The f-string evaluates the expressions at runtime and returns the formatted string.

# Use Cases of f-strings
# f-strings are used in various scenarios, such as:
# 1. Embedding variables inside strings.

# Example 2: Embedding variables inside strings
name = "Alice"
age = 10
print(f"Hello, {name}. You are {age} years old.")
# Output: Hello, Alice. You are 10 years old.



# 2. Formatting numbers.
# Example 3: Formatting numbers

#* In this example, we use f-strings to format the floating-point number pi to two decimal places. The expression {pi:.2f} formats the value of pi to two decimal places. The f-string evaluates the expression at runtime and returns the formatted string.
pi = 3.14159
print(f"Pi is approximately {pi:.2f}.")
# Output: Pi is approximately 3.14.

# Another example of formatting numbers using f-strings is shown below:
# Example 4: Formatting numbers

#* In this example, we use f-strings to format the integer value num to a fixed width of 5 characters. The expression {num:5d} formats the value of num to a fixed width of 5 characters. The f-string evaluates the expression at runtime and returns the formatted string.
num = 123
print(f"Number: {num:5d}")
# Output: Number:   123



# 3. Formatting dates and times.
# Example 5: Formatting dates and times

#* In this example, we use f-strings to format the current date and time. The expression {today:%Y-%m-%d} formats the current date in the YYYY-MM-DD format. The f-string evaluates the expression at runtime and returns the formatted string.
# from datetime import datetime

# today = datetime.today()
# print(f"Today's date is {today:%Y-%m-%d}")
# Output: Today's date is 2021-08-25.


# 4. Formatting dictionary values.

# Example 6: Formatting dictionary values
person = {"name": "Alice", "age": 10}
print(f"Name: {person['name']}, Age: {person['age']}")

# Output: Name: Alice, Age: 10.
# In this example, we use f-strings to format the values of the dictionary person. The expressions {person['name']} and {person['age']} access the values of the dictionary and embed them inside the string. The f-string evaluates the expressions at runtime and returns the formatted string.


# 5. Formatting list elements.

# Example 7: Formatting list elements
fruits = ["apple", "banana", "cherry"]
print(f"Fruits: {', '.join(fruits)}")
# Output: Fruits: apple, banana, cherry.

# In this example, we use f-strings to format the elements of the list fruits. The expression {', '.join(fruits)} joins the elements of the list with a comma and space and embeds them inside the string. The f-string evaluates the expression at runtime and returns the formatted string.

# Another example using the map() function to convert the list elements to strings before joining them:
# Example 8: Formatting list elements
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {', '.join(map(str, numbers))}")
# Output: Numbers: 1, 2, 3, 4, 5.

# Another example using a list comprehension to format the list elements:
# Example 9: Formatting list elements

#* In this example, we use a list comprehension to format the elements of the list numbers. The expression {', '.join([str(num) for num in numbers])} converts the list elements to strings and joins them with a comma and space. The f-string evaluates the expression at runtime and returns the formatted string.
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {', '.join([str(num) for num in numbers])}")
# Output: Numbers: 1, 2, 3, 4, 5.

# 6. Formatting function calls.

# Example 10: Formatting function calls
def greet(name):
    return f"Hello, {name}!"
  
print(greet("Alice"))
# Output: Hello, Alice!

# 7. Formatting expressions.

# Example 11: Formatting expressions
num1 = 10
num2 = 20
print(f"The sum of {num1} and {num2} is {num1 + num2}.")

# Output: The sum of 10 and 20 is 30.
# In this example, we use f-strings to format the sum of two numbers. 
# The expression {num1 + num2} calculates the sum of the numbers and embeds it inside the string. 
# The f-string evaluates the expression at runtime and returns the formatted string.c



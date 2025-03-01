# Description: This file is used to demonstrate string manipulation in Python.

# What is \n?
# \n is a special character that represents a new line. 
# It is called a newline character. It is used to start a new line in the output of the print() function.
print("Hello world!\nHello World!");

# What is \t?
# \t is a special character that represents a tab.
print("My\tWorld!");

# What is \\?
# \\ is a special character that represents a backslash.
print("Hello\\Everyone!");

# What is \r?
# \r is a special character that represents a carriage return.
print("World\rBest!");

# What is \b?
# \b is a special character that represents a backspace.
print("Good\bMorning");

# What is \f?
# \f is a special character that represents a form feed.

print("Hello\fWorld!");

# What is \v?
# \v is a special character that represents a vertical tab.

print("Hello\vWorld!");

# What is \a?
# \a is a special character that represents an alert.

print("Hello\aWorld!");


# Assign string to a variable
# Strings can be assigned to variables using the assignment operator (=).
# The variable name can be used to refer to the string value.

city = "New York"
print(city)

#* Multiline Strings

# Multiline strings can be created using triple quotes (""").
# Triple quotes can be used to create strings that span multiple lines.
# Triple quotes can be used to create strings that contain multiple lines of text.

# Example 1: Multiline string using triple quotes

triple = """This is a multiline string.
It can span multiple lines.
It can contain multiple lines of text."""

print(triple)

single = "This is a single line string."
print(single)

single1 = '''This is a single line string,
consecutive occurrence of single quotes
does not create multiline string.'''
print(single1)


#* Accessing Characters in a String
# Characters in a string can be accessed using the index of the character.

# Example 1: Accessing characters in a string

city = "New York"
print(city[0])  # Output: N
print(city[1])  # Output: e


#* String length

# The len() function can be used to find the length of a string.
# The length of a string is the number of characters in the string.

# Example 1: Finding the length of a string

city = "New York"
print(len(city))

# Example 2: Check the length of the user input

name = input("Enter your name: ")
print("The length of the name is:", len(name))

print(len(input("Where do you live?")))


study = input("What are you studying?")
print("The length of the study is:", len(study))


username = input("What is your username?")
print(len(username))
        
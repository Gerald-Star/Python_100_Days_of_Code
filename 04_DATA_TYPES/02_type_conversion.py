# ? TYPE CONVERSION

# * Type conversion is the process of converting the value of one data type (integer, string, float, etc.) to another data type.
# * Python has two types of type conversion:

# ? Implicit Type Conversion
# ? Explicit Type Conversion


# ? Implicit Type Conversion

# * In Implicit type conversion, Python automatically converts one data type to another data type without using the built-in function. 
# This process doesn't require any user involvement.
# In Python, implicit type conversion (type coercion) happens automatically when the interpreter converts one data type to another.


# * Let's see an example where Python promotes the conversion of the lower data type (integer) to the higher data type (float) to avoid data loss.

# Example 1: Converting integer to float
number = 10
print(number)  # Output: 10

number = 10.0
print(number)  # Output: 10.0

# In the above program, Python considers the integer value as 10 as a lower data type than the float value 10.0.
# So, it converts 10 to 10.0 to display the output.

#* Implicit Type Conversion Examples:
# Integer to Float
# Python automatically converts the integer to a float.

# Example 1
num_int = 5
num_float = num_int + 2.5  # int is automatically converted to float
print(type(num_float))  # Output: <class 'float'>



# Integer to complex
num_int = 10
num_complex = num_int + 2j  # int is converted to complex
print(type(num_complex))  # Output: <class 'complex'>


# Boolean to Integer
num = True + 5  # True is treated as 1, so result is 6
print(num)  # Output: 6
print(type(num))  # Output: <class 'int'>

# Integer to Boolean
result = 10 > 5  # Comparison returns boolean value
print(result)  # Output: True
print(type(result))  # Output: <class 'bool'>


# String Concatenation with Numbers
result = "Age: " + str(25)  # int is implicitly converted to string
print(result)  # Output: Age: 25




# ? Explicit Type Conversion
#* Explicit type conversion (type casting) is done manually by the programmer using built-in functions.
# * In Explicit Type Conversion, users convert the data type of an object to required data type.
# * We use the predefined functions like int(), float(), str(), etc to perform explicit type conversion.

# * This type of conversion is also called typecasting because the user casts (changes) the data type of the objects.

# * Syntax:
# * <required_datatype>(expression)

# * Typecasting can be done by assigning the required data type function to the expression.



# Example 1: Convert a string to an integer
number = "123"
print(type(number))  # Output: <class 'str'>
number = int(number)
print(type(number))  # Output: <class 'int'>


# Example 2: Convert an integer to a string
number1 = 123
print(type(number1))  # Output: <class 'int'>
number1 = str(number1)
print(type(number1))  # Output: <class 'str'>

# Example 3: Convert a string to a float
number2 = "3.14"
number2 = float(number2)
print(number2)  # Output: 3.14




# ?Explicit Type Conversion Examples:

# Integer to String
num = 100
num_str = str(num)
print(num_str)  # Output: 100
print(type(num_str))  # Output: <class 'str'>


# Float to Integer
num = 5.9
num_int = int(num)  # Converts to integer (truncates decimal part)
print(num_int)  # Output: 5
print(type(num_int))  # Output: <class 'int'>


# Integer to Float
num = 7
num_float = float(num)  # Converts integer to float
print(num_float)  # Output: 7.0
print(type(num_float))  # Output: <class 'float'>


num2 = 10
integer_to_float2 = float(num2)
print(integer_to_float2)
print(type(integer_to_float2))



# String to Integer
num_str = "50"
num_int = int(num_str)  # Converts string to integer
print(num_int)  # Output: 50
print(type(num_int))  # Output: <class 'int'>


# List to Tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)  # Converts list to tuple
print(my_tuple)  # Output: (1, 2, 3)
print(type(my_tuple))  # Output: <class 'tuple'>

# Tuple to List
my_tuple2 = (4, 5, 6)
my_tuple2_to_list = list(my_tuple2)
print(my_tuple2_to_list)
print(type(my_tuple2_to_list))






# Example 2: Addition of string(higher) data type and integer(lower) datatype
#* In this program, Python converts the integer to a string before performing string concatenation.

#num_int = 123
#num_str = "456"
#print(num_int + num_str)  # Error: TypeError

#* We can overcome this error by explicitly converting the integer to a string.

num_int = 123
num_str = "456"
num_str = int(num_str)
print(num_int + num_str)  # Output: 579

# Float to Integer
number3 = 3.4
float_to_int = int(number3)
print(float_to_int)
print(type(float_to_int))


name_of_city = input("Enter city name\n")
length_of_city = len(name_of_city)
print(length_of_city)
print(type(length_of_city))
print("Number of letters in your name is: " + str(length_of_city))
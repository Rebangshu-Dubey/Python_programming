# Python Data Types and Type Conversion

# Type conversion means converting a value from one data type to another. In Python, we can convert between different data types using built-in functions.
# we can do such type conversions either explicitly or implicitly. Explicit type conversion is done using functions like int(), float(), str(), etc.,
# while implicit type conversion is done automatically by Python when performing operations between different data types.

num1 = input("Enter num1 : ")
num2 = input("Enter num2 : ")

num1 = float(num1)  # Explicitly converting num1 to float
num2 = float(num2)  # Explicitly converting num2 to float

print("num1 is ", num1)
print(type(num1))  # This will print the data type of num1, which is now float

print("num2 is ", num2)
print(type(num2))  # This will print the data type of num2, which is now float

total = num1 + num2  # Adding the two numbers
print("The sum of num1 and num2 is: ", total)

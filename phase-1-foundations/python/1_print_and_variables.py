"""
Print and Variables lesson.

This script shows how to display values with print() and how to use variables.
"""

# print() displays text or values to the console.
print("Hello, World!")

# Variables store values so we can reuse them later.
# Python automatically detects the type of the value.
name = "Heidel"        # string - a sequence of characters
age = 30                # integer - a whole number
gpa = 3.5               # float - a number with a decimal point
is_student = True       # boolean - True or False value

# Use f-strings to create readable output with embedded values.
print(f"Name: {name}")
print(f"Age: {age}")
print(f"GPA: {gpa}")
print(f"Is student?: {is_student}")

# Variables can be updated:
age = age + 1
print(f"One year later, age = {age}")

# A variable can also hold a new type of value.
name = 123
print(f"Now name holds a number: {name} ({type(name).__name__})")


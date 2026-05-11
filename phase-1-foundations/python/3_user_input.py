"""
User input lesson.

This script shows how to get input from the user and convert the input to the proper type.
"""

# The input() function reads a line from the console and returns it as a string.
from unittest import result


name = input("Enter your name: ")
print(f"Hello, {name}!")
print(f"The input is stored as type: {type(name).__name__}")

age_text = input("Enter your age: ")
print(f"Input received: {age_text} (type: {type(age_text).__name__})")

# Convert the string to an integer for numeric operations.
age = int(age_text)
print(f"After conversion, age = {age} (type: {type(age).__name__})")
print(f"Next year you will be {age + 1} years old.")

# Input can also be converted to float when decimals are needed.
price_text = input("Enter a product price: ")
price = float(price_text)
print(f"Price after conversion is {price:.2f}")

# Use conversion to prevent runtime errors when performing math.
quantity = int(input("Enter item quantity: "))
total = price * quantity
print(f"Total cost for {quantity} items: {total:.2f}")

#String methods - these are functions that operate on strings and return a new string or a value based on the string content.

# len() can be used to get the length of the input string.
length_of_name = len(name)
print(f"Your name has {length_of_name} characters.")

result_find = name.find("a") # find() returns the index of the first occurrence of "a" or -1 if not found.

result_rfind = name.rfind("e") # rfind() returns the index of the last occurrence of "e" or -1 if not found.  

name = name.capitalize() # capitalize() returns a copy of the string with the first character capitalized and the rest lowercased.

name = name.upper() # upper() returns a copy of the string with all characters converted to uppercase.

name = name.lower() # lower() returns a copy of the string with all characters converted to lowercase.

result_digit = name.isdigit() # isdigit() returns True if all characters in the string are digits and there is at least one character, otherwise False.

result_alpha = name.isalpha() # isalpha() returns True if all characters in the string are alphabetic and there is at least one character, otherwise False.

phone_number = "555-123-4567"

result_phone = phone_number.count("-") # count() returns the number of occurrences of the specified substring in the string. In this case, it counts how many hyphens are in the phone number.
print(f"Number of hyphens in phone number: {result_phone}")

result_phone = phone_number.replace("-", "") # replace() returns a copy of the string with all occurrences of the specified substring replaced with another substring. Here, it removes the hyphens from the phone number.
# "-" is the substring to be replaced, and "" (empty string) is the substring to replace it with, effectively removing the hyphens.
print(f"Phone number without hyphens: {result_phone}")

print(help(str)) # help() can be used to get information about the string type and its methods. This will display a list of all string methods and their descriptions.

#Example:
# 1. Username is no more than 12 characters long.
# 2. Must not contain spaces.
# 3. Must not contain digits

username = input("Enter a username: ")
if len(username) > 12:
    print("Username must be no more than 12 characters long.")
elif username.find(" ") == -1:
    print("Username must not contain spaces.")
elif username.isdigit():
    print("Username must not contain digits.")
else:
    print("Username is valid.")
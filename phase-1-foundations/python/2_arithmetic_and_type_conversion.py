"""
Arithmetic and type conversion lesson.

This script demonstrates basic arithmetic operators and converting values between types.
"""

# Basic arithmetic operators:
# + addition, 
# - subtraction, 
# * multiplication, 
# / division
# // integer division, 
# % remainder, 
# ** exponentiation

value = 5
print(f"Starting value: {value}")

sum_result = value + 3
print(f"Addition 5 + 3 = {sum_result}")

diff_result = sum_result - 2
print(f"Subtraction 8 - 2 = {diff_result}")

product_result = diff_result * 4
print(f"Multiplication 6 * 4 = {product_result}")

division_result = product_result / 3
print(f"Division 24 / 3 = {division_result}")

int_division_result = product_result // 7
print(f"Integer division 24 // 7 = {int_division_result}")

remainder_result = product_result % 7
print(f"Remainder 24 % 7 = {remainder_result}")

power_result = 2 ** 3
print(f"Exponentiation 2 ** 3 = {power_result}")

# +=, -=, *=, /=, //=, %= are augmented assignment operators that update the variable in place.
value += 3 # Same as value = value + 3
print(f"After += 3: {value}")

value -= 2 # Same as value = value - 2
print(f"After -= 2: {value}")

value *= 2 # Same as value = value * 2
print(f"After *= 2: {value}")

value //= 4 # Same as value = value // 4
print(f"After //= 4: {value}")

value %= 3 # Same as value = value % 3
print(f"After %= 3: {value}")

value **= 2 # Same as value = value ** 2
print(f"After **= 2: {value}")

# Type conversion - changing a value from one type to another. 
# This is often needed when working with user input, which is always a string.

# Examples:
original_text = "123"
print(f"Original text: {original_text} ({type(original_text).__name__})") # Output: "123 (str)"

converted_int = int(original_text)
print(f"Converted to int: {converted_int} ({type(converted_int).__name__})") # Output: "Converted to int: 123 (int)"

converted_float = float(original_text)
print(f"Converted to float: {converted_float} ({type(converted_float).__name__})") # Output: "Converted to float: 123.0 (float)"

combined_text = original_text + "4"
print(f"String concatenation: {combined_text}") # Output: "String concatenation: 1234"

#.__name__ gives the name of the type for display purposes.


# Converting a number back to string allows concatenation with text.
text_result = str(converted_int) + " is a number"
print(text_result) # Output: "123 is a number"

# Boolean conversion rules:
print(f"bool('hello') = {bool('hello')}")
# Outputs True because non-empty strings are considered True.

print(f"bool('') = {bool('')} (empty string becomes False)")
# Outputs False because an empty string is considered False.

print(f"bool(0) = {bool(0)}")
# Outputs False because 0 is considered False.

print(f"bool(5) = {bool(5)}")
# Outputs True because any non-zero number is considered True.

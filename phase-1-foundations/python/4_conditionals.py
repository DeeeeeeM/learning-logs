"""
Conditionals lesson.

This script demonstrates how to use if, elif, and else statements to make decisions.
"""

age = int(input("Enter your age: "))

# if checks the first condition.
if age < 0: # Negative ages are not possible.
    print("That age is not possible.")
elif age == 0: # Newborn babies are age 0.
    print("You are a newborn.")
elif age < 13: # Children are under 13.
    print("You are a child.")
elif age < 20: # Teenagers are between 13 and 19.
    print("You are a teenager.")
elif age < 65: # Adults are between 20 and 64.
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Compare values with ==, !=, <, <=, >, >=
favorite_number = int(input("Enter your favorite number: "))

if favorite_number == 7: # Seven is a common favorite number.S
    print("Seven is often considered a lucky number.")
elif favorite_number % 2 == 0: # Check if the number is even.
    print("Your favorite number is even.")
else:
    print("Your favorite number is odd.")

# Conditions are evaluated in order, and only the first true block runs.

if favorite_number != 7:
    print("Your favorite number is not seven.")
elif favorite_number == 7:
    print("Your favorite number is seven.")
else:
    print("This will never be reached because the first two conditions cover all possibilities.")

if favorite_number <= 0:
    print("Your favorite number is zero or negative.")  
elif favorite_number > 0 and favorite_number < 10:
    print("Your favorite number is a positive single-digit number.")
elif favorite_number >= 10 and favorite_number < 100:
    print("Your favorite number is a positive two-digit number.")
else:
    print("Your favorite number is a positive three-digit number or larger.")

if favorite_number >= 100:
    print("Your favorite number is quite large!")   
elif favorite_number >= 10:
    print("Your favorite number is moderately large.")
else:
    print("Your favorite number is small.")
"""
Logical operators lesson.

This script shows how to combine conditions using or, and, and not.
"""

temperature = int(input("Enter the temperature in degrees Celsius: "))
raining = input("Is it raining? (yes/no): ").strip().lower() == "yes"

# or: true if either condition is true.
if temperature > 30 or raining:
    print("Bring water or an umbrella.")
else:
    print("The weather looks fine.")

# and: true only if both conditions are true.
sunny = input("Is it sunny? (yes/no): ").strip().lower() == "yes"

if temperature >= 20 and sunny:
    print("Nice warm and sunny weather.")
else:
    print("The weather is not both warm and sunny.")

# not: reverses the value of a boolean expression.
if not raining:
    print("You do not need an umbrella.")
else:
    print("Take an umbrella with you.")

# Multiple conditions can be combined.
if 10 < temperature < 20 and not raining:
    print("Great cool weather for a walk.")
    
# .strip() removes leading/trailing whitespace, 
# .lower() converts to lowercase.

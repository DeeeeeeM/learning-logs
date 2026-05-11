# Exception = An event that interrupts the flow of a program if not handled gracefully

# In Python, exceptions are objects that represent an error condition that can be "raised" during execution.

# When an exception occurs, normal execution stops and control jumps to the nearest matching except block.
# If no handler is found, the program terminates and prints a traceback.

# ZeroDivisionError
# Raised when attempting to divide a number by zero, e.g., 10 / 0.
# This is a subclass of ArithmeticError.
# The following code (commented out) demonstrates the exception:
# numerator = 10
# denominator = 0
# result = numerator / denominator  # Triggers the error
# print(result)

#TypeError
# 1 + "1"

# #ValueError
# int("pizza")

#1. Try - contains code that might raise an exception.
# If an exception occurs, the flow jumps to the matching except clause.
# If no exception occurs, the except blocks are skipped.
try:
    number = int(input("Enter a number: "))
    print(1/number)
    
#2. Except

# This specific except catches the ZeroDivisionError raised when the user enters 0.
except ZeroDivisionError:
    print("You can't divide by zero!")
    
# Entering a non-numeric string like "abc" triggers ValueError.
except ValueError:
    print("Numbers only!")
    
# Catches any other exception types not previously handled.
# This is a safety net to prevent the program from crashing unexpectedly.
# Use sparingly; prefer handling specific exceptions when possible.
except Exception:
    print("Something went wrong!")

#3. Finally - runs regardless of whether an exception occurred.
# It is typically used for cleanup actions such as closing files, releasing resources, or resetting states.
finally:
    print("Do some cleanup here")
    




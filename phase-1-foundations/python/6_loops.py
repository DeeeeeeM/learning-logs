"""
Loops lesson.

This script demonstrates how to repeat actions using while and for loops.
"""

# While loop example: repeat until a condition becomes false.
count = 0
print("Counting up with while:")
while count < 5:
    print(count)
    count += 1
# This loop will print numbers from 0 to 4, incrementing count by 1 each time.

# For loop example: iterate over a sequence of values.
print("Counting up with for:")
for number in range(5):
    print(number)
# This loop will also print numbers from 0 to 4, using the range function.

# range(start, stop, step) generates a sequence.
print("Even numbers from 0 to 8:")
for number in range(0, 10, 2):
    print(number)
# This loop will print even numbers from 0 to 8, starting at 0, stopping before 10, and stepping by 2.

# Loop over the characters in a string.
word = "Python"
print("Letters in the word:")
for letter in word:
    print(letter)
# This loop will print each letter in the word "Python" on a new line.

# Loop until user enters a valid answer.
answer = input("Type 'yes' when you are ready: ")
while answer.strip().lower() != "yes":
    answer = input("Please type 'yes' to continue: ")
print("Thank you! You are ready.")
# This while loop will keep asking the user to type 'yes' until they do, ignoring extra spaces and case.

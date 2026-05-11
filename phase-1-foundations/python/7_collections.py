"""
Collections lesson.

This script shows how to use lists, tuples, and sets in Python.
"""

# Lists [] are ordered and changeable.
fruits = ["apple", "banana", "cherry"]
print("List of fruits:", fruits)
print("First fruit:", fruits[0])

# Add, insert, and remove items.
fruits.append("orange")
fruits.insert(1, "kiwi")
print("After adding items:", fruits)

fruits.pop(2)  # Remove item at index 2 (cherry)
print("After popping index 2:", fruits)

fruits.remove("banana")
removed = fruits.pop()
print("Removed item:", removed)
print("Remaining list:", fruits)

# Loop through a list.
for item in fruits:
    print("Fruit:", item)

# Tuples () are ordered but immutable.
vegetables = ("carrot", "broccoli", "spinach")
print("Tuple of vegetables:", vegetables)
print("Second vegetable:", vegetables[1])

# Sets {} are unordered collections of unique values.
cars = {"Toyota", "Honda", "Ford", "Honda"}
print("Set of cars (duplicates removed):", cars)

# Add and remove from a set.
cars.add("Tesla")
print("After adding Tesla:", cars)

cars.discard("Ford")
print("After discarding Ford:", cars)

# Membership tests are fast in sets.
search = input("Enter a car to check: ")
if search in cars:
    print(f"{search} is in the set.")
else:
    print(f"{search} is not in the set.")

# Convert a list to a tuple and a tuple to a list.
fruits_tuple = tuple(fruits)
print("Fruits as tuple:", fruits_tuple)
print("Tuple length:", len(fruits_tuple))

#len() can be used with lists, tuples, and sets to get the number of items.
print("List length:", len(fruits))
print("Set length:", len(cars))
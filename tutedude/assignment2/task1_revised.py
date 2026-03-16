# Task 1: Print even or odd numbers

# Problem Statement:
# Write a Python program that:
# 1. 	Takes an integer input from the user.
# 2. 	Checks whether the number is even or odd using an if-else statement.
# 3. 	Displays the result accordingly

# Prompt user for input and convert the string response to an integer
number = int(input("Enter a number: "))

# Check if the number is divisible by 2 with no remainder
if number % 2 == 0:
	# If there is no remainder, the number is even
    print(f"{number} is an even number.")
else:
	# If there is a remainder, the number is odd
    print(f"{number} is an odd number.")

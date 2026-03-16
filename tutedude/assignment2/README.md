# Assignment 2

# Overview
This assignment includes two tasks: 
1) Checking if a number is even or odd, 
2) Calculating the sum of integers in a specified range. 


Task 1: Even or Odd Checker

# Problem Statement
Write a Python program that:
1. Takes an integer input from the user.
2. Checks whether the number is even or odd using an if-else statement.
3. Displays the result accordingly.

# Code 
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

# Instructions to Run
1. Ensure python is installed on your machine. 
2. Copy the code in a file (e.g. task1.py)
3. Run the script using the command" python task1.py
4. Follow the prompts to enter the number.

Task 2: Sum of Integers from 1 to 50

# Problem Statement
Write a Python program that:
1. Uses a for loop to iterate over numbers from 1 to 50.
2. Calculates the sum of all integers in this range.
3. Displays the final sum.

# Code:
start_number = 1
end_number = 50
total = 0

for i in range(start_number, end_number + 1):
    total += i
    
print(f"The sum of numbers from {start_number} to {end_number} is: {total}")

# Instructions to Run
1. Ensure python is installed on your machine. 
2. Copy the code in a file (e.g. task2.py)
3. Run the script using the command "python task2.py"






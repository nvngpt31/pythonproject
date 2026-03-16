# Task 2: Calculate sum of numbers 1 to 50

# Problem Statement: Write a Python program that:
# 1.   Uses a for loop to iterate over numbers from 1 to 50.
# 2.   Calculates the sum of all integers in this range.
# 3.   Displays the final sum.

start_number = 1 # Variable assignment
end_number = 50 # Variable assignment
total = 0 # Initialize accumulator variable to store the running total

# Loop through numbers 1 to 50
for i in range(start_number, end_number+1): # added space after comma
    # Accumulation pattern: add current number to total
    # This is equivalent to: total = total + i
    total += i

# Display the final result
print (f"The sum of numbers from {start_number} to {end_number} is: {total}")

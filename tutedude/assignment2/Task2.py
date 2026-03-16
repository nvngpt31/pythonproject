# Problem Statement: Write a Python program that:
# 1.   Uses a for loop to iterate over numbers from 1 to 50.
# 2.   Calculates the sum of all integers in this range.
# 3.   Displays the final sum.

start_number = 1
end_number = 50
total = 0

for i in range(start_number,end_number+1):
    total += i
    
print (f"The sum of numbers from {start_number} to {end_number} is: {total}")

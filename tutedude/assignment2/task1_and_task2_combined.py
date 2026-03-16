def check_even_odd():
    """
    Task 1: Prompts the user for a number and determines if it's even or odd.
    """
    print("\n--- Task 1: Check Even or Odd ---")
    try:
        # Prompt user for input and convert the string response to an integer
        number = int(input("Enter an integer: "))

        # Check if the number is divisible by 2 with no remainder
        if number % 2 == 0:
            # If there is no remainder, the number is even
            print(f"{number} is an even number.")
        else:
            # If there is a remainder, the number is odd
            print(f"{number} is an odd number.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

def calculate_sum_1_to_50():
    """
    Task 2: Calculates the sum of numbers from 1 to 50 and displays the result.
    """
    print("\n--- Task 2: Calculate Sum of 1 to 50 ---")
    start_number = 1
    end_number = 50
    total = 0 # Initialize accumulator variable

    # Loop through numbers 1 to 50
    for i in range(start_number, end_number + 1):
        # Accumulation pattern: add current number to total
        total += i

    # Display the final result
    print(f"The sum of numbers from {start_number} to {end_number} is: {total}")

def main_menu():
    """
    Displays a menu and calls the selected task function based on user input.
    """
    while True:
        print("\n==============================")
        print("  Python Program Main Menu")
        print("==============================")
        print("1. Run Task 1: Check Even or Odd")
        print("2. Run Task 2: Calculate Sum of 1 to 50")
        print("3. Exit Program")
        print("==============================")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            check_even_odd()
        elif choice == '2':
            calculate_sum_1_to_50()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# This ensures the main menu function runs when the script is executed
if __name__ == "__main__":
    main_menu()


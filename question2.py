# Function to check if a number is odd or even
def check_odd_even(number):
    # Check if the number is divisible by 2
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")

# Ask the user for a number
user_input = input("Please enter a number: ")

# Convert the user input to an integer
try:
    number = int(user_input)
    # Call the function to check if the number is odd or even
    check_odd_even(number)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
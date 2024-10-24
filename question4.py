# Function to perform the specified arithmetic operation
def simple_calculator(num1, num2, operation):
    # Perform the operation based on the user's choice
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        # Check for division by zero
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."


# Ask the user for the first number
user_input1 = input("Please enter the first number: ")

# Ask the user for the second number
user_input2 = input("Please enter the second number: ")

# Ask the user for the operation
operation = input("Please enter the operation (+, -, *, /): ")

# Convert user inputs to float
try:
    num1 = float(user_input1)
    num2 = float(user_input2)

    # Call the calculator function and print the result
    result = simple_calculator(num1, num2, operation)
    print(f"The result of {num1} {operation} {num2} = {result}")
except ValueError:
    print("Invalid input! Please enter valid numbers.")
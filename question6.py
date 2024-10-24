# Function to validate the password
def password_validator(input_password):
    # Check if the input password matches the predefined password
    if input_password == "python123":
        return "Access granted."
    else:
        return "Access denied."

# Ask the user for a password
user_input = input("Please enter your password: ")

# Call the password validation function and print the result
result = password_validator(user_input)
print(result)
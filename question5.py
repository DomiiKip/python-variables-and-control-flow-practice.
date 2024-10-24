# Function to categorize age
def age_category(age):
    # Determine the age category based on the provided age
    if age < 18:
        return "minor"
    elif 18 <= age <= 65:
        return "adult"
    else:
        return "senior"


# Ask the user for their age
user_input = input("Please enter your age: ")

# Convert the user input to an integer
try:
    age = int(user_input)

    # Call the function to categorize the age and print the result
    category = age_category(age)
    print(f"You are categorized as: {category}")
except ValueError:
    print("Invalid input! Please enter a valid integer for your age.")
# Function to get the day of the week based on the input number
def day_of_week(day_number):
    # Dictionary mapping numbers to days of the week
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    # Return the corresponding day or an error message if the number is invalid
    return days.get(day_number, "Invalid input.")


# Ask the user for a number
user_input = input("Please enter a number (1 to 7): ")

# Convert the user input to an integer
try:
    day_number = int(user_input)

    # Call the function to get the day of the week and print the result
    result = day_of_week(day_number)
    print(result)
except ValueError:
    print("Invalid input! Please enter a valid integer between 1 and 7.")
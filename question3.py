# Function to categorize the score into grades
def categorize_grade(score):
    # Check the score range and assign the corresponding grade
    if 90 <= score <= 100:
        grade = 'A'
    elif 80 <= score < 90:
        grade = 'B'
    elif 70 <= score < 80:
        grade = 'C'
    elif 60 <= score < 70:
        grade = 'D'
    elif 0 <= score < 60:
        grade = 'F'
    else:
        grade = None  # Invalid score

    return grade

# Ask the user for a score
user_input = input("Please enter a score (0-100): ")

# Convert the user input to a float
try:
    score = float(user_input)
    # Check for valid score range
    if 0 <= score <= 100:
        # Call the function to categorize the score
        grade = categorize_grade(score)
        print(f"The grade for the score {score} is: {grade}")
    else:
        print("Score must be between 0 and 100.")
except ValueError:
    print("Invalid input! Please enter a valid number.")
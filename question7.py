# Function to check the type of triangle
def triangle_type(a, b, c):
    # Check if the sides can form a valid triangle
    if a + b > c and a + c > b and b + c > a:
        # Check the type of triangle
        if a == b == c:
            return "Equilateral"
        elif a == b or a == c or b == c:
            return "Isosceles"
        else:
            return "Scalene"
    else:
        return "Invalid triangle"


# Ask the user for the lengths of the three sides
user_input1 = input("Please enter the length of side a: ")
user_input2 = input("Please enter the length of side b: ")
user_input3 = input("Please enter the length of side c: ")

# Convert the user inputs to floats
try:
    a = float(user_input1)
    b = float(user_input2)
    c = float(user_input3)

    # Call the triangle type function and print the result
    result = triangle_type(a, b, c)
    print(result)
except ValueError:
    print("Invalid input! Please enter valid numbers.")
# Example 8: Function Calling a Function & Math Module (Hard)
# LMS Module 11: Combining multiple functions and import math

import math

def calculate_hypotenuse(a, b):
    # Formula: square root of (a^2 + b^2)
    return math.sqrt(a**2 + b**2)

def display_result(side1, side2):
    # Function calling another function
    hyp = calculate_hypotenuse(side1, side2)
    print(f"A right triangle with sides {side1} and {side2}")
    print(f"has a hypotenuse of: {hyp:.2f}")

# Tawagin natin yung display function
display_result(3, 4)  # Dapat maging 5.00
display_result(5, 12) # Dapat maging 13.00
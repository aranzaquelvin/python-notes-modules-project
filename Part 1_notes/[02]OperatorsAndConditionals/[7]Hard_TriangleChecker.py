# Example 7: Valid Triangle (Hard)
# Checking multiple conditions using 'and'
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = float(input("Enter side C: "))

# Triangle inequality theorem: sum of two sides must be greater than the third
if (a + b > c) and (a + c > b) and (b + c > a):
    print("These sides form a valid triangle.")
else:
    print("These sides CANNOT form a triangle.")
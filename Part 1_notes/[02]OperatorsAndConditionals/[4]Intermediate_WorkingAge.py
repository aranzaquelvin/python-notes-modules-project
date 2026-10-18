# Example 4: Working Age (Intermediate)
# Using logical operators (and, or)
age = int(input("Enter your age: "))

# Legal working age is usually 18 to 60
if age >= 18 and age <= 60:
    print("You are in the working age group.")
else:
    print("You are outside the working age group.")
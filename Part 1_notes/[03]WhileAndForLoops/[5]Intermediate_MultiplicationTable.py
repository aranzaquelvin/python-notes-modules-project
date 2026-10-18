# Example 5: Multiplication Table (Intermediate)
# Using for loop to generate a table
num = int(input("Enter a number for the multiplication table: "))
print(f"--- Multiplication Table of {num} ---")

for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")
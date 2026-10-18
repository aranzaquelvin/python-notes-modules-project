# Example 1: Larger of Two Numbers (Easy)
# Basic if-else statement
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(f"{num1} is larger.")
elif num2 > num1:
    print(f"{num2} is larger.")
else:
    print("Both numbers are equal.")
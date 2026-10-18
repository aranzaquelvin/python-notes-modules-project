# Example 4: Max of Two using If-Else (Intermediate)
# Pagsasama ng If-Else (Module 2) at Functions

def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

largest = max_of_two(num1, num2)
print(f"The larger number is: {largest}")
# Example 6: Type Conversion (Intermediate)
# Kinukuha ang input bilang string, tapos ginagawang float
price = float(input("Enter the price: "))
quantity = int(input("Enter quantity: "))

total_cost = price * quantity
print(f"The total cost is: {total_cost:.2f}") # .2f means 2 decimal places
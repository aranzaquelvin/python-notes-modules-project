# Example 5: Count Even Numbers in a List (Intermediate)
# Using a loop with a condition
numbers = [1, 4, 7, 10, 12, 15, 18, 20]
even_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1

print(f"The list is: {numbers}")
print(f"There are {even_count} even numbers.")
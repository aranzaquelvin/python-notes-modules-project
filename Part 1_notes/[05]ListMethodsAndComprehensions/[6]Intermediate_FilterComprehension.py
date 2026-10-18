# Example 6: List Comprehension with 'if' (Intermediate)
# Kukunin lang yung mga pumasa sa condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Kunin lang yung even numbers
even_numbers = [x for x in numbers if x % 2 == 0]
print("Original:", numbers)
print("Even numbers only:", even_numbers)

# Kunin lang yung greater than 5
greater_than_five = [x for x in numbers if x > 5]
print("Greater than 5:", greater_than_five)
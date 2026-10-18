# Example 7: Comprehension with If-Else (Hard)
# Papalitan yung value base sa condition
numbers = [1, 2, 3, 4, 5]

# Kung even, "Even" ang ilalagay. Kung odd, "Odd".
labels = ["Even" if x % 2 == 0 else "Odd" for x in numbers]

print("Numbers:", numbers)
print("Labels:", labels)
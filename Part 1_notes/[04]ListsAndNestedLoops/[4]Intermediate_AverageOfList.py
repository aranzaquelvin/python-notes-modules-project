# Example 4: Average of a List (Intermediate)
# Combining sum and length
scores = [85, 90, 78, 92, 88]
total = 0

for score in scores:
    total += score

average = total / len(scores)
print(f"The average score is: {average:.2f}")
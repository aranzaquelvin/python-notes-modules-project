# Example 6: Print in Reverse (Intermediate)
# Using a for loop with reversed indices
colors = ["Red", "Green", "Blue", "Yellow"]

print("Original:", colors)
print("Reversed:")
for i in range(len(colors) - 1, -1, -1):
    print(colors[i])
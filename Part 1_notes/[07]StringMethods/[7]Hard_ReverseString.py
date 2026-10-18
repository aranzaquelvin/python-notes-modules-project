# Example 7: Reverse a String (Hard)
# Pinaka-mabilis na paraan gamit ang string slicing [::-1]
original = "Python"
reversed_text = original[::-1]

print("Original:", original)
print("Reversed:", reversed_text)

# Alternative way gamit ang for loop
reversed_loop = ""
for char in original:
    reversed_loop = char + reversed_loop # Idinadagdag sa unahan
print("Reversed (Loop):", reversed_loop)
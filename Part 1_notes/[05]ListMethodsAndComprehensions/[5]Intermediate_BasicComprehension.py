# Example 5: Basic List Comprehension (Intermediate)
# LMS Module 10: Mas maikling paraan para gumawa ng list

# Traditional way (For Loop)
squares_loop = []
for x in range(1, 6):
    squares_loop.append(x * x)
print("Using For Loop:", squares_loop)

# List Comprehension way (Isang linya lang!)
squares_comp = [x * x for x in range(1, 6)]
print("Using Comprehension:", squares_comp)
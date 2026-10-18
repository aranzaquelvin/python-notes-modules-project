# Example 8: Flatten a 2D Grid (Hard)
# Pagsasama ng Nested Loop (Module 8) at Comprehension (Module 10)
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Original Grid:", grid)

# Gagawing isang flat list na [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Basahin mo mula kaliwa pakanan: "Para sa bawat row, para sa bawat num, ilagay mo si num"
flat_list = [num for row in grid for num in row]

print("Flattened List:", flat_list)
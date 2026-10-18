# Example 7: Print a 2D Grid (Hard)
# LMS Module 8: Lists of Lists and Nested Loops
# Ito yung parang matrix o table
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("--- The Grid ---")
for row in grid:        # Outer loop para sa bawat row
    for item in row:    # Inner loop para sa bawat item sa row
        print(item, end=" ") 
    print() # Para mag-new line pagkatapos ng bawat row
# Example 8: Row Sums in a Grid (Hard)
# Adding all numbers per row using nested loops
grid = [
    [10, 20, 30],
    [5, 15, 25],
    [2, 4, 6]
]

print("--- Row Sums ---")
for i in range(len(grid)): # Outer loop para sa rows
    row_sum = 0
    for j in range(len(grid[i])): # Inner loop para sa columns
        row_sum += grid[i][j]
        
    print(f"Row {i+1} sum: {row_sum}")
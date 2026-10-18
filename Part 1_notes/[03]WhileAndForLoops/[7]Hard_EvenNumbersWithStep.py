# Example 7: Even Numbers with Step (Hard)
# Using range(start, stop, step) to get specific sequences
limit = int(input("Enter a limit: "))
print(f"Even numbers from 1 to {limit}:")

for i in range(2, limit + 1, 2):
    print(i, end=" ") # end=" " para magkasunod sa isang linya

print("\n") # Para mag-new line pagkatapos
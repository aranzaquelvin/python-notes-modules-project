# Example 3: Largest in a List (Easy)
# Finding the highest value without using the max() function
numbers = [45, 12, 89, 34, 67]
largest = numbers[0] # I-assume muna na yung una ang pinakamalaki

for num in numbers:
    if num > largest:
        largest = num

print(f"The largest number in the list is: {largest}")
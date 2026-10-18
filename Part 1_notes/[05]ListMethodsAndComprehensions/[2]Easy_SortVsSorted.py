# Example 2: sort() vs sorted() (Easy)
# LMS Module 9: Pinapakita ang pinagkaiba ng method at function
numbers = [45, 12, 89, 34]

# sorted() returns a NEW list, hindi binabago yung original
new_sorted_list = sorted(numbers)
print("Using sorted():", new_sorted_list)
print("Original list remains:", numbers)

# .sort() modifies the list in place (wala siyang return value / returns None)
numbers.sort()
print("Using .sort():", numbers)
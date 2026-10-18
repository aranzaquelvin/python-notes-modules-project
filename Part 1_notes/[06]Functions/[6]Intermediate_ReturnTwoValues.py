# Example 6: Returning Two Values (Intermediate)
# Pwedeng magbalik ng dalawang value gamit ang comma

def get_min_max(numbers):
    smallest = min(numbers)
    largest = max(numbers)
    return smallest, largest

my_list = [45, 12, 89, 34]
min_val, max_val = get_min_max(my_list)

print(f"List: {my_list}")
print(f"Minimum: {min_val}, Maximum: {max_val}")
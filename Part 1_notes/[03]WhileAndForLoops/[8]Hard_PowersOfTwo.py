# Example 8: Powers of Two (Hard)
# Generating a sequence of powers using a loop
limit = int(input("How many powers of 2 do you want to see? "))
current_power = 1

print("Powers of 2:")
for i in range(limit):
    print(f"2^{i} = {current_power}")
    current_power *= 2
# Example 5: Sum Numbers from a File (Intermediate)
# Dito, gagawa tayo ng file na puro numbers, tapos i-a-add natin sila

# 1. Gumawa muna ng file na may numbers
with open("numbers.txt", "w") as file:
    file.write("100\n")
    file.write("250\n")
    file.write("50\n")

# 2. Basahin at i-sum
total_sum = 0
with open("numbers.txt", "r") as file:
    for line in file:
        # Kailangan i-convert sa integer bago i-add
        total_sum += int(line.strip())

print(f"The sum of numbers in the file is: {total_sum}")
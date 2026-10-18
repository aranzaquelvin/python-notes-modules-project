# Example 8: Average of Three Numbers (Hard)
# Combining multiple inputs and formatting
print("Enter grades for 3 subjects:")
grade1 = float(input("Subject 1: "))
grade2 = float(input("Subject 2: "))
grade3 = float(input("Subject 3: "))

average = (grade1 + grade2 + grade3) / 3

print(f"\nYour average grade is: {average:.2f}")
if average >= 75:
    print("Status: Passed")
else:
    print("Status: Failed")
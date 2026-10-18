# Example 6: Sum of Digits (Intermediate)
# Using While loop and Modulo (%) to extract digits
num = int(input("Enter a number: "))
original_num = num
sum_digits = 0

while num > 0:
    digit = num % 10    # Kinukuha yung huling digit
    sum_digits += digit
    num = num // 10     # Tinatanggal yung huling digit

print(f"The sum of the digits of {original_num} is: {sum_digits}")
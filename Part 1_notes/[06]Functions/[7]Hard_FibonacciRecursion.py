# Example 7: Recursion - Fibonacci (Hard)
# LMS Module 11: Function calling itself
# Sequence: 0, 1, 1, 2, 3, 5, 8, 13...

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Function calling itself!
        return fibonacci(n - 1) + fibonacci(n - 2)

print("First 7 Fibonacci numbers:")
for i in range(7):
    print(fibonacci(i), end=" ")
print()
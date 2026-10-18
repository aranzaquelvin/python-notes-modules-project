# Example 6: Tiny Calculator using match/case (Intermediate)
# LMS Module 4: match/case (Requires Python 3.10+)
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

match operator:
    case '+':
        print(f"Result: {num1 + num2}")
    case '-':
        print(f"Result: {num1 - num2}")
    case '*':
        print(f"Result: {num1 * num2}")
    case '/':
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error: Cannot divide by zero.")
    case _:
        print("Invalid operator.")
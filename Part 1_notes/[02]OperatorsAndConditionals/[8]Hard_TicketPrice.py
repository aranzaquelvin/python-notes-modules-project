# Example 8: Ticket Price by Age with Nested Ifs (Hard)
# LMS Module 3: Nested If statements
age = int(input("Enter your age: "))
is_weekend = input("Is it a weekend? (yes/no): ").lower()

base_price = 100

if age < 12:
    if is_weekend == "yes":
        price = base_price * 0.5  # 50% discount for kids on weekend
        print("Child Weekend Discount applied.")
    else:
        price = base_price * 0.8  # 20% discount for kids on weekdays
elif age >= 60:
    price = 0  # Free for seniors
    print("Senior Citizen: Free Ticket!")
else:
    price = base_price
    print("Regular Ticket Price.")

print(f"Your ticket price is: {price}")
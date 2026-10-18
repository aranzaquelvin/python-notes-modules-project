# Example 1: Count Up to N using While Loop (Easy)
# LMS Module 5: Basic While loop
limit = int(input("Enter a number to count up to: "))
count = 1

while count <= limit:
    print(count)
    count += 1  # Important: para hindi maging infinite loop

print("Done counting!")
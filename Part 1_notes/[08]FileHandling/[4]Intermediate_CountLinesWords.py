# Example 4: Count Lines and Words (Intermediate)
try:  # <--- Umpisa ng try
    line_count = 0
    word_count = 0

    with open("my_text.txt", "r") as file:
        for line in file:
            line_count += 1
            word_count += len(line.split())

    print(f"Total Lines: {line_count}")
    print(f"Total Words: {word_count}")

except FileNotFoundError: # <--- Kapag nag-error sa try, dito pupunta
    print("Error: 'my_text.txt' not found. Run Example 1 first.")
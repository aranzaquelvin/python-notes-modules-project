# Example 6: Uppercase a File (Intermediate)
# Babasahin yung text, gagawing uppercase, tapos ise-save sa BAGONG file

# Basahin yung original file
with open("my_text.txt", "r") as file:
    original_text = file.read()

# Gawing uppercase
upper_text = original_text.upper()

# I-save sa bagong file
with open("my_text_upper.txt", "w") as file:
    file.write(upper_text)

print("Created 'my_text_upper.txt' with all uppercase letters!")
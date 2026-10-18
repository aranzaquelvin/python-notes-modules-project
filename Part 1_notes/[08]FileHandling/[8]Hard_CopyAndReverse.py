# Example 8: Read Back in Reverse / Copy a File (Hard)
# Iko-copy natin yung file, pero babaliktarin yung pagkakasulat ng mga linya

with open("my_text.txt", "r") as file:
    lines = file.readlines() # Ginagawang listahan bawat linya

# I-reverse yung listahan ng linya
lines.reverse()

# I-save sa bagong file
with open("my_text_reversed.txt", "w") as file:
    for line in lines:
        file.write(line)

print("Created 'my_text_reversed.txt' with reversed line order!")
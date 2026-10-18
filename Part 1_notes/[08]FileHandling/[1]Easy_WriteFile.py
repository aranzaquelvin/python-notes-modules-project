# Example 1: Write to a File (Easy)
# Ang "w" mode ay nagsusulat (o nag-o-overwrite kung existing na yung file)
# Ang "with" statement ay awtomatikong nagsasara ng file pagkatapos

with open("my_text.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("This is the second line.\n")

print("File created and written successfully!")
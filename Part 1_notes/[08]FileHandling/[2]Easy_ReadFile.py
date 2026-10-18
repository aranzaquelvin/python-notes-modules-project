# Example 2: Read a File (Easy)
# Ang "r" mode ay para basahin lang yung file

try:
    with open("my_text.txt", "r") as file:
        content = file.read()
        print("--- File Contents ---")
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist. Run Example 1 first.")
import os

# 2. List all files in the current folder
files = os.listdir('.')
print("Files in this folder:")
for file in files:
    print(f"- {file}")
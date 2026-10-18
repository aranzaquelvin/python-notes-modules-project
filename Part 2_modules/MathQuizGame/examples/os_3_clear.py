import os
import time

# 3. Clear the screen (works on Windows 'nt' and Mac/Linux 'posix')
print("This text will disappear in 2 seconds...")
time.sleep(2)

# This clears the terminal screen
if os.name == 'nt': # For Windows
    os.system('cls')
else: # For Mac/Linux
    os.system('clear')

print("Screen cleared!")
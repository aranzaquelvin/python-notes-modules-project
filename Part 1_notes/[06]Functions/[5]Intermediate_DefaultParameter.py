# Example 5: Default Parameters (Intermediate)
# Pwedeng bigyan ng default value yung parameter para hindi na kailangan i-input

def greet_user(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Ginamit yung default "Hello"
greet_user("Maria") 

# Pinalitan yung default value
greet_user("Juan", "Good morning") 
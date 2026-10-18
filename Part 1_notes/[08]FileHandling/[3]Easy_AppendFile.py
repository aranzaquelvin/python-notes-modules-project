# Example 3: Append to a File (Easy)
# Ang "a" mode ay nagdadagdag ng text sa DULO ng file nang hindi binubura yung dati

with open("my_text.txt", "a") as file:
    file.write("This line was appended later.\n")

print("Text appended successfully!")

# Basahin ulit para makita yung dagdag
with open("my_text.txt", "r") as file:
    print(file.read())
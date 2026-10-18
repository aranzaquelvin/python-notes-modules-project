# Example 7: Number the Lines (Hard)
# Bubasahin yung file, tapos lalagyan ng number sa unahan bawat linya

input_file = "my_text.txt"
output_file = "my_text_numbered.txt"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    line_number = 1
    for line in infile:
        # Isusulat yung format na: "1: [yung text]"
        outfile.write(f"{line_number}: {line}")
        line_number += 1

print(f"Created '{output_file}' with numbered lines!")
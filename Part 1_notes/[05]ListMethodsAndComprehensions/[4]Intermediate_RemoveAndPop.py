# Example 4: remove() and pop() (Intermediate)
# Pagtanggal ng items sa listahan
fruits = ["apple", "banana", "orange", "mango", "banana"]
print("Original:", fruits)

# .remove() - tinatanggal base sa VALUE (yung unang nakita)
fruits.remove("banana") 
print("After remove('banana'):", fruits)

# .pop() - tinatanggal base sa INDEX (at ibinabalik yung tinanggal)
removed_item = fruits.pop(1) # Tataanggalin yung "orange" (index 1)
print(f"Removed item: {removed_item}")
print("After pop(1):", fruits)
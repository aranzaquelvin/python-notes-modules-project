# Example 8: Palindrome Checker (Hard)
# Palindrome = pareho ang basa kahit baliktarin (e.g., racecar)
# Pinagsama-sama ang lower(), replace(), at slicing

def is_palindrome(text):
    # 1. Gawing lowercase lahat
    # 2. Alisin ang mga spaces
    cleaned_text = text.lower().replace(" ", "")
    
    # 3. I-check kung kaparehas sa binaliktad
    return cleaned_text == cleaned_text[::-1]

word1 = "Racecar"
word2 = "A man a plan a canal Panama"
word3 = "Python"

print(f"'{word1}' is a palindrome: {is_palindrome(word1)}")
print(f"'{word2}' is a palindrome: {is_palindrome(word2)}")
print(f"'{word3}' is a palindrome: {is_palindrome(word3)}")
# Example 6: startswith() and endswith() (Intermediate)
# Madalas gamitin sa pag-validate ng file types o URLs
filename = "document.pdf"

if filename.endswith(".pdf"):
    print(f"'{filename}' is a PDF file.")
else:
    print(f"'{filename}' is NOT a PDF file.")

url = "https://www.google.com"
if url.startswith("https"):
    print("This website is secure.")
import secrets
# Gumagawa ng random number from 10 to 50 (secure way)
# secrets.randbelow(41) gives 0 to 40, then add 10.
number = secrets.randbelow(41) + 10
print(f"Secure random number: {number}")

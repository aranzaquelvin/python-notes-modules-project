import secrets
# Gumagawa ng secure token (parang password)
# Ginagamit ito sa totoong buhay para sa security
token = secrets.token_hex(8)
print(f"Your secure token is: {token}")

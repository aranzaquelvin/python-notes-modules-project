import secrets
# Pumipili ng random item sa listahan (secure way)
operators = ['+', '-', '*', '/']
op = secrets.choice(operators)
print(f"Selected operator: {op}")

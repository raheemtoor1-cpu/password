password = input("Enter your password: ")

score = 0

# 1. Check password length
if len(password) >= 8:
    score += 1

# 2. Check for uppercase letter
if any(char.isupper() for char in password):
    score += 1

# 3. Check for lowercase letter
if any(char.islower() for char in password):
    score += 1

# 4. Check for number
if any(char.isdigit() for char in password):
    score += 1

# 5. Check for symbol
if any(not char.isalnum() for char in password):
    score += 1


# Display password strength
if score <= 2:
    print("Password Strength: WEAK")

elif score <= 4:
    print("Password Strength: MEDIUM")

else:
    print("Password Strength: STRONG")

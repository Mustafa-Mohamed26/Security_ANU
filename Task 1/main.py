import itertools

# Hardcoded password
CORRECT_PASSWORD = "hello"

# Sample dictionary list
DICTIONARY = ["password", "admin", "12345", "qwerty", "hello", "welcome"]

def dictionary_attack():
    username = input("Enter username: ")
    print("Performing Dictionary Attack...")

    for word in DICTIONARY:
        if word == CORRECT_PASSWORD:
            print(f"Success! Password found: {word}")
            return True
    
    print("Dictionary attack failed.")
    return False

def brute_force_attack():
    print("Performing Brute Force Attack...")
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for attempt in itertools.product(chars, repeat=5):  # Generate all 5-letter combinations
        attempt_password = "".join(attempt)
        if attempt_password == CORRECT_PASSWORD:
            print(f"Success! Password cracked: {attempt_password}")
            return

dictionary_attack()
print("========================================")
brute_force_attack()

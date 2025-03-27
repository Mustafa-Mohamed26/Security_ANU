# 🔐 Brute Force Attack & Dictionary Attack

## 📌 Overview
This project demonstrates two common password-cracking techniques:
1. **Dictionary Attack**: Tries passwords from a predefined list.
2. **Brute Force Attack**: Generates and tests all possible character combinations.

## 📜 How It Works
The program uses a hardcoded password (`hello`) and attempts to guess it using both methods.

### 🔹 Dictionary Attack
- Uses a predefined list of common passwords.
- Compares each word in the list with the actual password.
- If a match is found, the attack succeeds; otherwise, it fails.

**Code Snippet:**
```python
for word in DICTIONARY:
    if word == CORRECT_PASSWORD:
        print(f"Success! Password found: {word}")
        return True
```

### 🔹 Brute Force Attack
- Generates every possible 5-letter combination using letters `a-z` and `A-Z`.
- Checks each generated password against the correct password.
- If a match is found, the attack succeeds.

**Code Snippet:**
```python
for attempt in itertools.product(chars, repeat=5):
    attempt_password = "".join(attempt)
    if attempt_password == CORRECT_PASSWORD:
        print(f"Success! Password cracked: {attempt_password}")
        return
```

## 🛡️ Security Implications
- **Weak passwords** (e.g., `12345`, `admin`, `password`) can be cracked easily using a dictionary attack.
- **Short passwords** are vulnerable to brute-force attacks.
- Using **long and complex passwords** (mix of uppercase, lowercase, numbers, and special characters) increases security.

## 🚀 How to Run
1. Run the script in a Python environment:
   ```sh
   python attack_script.py
   ```
2. Enter a username when prompted (not used in the attack logic).
3. The script will attempt both a dictionary attack and a brute force attack.

## ⚠️ Disclaimer
This script is for **educational purposes only**. Do not use it for unauthorized access or malicious purposes.
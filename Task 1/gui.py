import tkinter as tk
from tkinter import messagebox
import itertools

# Hardcoded password
CORRECT_PASSWORD = "hello"

# Sample dictionary list
DICTIONARY = ["password", "admin", "12345", "qwerty", "welcome"]

# Function for dictionary attack
def dictionary_attack(username, password_label):
    for word in DICTIONARY:
        if word == CORRECT_PASSWORD:
            password_label.config(text=f"Success! Password found: {word}", fg="green")
            return True
    return False

# Function for brute force attack
def brute_force_attack(password_label):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for attempt in itertools.product(chars, repeat=5):  # Generate all 5-letter combinations
        attempt_password = "".join(attempt)
        if attempt_password == CORRECT_PASSWORD:
            password_label.config(text=f"Success! Password cracked: {attempt_password}", fg="red")
            return

# Function to start attack
def start_attack():
    username = username_entry.get().strip()
    
    if not username:
        messagebox.showwarning("Input Error", "Please enter a username.")
        return
    
    password_label.config(text="Performing Dictionary Attack...", fg="blue")
    root.update()

    if not dictionary_attack(username, password_label):
        password_label.config(text="Dictionary Attack Failed. Performing Brute Force...", fg="orange")
        root.update()
        brute_force_attack(password_label)

# Create GUI window
root = tk.Tk()
root.title("Password Cracker")
root.geometry("400x300")

# Username input
tk.Label(root, text="Enter Username:").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# Attack button
attack_button = tk.Button(root, text="Start Attack", command=start_attack)
attack_button.pack(pady=10)

# Label to display results
password_label = tk.Label(root, text="", font=("Arial", 12))
password_label.pack(pady=10)

# Run the GUI
root.mainloop()

import random
import string
import tkinter as tk
from tkinter import messagebox

# Set up the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

# Result label to display the generated password
result_label = tk.Label(root, text="Generated Password will appear here")
result_label.pack(pady=5)

# Generate password function
def on_generate_button_click():
    length = 8  # Default password length
    # Generate password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    # Update result label with generated password
    result_label.config(text=f"Generated Password: {password}")

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=on_generate_button_click)
generate_button.pack(pady=10)

# Run the application
root.mainloop()
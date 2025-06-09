import tkinter as tk
from tkinter import font

# Function to verify credentials
def login():
    username = entry_username.get()
    password = entry_password.get()
    first_letter = entry_first_letter.get()

    if username == "admin-user" and password == "turing123!" and first_letter.lower() == username[0].lower():
        root.destroy()
        print("Login attempt: SUCCESS")
        open_welcome_window()
    else:
        print("Login attempt: FAILED")

# Function to cancel the login window
def cancel():
    root.destroy()

# Function to open the welcome window
def open_welcome_window():
    welcome = tk.Tk()
    welcome.title("My App")
    welcome.geometry("400x200")

    big_font = font.Font(family="Helvetica", size=24, weight="bold")
    label = tk.Label(welcome, text="Welcome to my App", font=big_font)
    label.pack(expand=True)

    welcome.mainloop()

# Create login window
root = tk.Tk()
root.title("Login")
root.geometry("300x200")

# Username Entry
tk.Label(root, text="Username:").pack(pady=(10, 0))
entry_username = tk.Entry(root)
entry_username.pack()

# Password Entry
tk.Label(root, text="Password:").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# First Letter Entry
tk.Label(root, text="First letter of username:").pack()
entry_first_letter = tk.Entry(root)
entry_first_letter.pack()

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Login", command=login).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Cancel", command=cancel).pack(side=tk.RIGHT, padx=5)

root.mainloop()

import tkinter as tk
from tkinter import messagebox

def submit_fields():
    # Get user input from entry fields
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    # Check if passwords match
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
        return

    # Logic to store user data (you can modify this as needed)
    print("Registration successful!")
    print("Name:", name)
    print("Email:", email)
    print("Age:", age)
    print("Phone:", phone)
    print("Address:", address)
    print("Password:", password)

    # Clear the entry fields
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    confirm_password_entry.delete(0, tk.END)

    # Show the success message
    success_label.config(text="Submit Successful!", fg="green")

# Create the main application window
root = tk.Tk()
root.title("Student Registration Form")
root.configure(bg='lightblue')  # Set background color
root.geometry("350x350")  # Set fixed size
root.resizable(False, False)  # Disable maximize button

# Create a label for success message (initially empty)
success_label = tk.Label(root, text="", bg='lightblue', font=("Arial", 12, "bold"))
success_label.grid(row=0, column=0, columnspan=2, pady=5)

# Create labels and entry fields
name_label = tk.Label(root, text="Name:", bg='lightblue')
name_label.grid(row=1, column=0, padx=5, pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=1, column=1, padx=5, pady=5)

email_label = tk.Label(root, text="Email:", bg='lightblue')
email_label.grid(row=2, column=0, padx=5, pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=2, column=1, padx=5, pady=5)

age_label = tk.Label(root, text="Age:", bg='lightblue')
age_label.grid(row=3, column=0, padx=5, pady=5)
age_entry = tk.Entry(root, width=30)
age_entry.grid(row=3, column=1, padx=5, pady=5)

phone_label = tk.Label(root, text="Phone Number:", bg='lightblue')
phone_label.grid(row=4, column=0, padx=5, pady=5)
phone_entry = tk.Entry(root, width=30)
phone_entry.grid(row=4, column=1, padx=5, pady=5)

address_label = tk.Label(root, text="Address:", bg='lightblue')
address_label.grid(row=5, column=0, padx=5, pady=5)
address_entry = tk.Entry(root, width=30)
address_entry.grid(row=5, column=1, padx=5, pady=5)

password_label = tk.Label(root, text="Password:", bg='lightblue')
password_label.grid(row=6, column=0, padx=5, pady=5)
password_entry = tk.Entry(root, width=30, show="*")
password_entry.grid(row=6, column=1, padx=5, pady=5)

confirm_password_label = tk.Label(root, text="Confirm Password:", bg='lightblue')
confirm_password_label.grid(row=7, column=0, padx=5, pady=5)
confirm_password_entry = tk.Entry(root, width=30, show="*")
confirm_password_entry.grid(row=7, column=1, padx=5, pady=5)

# Create submit button
submit_button = tk.Button(root, text="Submit", command=submit_fields)
submit_button.grid(row=8, column=1, padx=5, pady=10)

# Run the main event loop
root.mainloop()